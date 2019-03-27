from . import views
from django.urls import path
urlpatterns = [
    path ('', views.home, name = 'Intpap-home'),
    path ('semester1' , views.sem1 , name = 'Intpap-sem1'),
    ]
