from django.urls import path
from . import views

urlpatterns = [

    path('', views.fruits, name='home page'),

]