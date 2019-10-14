from django.urls import path
from django.conf import settings
from .views import HomePageView
from .views import emailView, successView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
]