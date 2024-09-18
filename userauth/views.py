from rest_framework import generics
from .serializers import UserSerializer, User

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer