from django.db import models
from .personne import Personne
from .entreprise import Entreprise

class TuteurEntreprise(Personne):
  entreprise = models.ForeignKey(Entreprise, on_delete=models.PROTECT, related_name='tuteurs')
  def __str__(self):
        return f"Tuteur : {self.prenom} {self.nom}"