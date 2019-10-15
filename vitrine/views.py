from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Actualite

class HomePageView(TemplateView):
    template_name = 'home.html'

class ActualiteListView(ListView):
    model = Actualite
    template_name = 'actualite_list.html'
    context_object_name = 'actualites'


