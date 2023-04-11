from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('otkatka', views.vorota_otkatka, name='otkatka'),
    path('raspashka', views.vorota_raspashka, name='raspashka'),
    path('garage', views.vorota_garage, name='garage'),
    path('kalitka', views.kalitka, name='kalitka'),
    path('servis', views.servis, name='servis'),
    path('contact', views.contacts, name='contact'),

]
