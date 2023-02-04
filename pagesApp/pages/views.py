from importlib.resources import path
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "htmlPages/home.html"

class AboutPageView(TemplateView):
    template_name = "htmlPages/about.html"
