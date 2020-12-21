from system import models
from rest_framework import serializers
from rest_framework import validators


class PermissionSerializer(serializers.ModelSerializer):
    """权限"""

    class Meta:
        model = models.Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """角色创建"""
    insert_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")

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
    roles = RoleSerializer(many=True)


class MenuSerializer(serializers.ModelSerializer):
    """菜单"""

    class Meta:
        model = models.MenuModel
        fields = '__all__'
