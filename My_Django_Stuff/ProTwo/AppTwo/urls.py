from django.urls import path
from AppTwo import views

urlpatterns = [
    path('', views.app_two_index),
    path('help', views.helpMe),
    path('pictures', views.pictures),
    path('access_records_list', views.access_records_list),
    path('users_list', views.users_list),
]
