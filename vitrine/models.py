from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.CharField(max_length=200)
    date_publication = models.DateField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.titre

class Equipe(models.Model):
    photo = models.FileField(upload_to='images')
    nom = models.CharField(max_length=100)
    bio = models.TextField()
    formation = models.TextField()
    engagement = models.TextField()
    fonction = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin = models.CharField(max_length= 100)