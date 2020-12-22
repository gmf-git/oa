from datetime import datetime

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings

from system import models
from system import serializers
from utils.jwt_response import jwt_response_payload_handler
from utils.public import DefineViewSet, get_keywords

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class PermissionViewSet(ModelViewSet):
    """权限"""
    queryset = models.Permission.objects.all()
    serializer_class = serializers.PermissionSerializer


class UserViewSet(DefineViewSet):
    """用户"""
    list_serializer = serializers.ListUserSerializer
    create_serializer = serializers.UserSerializer
    queryset = models.UserModel.objects.all()

    def get_queryset(self):
        params = self.request.query_params
        fields_map = {
            'roles__id': 'role'
        }
        keywords = get_keywords(params, fields_map)
        return self.queryset.filter(**keywords)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response_data = jwt_response_payload_handler(token, user, request)
        response = Response(response_data, status=201, headers=headers)
        expiration = (datetime.utcnow() +
                      api_settings.JWT_EXPIRATION_DELTA)
        response.set_cookie(api_settings.JWT_AUTH_COOKIE, token, expires=expiration, httponly=True)
        return response


class RoleViewSet(DefineViewSet):
    """角色"""
    create_serializer = serializers.RoleSerializer
    list_serializer = serializers.ListRoleSerializer
    queryset = models.RoleModel.objects.all()


class MenuViewSet(ModelViewSet):
    """菜单"""
    serializer_class = serializers.MenuSerializer
    queryset = models.MenuModel.objects.all()
    pagination_class = None

    def get_queryset(self):
        params = self.request.query_params
        if params.get('drop'):
            # 选择菜单
            return self.queryset.filter(child__isnull=True)
        fields_map = {
            'level': 'level'
        }
        keywords = get_keywords(params, fields_map)
        return self.queryset.filter(**keywords)
