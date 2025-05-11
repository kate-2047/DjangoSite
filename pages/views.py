from django.shortcuts import render
from .models import Project, ProjectIntro, TeamMember, AboutCo


def home(request):
    return render(request, "pages/home.html")

def about(request):
    team = TeamMember.objects.all()
    paragraph = AboutCo.objects.first()
    return render(request, "pages/about.html", {'team': team,
                                                'paragraph': paragraph})

def projects(request):
    about = ProjectIntro.objects.first()
    project = Project.objects.all()
    return render(request, "pages/projects.html", {
        'about': about,
        'projects': project
    })

def contactus(request):
    return render(request, "pages/contactus.html")