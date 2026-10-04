from django.db import models
from .personne import Personne

class Etudiant(Personne):
    matricule = models.CharField(max_length=50, unique=True)
    promotion = models.CharField(max_length=50)
    competences = models.ManyToManyField('Competence', related_name='etudiants', blank=True)