from django.shortcuts import render
from .models import MO_projects

# Create your views here.
def VW_home(request):
    projects = MO_projects.objects.all()
    return render(request, 'home.html', {
        'projects': projects
    })
