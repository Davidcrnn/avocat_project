from django.contrib import admin
from .models import Actualite, Equipe

# Register your models here.
@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'auteur')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'bio', 'formation', 'photo')