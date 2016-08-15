from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "bookstore/index.html"


class ResultView(TemplateView):
    template_name = 'bookstore/result.html'


