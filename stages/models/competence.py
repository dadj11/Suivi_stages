from django.db import models


class Competence(models.Model):
    libelle = models.CharField(max_length=150)

    def __str__(self):
        return self.libelle
