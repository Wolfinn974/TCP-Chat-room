## Chat Room TCP (Serveur et Client)

Ce projet est une implémentation d'une simple salle de chat TCP en Python, où plusieurs utilisateurs peuvent se connecter, envoyer et recevoir des messages en temps réel. Le serveur gère la communication entre les clients et offre des commandes comme `/list` et `/exit` pour faciliter l'interaction.

## Fonctionnalités

- **Connexion des utilisateurs** : Plusieurs utilisateurs peuvent se connecter au serveur via un réseau local (localhost).
- **Envoi et réception de messages** : Les utilisateurs peuvent envoyer des messages à tous les autres utilisateurs connectés en temps réel.
- **Commandes disponibles** :
  - `/list` : Affiche la liste des utilisateurs actuellement connectés au chat.
  - `/exit` : Permet à un utilisateur de quitter le chat proprement.
  
> **Note :** La fonctionnalité de commande `/kick` (qui permet d'expulser un utilisateur) n'a pas encore été implémentée.

## Installation

### Prérequis

- Python 3.x
- Aucune bibliothèque externe n'est nécessaire pour la version actuelle.

### Exécution du serveur

1. Ouvrir un terminal ou une invite de commande.
2. Aller dans le répertoire où le projet est stocké.
3. Exécuter le script du serveur en utilisant la commande suivante :

bash
python server.py

Le serveur commencera à écouter les connexions entrantes sur l'adresse 127.0.0.1 et le port 55555.

## Exécution du client
Ouvrir un autre terminal ou invite de commande.

Aller dans le répertoire où le projet est stocké.

Exécuter le script du client en utilisant la commande suivante :
python client.py

L'utilisateur sera invité à entrer un pseudo avant de se connecter au serveur. Une fois connecté, l'utilisateur pourra commencer à envoyer et recevoir des messages.

## Commandes du client
/list : Affiche la liste des utilisateurs connectés.

/exit : Permet de quitter la session de chat et de fermer la connexion avec le serveur.

## Comment ça marche
## Le serveur
Le serveur crée un socket TCP qui écoute les connexions entrantes. Lorsqu'un client se connecte, il reçoit un message pour lui demander de choisir un pseudo. Ensuite, il peut commencer à envoyer des messages. Le serveur transmet ces messages à tous les autres clients connectés en temps réel. Le serveur gère également les commandes /list et /exit.

## Le client
Le client crée également un socket TCP pour se connecter au serveur. Une fois connecté, il peut envoyer des messages à d'autres utilisateurs. Le client peut aussi saisir des commandes comme /list pour voir les utilisateurs connectés ou /exit pour quitter la session de chat.

## Limitations
Le serveur est uniquement en mode texte et ne supporte pas encore des fonctionnalités avancées comme l'expulsion d'un utilisateur (commande /kick).

Il n'y a pas de gestion d'authentification ou de sécurité, toutes les données circulent en texte clair.

## Contribution
Les contributions à ce projet sont les bienvenues. Si vous souhaitez ajouter des fonctionnalités ou améliorer le code, n'hésitez pas à ouvrir une pull request.