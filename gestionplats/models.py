# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Plat(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.PositiveIntegerField()
    image = models.CharField(max_length=42)
    menu = models.ForeignKey('Menu')

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.nom

class Menu(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.PositiveIntegerField()

    def __str__(self):
        return self.nom
