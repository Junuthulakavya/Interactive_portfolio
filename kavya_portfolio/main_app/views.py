

# Create your views here.
from django.shortcuts import render

def index(request): return render(request, 'main_app/index.html')
def about(request): return render(request, 'main_app/about.html')
def skills(request): return render(request, 'main_app/skills.html')
def projects(request): return render(request, 'main_app/projects.html')
def achievements(request): return render(request, 'main_app/achievements.html')
def certifications(request): return render(request, 'main_app/certifications.html')
def education(request): return render(request, 'main_app/education.html')
def contact(request): return render(request, 'main_app/contact.html')
def languages(request): return render(request, 'main_app/languages.html')
def platforms(request): return render(request, 'main_app/platforms.html')
def objective(request): return render(request, 'main_app/objective.html')
