from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, template_name="index.html")


def blog(request):
    return HttpResponse("Blog page")


def portfolio(request):
    return HttpResponse("Portfolio page")


def contacts(request):
    return HttpResponse("Contact page")
