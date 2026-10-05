from django.db import models
from .entreprise import Entreprise
from .tuteur_entreprise import TuteurEntreprise
from .enseignant_referent import EnseignantReferent
from .etudiant import Etudiant


class Stage(models.Model):
    sujet = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField()

    entreprise = models.ForeignKey(
        Entreprise, on_delete=models.PROTECT, related_name="stages"
    )
    tuteur_entreprise = models.ForeignKey(
        TuteurEntreprise,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stages",
    )
    enseignant_referent = models.ForeignKey(
        EnseignantReferent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stages",
    )
    etudiant = models.ForeignKey(
        Etudiant, on_delete=models.CASCADE, related_name="stages", null=True, blank=True
    )
    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
   

    def __str__(self):
        return self.sujet
