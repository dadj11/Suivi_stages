from django.contrib import admin

# Register your models here.
from .models import (
    Personne,
    Etudiant,
    TuteurEntreprise,
    EnseignantReferent,
    Entreprise,
    Competence,
    Offre,
    Stage,
    Candidature,
)



@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ["nom", "ville", "secteur"]
    search_fields = ["nom", "ville"]




@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['matricule', 'promotion']
    search_fields = ['matricule', 'promotion', 'nom', 'prenom', 'email']

@admin.register(TuteurEntreprise)
class TuteurAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom', 'email']

@admin.register(EnseignantReferent)
class EnseignantAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'prenom', 'email']


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'nb_places']
    search_fields = ['titre', 'description']

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['sujet', 'entreprise', 'etudiant', 'date_debut', 'date_fin']
    list_filter = ['date_debut', 'entreprise']
    search_fields = ['sujet', 'description']

@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display = ['etudiant', 'statut', 'date_depot', 'offre', 'stage']
    list_filter = ['statut', 'date_depot']