# Développez une application Web en utilisant Django

# Le Projet:

Le projet consiste à la réalisation d'un site web permettant l'échange des critiques sur des livres et articles.

-----------------
<div style="text-align: center;">
<img src="./static/css/images/LITrevu_banner.png" width = auto>
</div>


# L'installation

### Cloner le dépôt

Pour procéder au clonage du repositotry GitHUB, ouvrez votre terminal préféré et exécuter l'instruction suivante dans le dossier de votre choix :

```bash
git clone https://github.com/william94240/LITRevu.git
```

Ensuite positionnez-vous dans le dossier créé par le clonage nommé `LITRevu`, à l'aide de la commande :

```bash
cd < racine_du_repertoire_destination_du projet >
```

### Créer un environnement virtuel

Pour observer les bonnes pratiques, un environement virtuel est requis. Par conséquent, vous devez l'implémenter. A l'occurance, celui-ci est nommé `.env`. Pensez à ajoutez un fichier `.gitignore` pour l'exclusion des fichiers qui ne seront pas pistés. Concrètement, accéder à un terminal de votre choix et rendez-vous dans le dossier du projet si vous n'y êtes pas déjà, puis tapez la commande suivante :

```bash
python -m venv nom_de_l_environnement_virtuel
```
L'environement virtuel est crée.

### Activer votre environnement virtuel

Pour activer votre environnement virtuel, la commande est différente selon votre système d'exploitation.

#### Plateforme Linux:
```bash
source chemin_de_votre_environement/bin/activate
```
#### Plateforme Windows :

##### CMD :
```bash
chemin_de_votre_environement\Scripts\activate.bat
```

##### PowerShell :
```bash
chemin_de_votre_environement\Scripts\activate.ps1
```

### Installation de différents packages

Dans ce étape vous allez procéder à l'Installation de différents packages nécessaires au bon fonctionnement de l'application. Ils sont tous listés dans le fichier texte **requirements.txt** . veuillez lancer l'installation de ces modules à l'aide de la commande :

```bash
pip install -r requirements.txt
```

### Mise en route du serveur

Vous devez vous situer dans le même repertoire que le script **manage.py**. ce fichier est votre boussole.
Pour pouvoir lancer le serveur afin de pouvoir afficher le site web, exécutez la commande suivante :

```bash
python manage.py runserver
```

Le terminal affiche les informations suivantes :
```Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 13, 2025 - 12:22:20
Django version 5.1.2, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Deux options s'offrent à vous : cliquez directement sur le lien dans le terminal,
ou tapez [http://127.0.0.1:8000/](http://127.0.0.1:8000/) dans votre navigateur.

# L'usage du site web

L'application étant lancée, Créez-vous un compte ou connectez-vous avec les identifiants d'un utilisateur existant ci-dessous :

| Nom de compte | Mot de passe   |
| :------------ |:-------------- |
| willema       | c1secret       |
| wilhem        | c1secret       |
| wilfrid       | c1secret       |
| willybroard   | c1secret       |
| testUser10    | c1secret       |

### Onglet Flux

Lorsque vous êtes connecté, la page de Flux est premier à se manifester.
Sur cette page, vous avez une rivière antéchronologique de tous les tickets et critiques que vous avez postés,les tickets et les critiques postés par les utilisateurs que vous suivez, les critiques en réponse à vos tickets y figurent également.

Vous pourrez créer des tickets, créer des critiques à partir de zéro et des critiques en réponse à des tickets. Vous détenez également la possibilité de modifier vos différents posts.

### Onglet Posts

Dans la page des posts, vous pouvez observer tous les tickets et critiques que vous avez postés en propre. Sur chacun de vos posts, vous avez la main pour modifier ou supprimer vos créations.

**Attention** : La suppression d'un ticket, conduit fatalement à la suppression de toutes les critiques associées.

### Onglet Abonnements

Sur cette page, il est question de voir les activités de vos abonnés et de créer des abonnements. La possibilité de trouver des utilisateurs à suivre à l'aide d'une liste déroulante et l'option inverse de ne plus suivre un utilisateur vous sont offertes. En suivant un utilisateur, vous avez accès à tous ses posts.

### Déconnexion

A la fin, losrque vous vous déconnectez, vous êtes automatiquement redirigé vers la page de connexion.

# Flake8

L'application a été passée sous la moulinette de Flake8. Elle est par conséquent conforme à la PEP8 et à d'autres directives.

----------
