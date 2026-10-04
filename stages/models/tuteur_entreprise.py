from django.db import models
from .personne import Personne

class TuteurEntreprise(Personne):
  def __str__(self):
        return f"Tuteur : {self.prenom} {self.nom}"