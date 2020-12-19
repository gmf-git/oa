from django.db.models import Q
from rest_framework.permissions import BasePermission
from system.models import Permission


class UrlPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        method = request.method
        path = request.path
        params = request.query_params.keys()
        res = Permission.objects.filter(
            Q(params__in=params) | Q(params__isnull=True),
            method=method,
            url=path,
            role__user=user)
        if res:
            return True
