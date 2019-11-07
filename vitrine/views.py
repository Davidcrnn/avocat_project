from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Actualite, Equipe
from datetime import datetime


from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Actualite

    def get(self, request):
         actualites = Actualite.objects.all()
         stu = {"actualites": actualites}
         return render(request, 'home.html', stu)


class ActualiteListView(ListView):
    model = Actualite
    template_name = 'actualite_list.html'


class ActualiteDetailView(DetailView):
    model = Actualite
    template_name = 'actualites_detail.html'


class EquipeListView(ListView):
    model = Equipe
    template_name = 'equipe_list.html'
    

class EquipeDetailView(DetailView):
    model = Equipe
    template_name = 'equipe_detail.html'


class ExpertiseView(TemplateView):
    template_name= 'expertise.html'

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Objet']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            
            try:
                send_mail(subject, message, from_email, ['david.crenin@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')