from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Attempt to find the user by email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # If not found by email, try to find by username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None
