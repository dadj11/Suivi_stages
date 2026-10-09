## TP3


3. Une feuille de style

   a. Pourquoi cet endroit précis ?
Django utilise un système de recherche (les Finders) pour localiser les fichiers statiques. Le chargeur AppDirectoriesFinder cherche automatiquement un dossier nommé static/ à l'intérieur de chaque application enregistrée (INSTALLED_APPS).

Le sous-dossier supplémentaire (stages/) crée un espace de noms (namespace). Cela évite les conflits si une autre application possède également un fichier nommé style.css. Django regroupera et servira correctement le fichier sous le chemin /static/stages/style.css.
  
  b. 