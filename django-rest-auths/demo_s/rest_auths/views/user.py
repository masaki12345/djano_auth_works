from django.shortcuts import render
from rest_framework import generics
from ..models import User
from rest_framework import viewsets


from ..serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
