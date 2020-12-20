from rest_framework.filters import BaseFilterBackend


class OrderingFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_delete=False).order_by('-pk')
