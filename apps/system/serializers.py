from system import models
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    """权限"""

    class Meta:
        model = models.Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """角色创建"""

    class Meta:
        model = models.RoleModel
        fields = '__all__'


class ListRoleSerializer(RoleSerializer):
    """角色查看"""
    permissions = PermissionSerializer(many=True)


class UserSerializer(serializers.ModelSerializer):
    """用户创建"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.UserModel
        fields = '__all__'


class ListUserSerializer(UserSerializer):
    """用户查看"""
    roles = ListRoleSerializer(many=True)
