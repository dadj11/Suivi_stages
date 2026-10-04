from django.db import models


class Personne(models.Model):
    class SexeChoices(models.TextChoices):
        HOMME = "M", "Masculin"
        FEMME = "F", "Feminin"
        AUTRE = "A", "Autre"

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(
        max_length=1, choices=SexeChoices.choices, default=SexeChoices.HOMME
    )
    date_naissance = models.DateField()
    email = models.EmailField(unique=True)
    class Meta:
        abstract = True

