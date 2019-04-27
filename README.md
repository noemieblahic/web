### Projet ###
Projet de programmation web INSA 4 BIM

### Auteurs ###
Blahic Noémie
Bourdet-Pees Marie
Delecroix Clara
Grosso Mélanie

### Description ###
Django est un cadre de développement web open source en Python utilisé pour développer l'application web.
Les données biologiques sont rassemblées dans un fichier tabulé. Ce fichier traite des polymorphismes (SNP), correspondant à des variations mineures du génome au sein d'une population. Ce sont des mutations très courantes, qui peuvent être à l'origine de maladies génétiques, ou de prédispositions à des maladies. Ainsi, pour chaque mutation (SNP) on retrouve l'article scientifique qui associe cette mutation à un phénotype (maladie) et les informations biologiques comme par exemple le numéro du chromosome, la position sur le génome de référence et l'identifiant unique de la mutation. Pour chaque relation mutation - maladie il y a une p_value qui permet de quantifier le degré d'association.  
Pour exploiter ces données, le fichier tabulé a été transformé en base de données utilisable par django (fichier models.py).

La page d'accueil est accessible à tout le monde. Ensuite il faut être authentifié pour accéder aux données (pouvant être confidentielles).
L'utilisateur a le choix entre :
- Parcourir la liste des phénotypes répertoriés
A chaque phénotype est associé un ou plusieurs SNP, pour chacun l'étude est précisée ainsi que les informations biologiques associées.
- Effectuer une recherche s'il connait un polymorphisme ou un chromosome en particulier.
Une seule partie de l'identifiant peut être saisie, les résultats retournés sont tous les identifiants qui comportent la valeur saisie.

Les liens externes permettent d'être :
-  redirigé vers le site du NCBI pour l’article
- redirigé vers dbSNP pour avoir de plus amples précisions sur le polymorphisme étudié.

Voir PDF qui schématise les relations entre les pages.

### Installation ###
Créez un environnement CONDA pour développer ou exécuter l'application web avec les versions suivantes :
Django 2.0.2
Python 3.6.4 :: Anaconda, Inc.

Pour lancer Django, utilisez la commande :
$ python manage.py runserver

Le serveur va se lancer, le site est accessible à l'adresse suivante (en local) :
http://127.0.0.1:8000/

### Heroku ###
Pour plus de facilité l'application a été déployée sur Heroku.
Elle est accessible à l'adresse suivante :
https://mmcn2019.herokuapp.com
