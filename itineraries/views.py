from rest_framework import viewsets, permissions, generics
from .models import Itinerary
from .serializer import ItinerarySerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ItineraryForm

# Create your views here.
class ItineraryView(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(ItineraryView, self).get_permissions()


# Vista para listar itinerarios
class ItineraryListView(ListView):
    model = Itinerary
    template_name = 'itineraries/itinerary_list.html'
    context_object_name = 'itineraries'

# Vista para añadir un nuevo itinerario
class ItineraryCreateView(CreateView):
    model = Itinerary
    form_class = ItineraryForm
    template_name = 'itineraries/itinerary_form.html'
    success_url = reverse_lazy('itinerary-list')
    title = "Add New Itinerary"

# Vista para editar un itinerario existente
class ItineraryUpdateView(UpdateView):
    model = Itinerary
    form_class = ItineraryForm
    template_name = 'itineraries/itinerary_form.html'
    success_url = reverse_lazy('itinerary-list')
    title = "Edit Itinerary"
# Vista para borrar un itinerario existente
class ItineraryDeleteView(DeleteView):
    model = Itinerary
    template_name = 'itineraries/itinerary_confirm_delete.html'
    success_url = reverse_lazy('itinerary-list')