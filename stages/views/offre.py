from django.shortcuts import render


from models import Offre


def liste_offres(request):
    return render(
        request,
        "stages/liste_offres.html",
        {"offres": Offre.objects.all()},
    )