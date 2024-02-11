"""
URL configuration for dj_ecomm_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .doc_schemas import (
    urlpatterns as doc_urlpatterns
)

urlpatterns = doc_urlpatterns

urlpatterns_root = [
    path('admin/', admin.site.urls),
    # adding api app for setting endpoint
    path('api/v2/', include('product.api.urls')),
    path('api/v2/auth/', include('users.api.urls')),
]

urlpatterns += urlpatterns_root


if settings.DEBUG:
    urlpatterns_root += static(settings.MEDIA_URL,
                               document_root=settings.MEDIA_ROOT)
