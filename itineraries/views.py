from django.db.models import Q
from django.core.mail import send_mail
from rest_framework import viewsets, permissions
from rest_framework.authtoken.admin import User
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.response import Response

from .models import Itinerary
from .serializer import ItinerarySerializer


# Create your views here.
class ItineraryView(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(ItineraryView, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_delete(self, instance):
        if instance.user == self.request.user or self.request.user in instance.collaborators.all() or self.request.user.is_staff:
            instance.delete()
        else:
            raise PermissionDenied("You are not allowed to delete this itinerary.")

    def perform_update(self, serializer):
        if serializer.instance.user == self.request.user or self.request.user in serializer.instance.collaborators.all():
            serializer.save()
        else:
            raise PermissionDenied("You are not allowed to edit this itinerary.")

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def save_itinerary(self, request, pk=None):
        # Allows users to save itineraries to their saved list
        itinerary = self.get_object()
        user_profile = request.user.userprofile  # Assuming UserProfile is linked
        user_profile.saved_itineraries.add(itinerary)
        user_profile.save()
        return Response({"status": "itinerary saved"})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def remove_saved_itinerary(self, request, pk=None):
        # Allows users to remove itineraries from their saved list
        itinerary = self.get_object()
        user_profile = request.user.userprofile
        user_profile.saved_itineraries.remove(itinerary)
        user_profile.save()
        return Response({"status": "itinerary removed from saved"})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def add_collaborator(self, request, pk=None):
        itinerary = self.get_object()
        email_or_username = request.data.get('email_or_username')
        try:
            collaborator = User.objects.get(
                Q(email=email_or_username) | Q(username=email_or_username)
            )
        except User.DoesNotExist:
            if '@' in email_or_username:
                # If it's an email, send invitation email to register
                self.send_invitation_email(email_or_username, itinerary)
                return Response({"status": "Invitation email sent to register."})
            else:
                raise NotFound("User with that email or username does not exist.")

        if request.user == itinerary.user or request.user in itinerary.collaborators.all():
            itinerary.collaborators.add(collaborator)

            self.send_collaboration_email(collaborator, itinerary)

            return Response({"status": "Collaborator added"})
        else:
            raise PermissionDenied("You are not allowed to add collaborators to this itinerary.")

    def send_invitation_email(self, email, itinerary):
        subject = f"Invitation to collaborate on the itinerary '{itinerary.name}'"
        message = f"Hello,\n\nYou have been invited to collaborate on the itinerary '{itinerary.name}' on our platform." \
                  f"\nPlease register using this email address to collaborate.\n\nBest regards,\nItinerary Team"
        from_email = 'your-email@example.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

    def send_collaboration_email(self, collaborator, itinerary):
        subject = f"You have been added as a collaborator on the itinerary '{itinerary.name}'"
        message = f"Hello {collaborator.username},\n\n" \
                  f"You have benn added as a collaborator on the itinerary '{itinerary.name}'.\n" \
                  f"You can access and collaborate on this itinerary from your account.\n\n" \
                    "Greetings,\nItineraries' team"
        from_email = 'josecarloslopezgomez1@gmail.com'
        recipient_list = [collaborator.email]

        send_mail(subject, message, from_email, recipient_list)


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def remove_collaborator(self, request, pk=None):
        itinerary = self.get_object()
        email_or_username = request.data.get('email_or_username')
        collaborator = User.objects.get(
            Q(email=email_or_username) | Q(username=email_or_username)
            )

        if request.user == itinerary.user or request.user == collaborator:
            itinerary.collaborators.remove(collaborator)
            return Response({"status": "collaborator removed"})
        else:
            raise PermissionDenied("You are not allowed to remove collaborators from this itinerary")
