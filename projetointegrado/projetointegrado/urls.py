"""projetointegrado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cgitb import html
from pipes import Template
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView

from nomedaapp.views import Hospedes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path ('',TemplateView.as_view(template_name='registration/login.html')),
    path ('menu/',TemplateView.as_view(template_name='Menu.html')),
    path ('calendario/',TemplateView.as_view(template_name='Calendario.html')),
    path ('hospedes/',Hospedes.as_view(),),
    path ('ver_hospedes/',TemplateView.as_view(template_name='VerHospedes.html')),
    path ('estoque/', TemplateView.as_view(template_name="Estoque.html"))

    
]