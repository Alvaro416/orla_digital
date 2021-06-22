from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.orla_list, name='orla_list'),
]
