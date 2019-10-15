from django.contrib import admin
from .models import Actualite

# Register your models here.
@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'auteur')
    