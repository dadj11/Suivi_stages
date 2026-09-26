# TP 1
## 1 - L'outillage
### 3 Questions

- ```uv python pin 3.14``` cette commande ramene la version de python du projet a 3.14
- Le prof impose cette version de python pour etre sur la meme longuer d'onde , avoir presque exactement le meme environement et en cas d'erreur avoir les meme erreur 

## 2 - Le projet Django
##  Lire avant d’écrire

- INSTALLED_APPS = [
    'django.contrib.admin', ]
- manage.py permet de lencer les commande django dans l'environement du projet django  or 
django-admin permet specialement  de crée configurer administrer un projet django 
								  

## 3 - Modele Entreprise 
### Specification 

---

- Pour indentifier une entreprise sans ambiguité : je combinerer le nom et la ville car dans une ville on ne peut pas avoir la meme entrprise 2 fois  ou plus 

- Pour la d'esse mail je prefaire le champs email pour reduire les erreur et faciliter le controlle des information 

- Pour le secteur d'activieté je prefere une liste de valeurs imposée ;pare la suit on devran modifier la liste si de nouveaus secteurs ce revelent a l'avenir , mais apres on ferra tout pour generaliser la liste de valeur histoire de faciliter le filtrage par secteur 


- La dernier phrase nous indique q'on devras afficher le maximum d'information permetent de reconnaitre un entreprise 

---

###  Migrate 
- la contrainte sql qui permet d'eviter les doublon dans les sql est UNIQUE 
- c'est Id c'est django qui la crée automatiquement  


## 4 - L’administration
- l'erreur apparet en valident 
- oui l'erreur est comprehensible   

##  5 - La première page
- Apres avoir changer l'emplacement du template une erreur survien en indiquant les information relative a la requete en suite les raison de l'erreur (fichier non trouvé)  et elle nous indique la ou le fichier devras ce trouver 
- L'affichage du message d'erreur et debugage depend des parametre de l'app dans notre fichier settings.py il a un atribut DEBUG detype boolean s'il est a true il s'affichera dans le cas contraire non  

## 6 - Le dépôt git