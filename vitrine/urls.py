from django.urls import path
from django.conf import settings
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]