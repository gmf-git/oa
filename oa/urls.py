"""oa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.views import static

from oa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('system.urls')),
    path('system/', include('business.urls')),
    path('system/', include('daily.urls')),
    path('system/', include('finance.urls')),
    path('system/', include('project.urls')),
    path('login/', obtain_jwt_token),
    url('^upload/(?P<model>.*)/$', views.FileUpload.as_view(), name='upload'),
    url(r'^media/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='media'),
    path(r'docs/', include_docs_urls(title='接口文档', permission_classes=[]))
]
