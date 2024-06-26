from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    return render(request, template_name="index.html")


def blog(request):
    return HttpResponse("Blog page")


def single_post(request, post_id):
    post_to_open = models.Post.objects.get(id=post_id)
    return render()


def portfolio(request):
    return HttpResponse("Portfolio page")

def single_project(request, project_id):
    project_to_open = models.Project.objects.get(id=id)
    return render()

def contacts(request):
    return HttpResponse("Contact page")
