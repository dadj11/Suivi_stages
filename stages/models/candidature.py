from django.db import models
from .stage import Stage
from .offre import Offre
from .etudiant import Etudiant


class Candidature(models.Model):
    date_depot = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=50)

    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
        related_name="candidatures",
        null=True,
        blank=True,
    )
    offre = models.ForeignKey(
        Offre,
        on_delete=models.CASCADE,
        related_name="candidatures",
        null=True,
        blank=True,
    )
    etudiant = models.ForeignKey(
        Etudiant, on_delete=models.CASCADE, related_name="candidatures"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["etudiant", "offre"], name="candidature_unique"
            )
        ]

    def __str__(self):
        return f"Candidature de {self.etudiant} - {self.statut}"
