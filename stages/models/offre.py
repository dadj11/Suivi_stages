from django.db import models


class Offre(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    nb_places = models.IntegerField()
    competences = models.ManyToManyField(
        "Competence", related_name="offres", blank=True
    )

    def __str__(self):
        return self.titre
