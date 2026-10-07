from django.shortcuts import get_object_or_404, render

from ..models import Offre


def liste_offres(request):
    return render(
        request,
        "stages/liste_offres.html",
        {"offres": Offre.objects.select_related("entreprise").prefetch_related("competences")},
    )


def detail_offre(request, pk):
    offre = get_object_or_404(
        Offre.objects.select_related("entreprise").prefetch_related("competences"),
        pk=pk,
    )
    return render(request, "stages/detail_offre.html", {"offre": offre})