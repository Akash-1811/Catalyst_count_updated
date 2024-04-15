"""
URL configuration for Catalyst_count project.

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
from django.urls import path,include
from login_signup import views as login_views
from upload_data import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_signup/',include('login_signup.urls')),
    path('upload_data/',include('upload_data.urls')),
    path('upload_data_api/',include('upload_data.api_urls')),
    path('',login_views.signup)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
