from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('lookup', views.lookup_page, name="lookup_page"),
    path('student/add', views.StudentCreateView.as_view(), name="create_student_form"),
    path('student/<int:pk>/update', views.StudentUpdateView.as_view(), name="update_student_form"),
]
