from django.urls import path
from django.conf import settings
from .views import HomePageView, ActualiteListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('actualites', ActualiteListView.as_view(), name= 'actualites')
    
]