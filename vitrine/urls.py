from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ActualiteListView, ActualiteDetailView, EquipeListView, EquipeDetailView, emailView, successView, ExpertiseView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('actualites', ActualiteListView.as_view(), name= 'actualites'),
    path('actualite/<int:pk>', ActualiteDetailView.as_view(), name='actualite-detail'),
    path('equipe', EquipeListView.as_view(), name='equipe'),
    path('equipe/<int:pk>', EquipeDetailView.as_view(), name='equipe-detail'),
    path('contact/', emailView, name='contact'),
    path('success/', successView, name='success'), 
    path('expertise/', ExpertiseView.as_view(), name='expertise')
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

