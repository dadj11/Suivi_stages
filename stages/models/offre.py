from django.db import models


class Offre(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    nb_places = models.IntegerField()
    entreprise = models.ForeignKey(
        "Entreprise", on_delete=models.PROTECT, related_name="offres"
    )
    competences = models.ManyToManyField(
        "Competence", related_name="offres", blank=True
    )
     
    def __str__(self):
        return self.titre
