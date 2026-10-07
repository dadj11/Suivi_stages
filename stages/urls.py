from django.urls import path

from .views.entreprise import detail_entreprise, liste_entreprises
from .views.offre import detail_offre, liste_offres

app_name="stages"
urlpatterns = [
    path("", liste_offres, name="liste_offres"),
    path("offres/<int:pk>/", detail_offre, name="detail_offre"),
    path("entreprises/", liste_entreprises, name="liste_entreprises"),
    path("entreprises/<int:pk>/", detail_entreprise, name="detail_entreprise"),
]
