class OrderingFilter:
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_delete=False).order_by('-pk')
