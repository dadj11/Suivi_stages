# TP2
## Model par fichier :
1. Django repons: " No changes detected " car le contenue de la class ou model Entreprise n'as pas changé ; dans notre cas ca nous apprend que  django consider les fichier qui sont exposer par __init__.py  et q'il disont efectue une comparaison entre la migration precedente et la migration 	actuell  une migration est en quel que soret un fichier qui permetra de crée la table corespondent a notre model .

## La parole de la responsable des stages :
- Oui personne doit abstraite car o n'aura jamain besoin de chercher tout les etudiants
- le tuteur appartien a une entreprise cas je supose qu'on ne peut pas associer un tuteur qui est dans la rue 
- une candidature ne peut pas donner lieux a deux stage , un stage peut exister sans candidature ,staut de la candidature c'est au niveaux de python 
- « Jamais deux fois à la même offre » , pour le ganrentire il faux une contraite d'uniciter sur l'etudiant et l'offre dans la table candidature 
- Pour la promotion : je choisit un texte car on ne peut pas dire 2025-2026 (un nombre)
- 'Protect' on ne peut pas tant que ca des enfant on ne peut pas suprimer 

## Lire le SQL
1. ca a crée 9 table au total les table qui ne corespondent a auqu'un de mes models sont stage_etudiant_competence ,stage_offre_competence les existe a cause des multiplicité * * entre 2 relation ce qui engentre une table d'aissociation 
2. non il n'y a pas de table , oui c'est coherent avec mon chois 
3. un 'UNIQUE key' 
4. on_delete=models.CASCADE se traduit par ON DELETE CASCADE.

     - on_delete=models.PROTECT se traduit par ON DELETE RESTRICT (ou PROTECT selon les SGBD).

