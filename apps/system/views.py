from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from system import models
from system import serializers
from utils.public import DefineViewSet


class PermissionViewSet(ModelViewSet):
    """权限"""
    queryset = models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class UserViewSet(DefineViewSet):
    """用户"""
    list_serializer = serializers.ListUserSerializer
    create_serializer = serializers.UserSerializer
    queryset = models.UserModel.objects
