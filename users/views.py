from rest_framework import viewsets
from users.serializer import UserSerializer
from users.models import User


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    # Usar modelo a través del ORM
    queryset = User.objects.all()
