from datetime import date
from stages.models import (
    Entreprise, Competence, Etudiant, 
    TuteurEntreprise, EnseignantReferent, 
    Offre, Stage, Candidature
)

print("Début du peuplement...")

competences_noms = ['Python', 'Django', 'PHP / Laravel', 'JavaScript', 'PostgreSQL', 'Arduino']
competences = {nom: Competence.objects.get_or_create(libelle=nom)[0] for nom in competences_noms}

ent1, _ = Entreprise.objects.get_or_create(nom="Togo Telecom", defaults={'ville': 'Lomé'})
ent2, _ = Entreprise.objects.get_or_create(nom="Cauri Tech", defaults={'ville': 'Sokodé'})

tuteur1, _ = TuteurEntreprise.objects.get_or_create(
    email='aklesso.tuteur@togotelecom.tg',
    defaults={
        'nom': 'AKLESSO',
        'prenom': 'Koffi',
        'sexe': 'M',
        'date_naissance': date(1985, 4, 12),
        'entreprise': ent1 
    }
)

enseignant1, _ = EnseignantReferent.objects.get_or_create(
    email='prof.kpessou@ifnti.tg',
    defaults={
        'nom': 'KPESSOU',
        'prenom': 'Kodjo',
        'sexe': 'M',
        'date_naissance': date(1980, 9, 5)
    }
)

etudiant1, _ = Etudiant.objects.get_or_create(
    matricule='IFNTI-2025-001',
    defaults={
        'nom': 'DADJA',
        'prenom': 'Godwin',
        'sexe': 'M',
        'date_naissance': date(2003, 5, 12),
        'email': 'godwin.dadja@ifnti.tg',
        'promotion': '2026'
    }
)
etudiant1.competences.set([competences['Python'], competences['Django'], competences['PostgreSQL']])

etudiant2, _ = Etudiant.objects.get_or_create(
    matricule='IFNTI-2025-002',
    defaults={
        'nom': 'AGBA',
        'prenom': 'Afi',
        'sexe': 'F',
        'date_naissance': date(2004, 2, 20),
        'email': 'afi.agba@ifnti.tg',
        'promotion': '2026'
    }
)
etudiant2.competences.set([competences['PHP / Laravel'], competences['JavaScript']])

offre1, _ = Offre.objects.get_or_create(
    titre='Développeur Backend Django',
    entreprise=ent1,
    defaults={'description': 'Mise en place d\'API REST.', 'nb_places': 2}
)

offre2, _ = Offre.objects.get_or_create(
    titre='Développeur Web Laravel',
    entreprise=ent2,
    defaults={'description': 'Refonte de l\'interface interne.', 'nb_places': 1}
)

offre1.competences.set([competences['Django'], competences['Python'], competences['PostgreSQL']])

# 3. Association des compétences à offre2 (Développeur Web Laravel)
offre2.competences.set([competences['PHP / Laravel'], competences['JavaScript']])

stage1, _ = Stage.objects.get_or_create(
    etudiant=etudiant1,
    defaults={
        'sujet': 'Optimisation des performances PostgreSQL',
        'description': 'Stage axé sur l\'optimisation des requêtes complexes.',
        'date_debut': date(2026, 6, 1),
        'date_fin': date(2026, 8, 31),
        'entreprise': ent1,
        'tuteur_entreprise': tuteur1,
        'enseignant_referent': enseignant1
    }
)

candidature1, _ = Candidature.objects.get_or_create(
    etudiant=etudiant1,
    offre=offre1,
    defaults={'statut': 'VALIDEE', 'stage': stage1}
)
candidature1.stage = stage1
candidature1.save()

print("Base peuplée avec succès !")