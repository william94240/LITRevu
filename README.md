# Développez une application Web en utilisant Django

# Le Projet:

Réalisation d'un site permettant l'échange des critiques sur des livres et articles.

-----------------
<p align="center">
<img src="./static/css/images/LITrevu_banner.png" width = 1000>
</p>

# Installation

### Clonez le dépôt

Pour cloner le dépôt, il suffit d'ouvrir le terminal et effectuer la commande suivante dans le dossier de votre choix :
```bash
git clone https://github.com/william94240/LITRevu.git
```
Ensuite déplacez-vous dans le dossier créé par le clonage nommé `LITRevu` avec la commande :

```bash
cd
```

### Créez un environnement virtuel

Vous devez créer un environnement virtuel. Dans le cas péent, celui-ci est nommé `.env`  dans notre cas. Ajoutez un fichier `.gitignore` pour l'exclusion des fichiers qui ne seront pas suivis. Concrètement accéder à un terminal de votre choix et rendez-vous dans le dossier du dépôt local du projet, puis tapez la commande suivante :


```bash
python -m venv nom_de_l_environnement_virtuel
```
L'environement virtuel est crée.

### Activez votre environnement virtuel

Pour activer votre environnement virtuel, la commande est différente selon votre système d'exploitation.

#### Linux:
```bash
source chemin_de_votre_env/bin/activate
```
#### Windows :

##### CMD :
```bash
chemin_de_votre_env\Scripts\activate.bat
```

##### PowerShell :
```bash
chemin_de_votre_env\Scripts\activate.ps1
```

### Installation de différents packages

Dans ce étape vous allez procéder à l'Installation de différents packages nécessaires au bon fonctionnement de l'application. Ils sont tous listés dans le fichier texte **requirements.txt** . veuillez lancer l'installation de ces modules à l'aide de la commande :

```bash
pip install -r requirements.txt
```

### Mise en route du serveur

Vous devez vous situer dans le même repertoire que le script **manage.py**.
Pour pouvoir lancer le serveur afin de pouvoir afficher le site web, exécutez la commande suivante :

```bash
python manage.py runserver
```

Le terminal de commande affiche le message suivant :
```Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 13, 2025 - 12:22:20
Django version 5.1.2, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Vous avez alors deux possibilités : cliquez directement sur le lien dans le terminal,
ou tapez [http://127.0.0.1:8000/](http://127.0.0.1:8000/) dans votre navigateur.

# Utilisation du site web

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

Dans cette page, vous avez une rivière antéchronologique de tous les tickets et critiques que vous avez postés. Les tickets et les critiques postés par les utilisateurs que vous suivez ainsi que les critiques en réponse à vos tickets y figurent également.

Vous pourrez créer des tickets, créer des critiques à partir de zéro et des critiques en réponse à des tickets.

Vous avez également la possibilité de modifier vos différents posts.

### Onglet Posts

Dans la page des posts, vous pourrez voir tous les tickets et critiques que vous avez postés. Sur chacun de vos posts, vous aurez la possibilité de les modifier ou de les supprimer.

**Attention** : Si vous supprimez un ticket, toutes les critiques associées seront également supprimées.

### Onglet Abonnements

Dans cette page, vous pouvez voir vos abonnés, vos abonnements avec la possibilité de ne plus suivre l'utilisateur ainsi qu'une barre de recherche afin de trouver des utilisateurs à suivre.

En suivant un utilisateur, vous avez accès à tous ses posts.

### Déconnexion

Enfin, vous pourrez vous déconnecter et vous serez automatiquement redirigé vers la page de connexion.

# Flake8

L'application a été contrôlée par Flake8. Elle est par conséquent conforme à la PEP8 et autres directives.

----------
