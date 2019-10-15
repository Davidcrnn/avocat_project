from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.CharField(max_length=200)

    def __str__(self):
        return self.titre

