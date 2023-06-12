from django.urls import path
from . import views

urlpatterns = [
    path('inventory',views.inventory,name='inventory'),
    path('faculty',views.Faculty, name='faculties'),
    path('student',views.Student, name='student'),
    path('projects',views.projects, name='projects'),



]
