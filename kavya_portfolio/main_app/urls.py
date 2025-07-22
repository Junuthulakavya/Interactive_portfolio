from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('achievements/', views.achievements, name='achievements'),
    path('certifications/', views.certifications, name='certifications'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact, name='contact'),
    path('languages/', views.languages, name='languages'),
    path('platforms/', views.platforms, name='platforms'),
    path('objective/', views.objective, name='objective'),
]
