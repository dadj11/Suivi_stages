from django.db import models

# Create your models here.
class Secteur(models.TextChoices):
    INFORMATIQUE = "informatique", "Informatique"
    FINANCE = "finance", "Finance"
    SANTE = "sante", "Santé"
    INDUSTRIE = "industrie", "Industrie"
    COMMERCE = "commerce", "Commerce"
    EDUCATION = "education", "Éducation"
    AUTRE = "autre", "Autre"

class Entreprise (models.Model):
    """ Une entreprise susceptible d'accueillir un stageaire ."""

    nom=models.CharField(max_length=120,unique=True)
    ville=models.CharField(max_length=80)
    secteur=secteur = models.CharField(
        max_length=20,
        choices=Secteur.choices,
        default=Secteur.AUTRE
    )
    contact=models.EmailField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom', 'ville'],
                name='unique_nom_ville'
            ),]
        ordering=["nom"]
        verbose_name="entreprise"
        verbose_name_plural="entreprises"

    def __str__(self):
     return f"{self.nom} — {self.ville} | {self.get_secteur_display()} | {self.contact}"