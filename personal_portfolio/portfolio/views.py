from django.shortcuts import render
from .models import Project


def home(request):
    # take objects from database and then pass to html page
    projects = Project.objects.all()
    return render(request, "portfolio/home.html", {"projects": projects})
