from django.contrib import admin

# Register your models here.
from .models import Entreprise


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display=["nom","ville","secteur"]
    search_fields=["nom","ville"]