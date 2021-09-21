from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('lookup', views.lookup_page, name="lookup_page"),
    path('student/add', views.student_registration, name="create_student_form"),
    path('student/<int:student_id>/lookup', views.student_group, name="student_group"),
]
