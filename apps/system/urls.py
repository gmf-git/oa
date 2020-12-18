from rest_framework.routers import DefaultRouter
from system import views

urlpatterns = [

]
router = DefaultRouter()
router.register('permission', views.PermissionViewSet, basename='permission')
router.register('user', views.UserViewSet, basename='user')
urlpatterns += router.urls
