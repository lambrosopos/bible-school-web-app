from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('registration', views.registration_page, name="registration_page"),
    path('lookup', views.lookup_page, name="lookup_page"),
]
