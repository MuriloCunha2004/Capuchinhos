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

from nomedaapp.views import HospedesView, EstoqueView, EstoqueListView
from nomedaapp.views import HospedesListView
from nomedaapp.views import HospedeDeleteView
from nomedaapp.views import EstoqueDeleteView
from django.contrib.auth.decorators import login_required

from nomedaapp.views import GaleriaListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path ('',TemplateView.as_view(template_name='registration/login.html')),
    path ('menu/',login_required(TemplateView.as_view(template_name='Menu.html'))),
    path ('calendario/',TemplateView.as_view(template_name='Calendario.html')),
    path ('hospedes/', login_required(HospedesView.as_view())),
    path ('ver_hospedes/',login_required(HospedesListView.as_view())),
    path ('estoque/', login_required(EstoqueView.as_view())),
    path ('ver_hospedes/delete/<int:pk>',HospedeDeleteView.as_view()),
    path ('ver_estoque/delete/<int:pk>',EstoqueDeleteView.as_view()),
    path ('ver_estoque/',EstoqueListView.as_view()),
    path ('galeria/',GaleriaListView.as_view()),
    
]

#path(login_required(ViewSpaceIndx.as_view(..)),