from django.shortcuts import render

# Create your views here.

from models import Entreprise

def liste_entreprises (request):
    return render(
        request,"stages/liste_entreprises.html",
        {"entreprises":Entreprise.objects.all()},
    )