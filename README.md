# Missing Person Finder

Ce projet permet de détecter les personnes disparues en utilisant la reconnaissance faciale en temps réel. L'utilisateur peut télécharger une photo d'une personne disparue et l'application comparera cette photo avec une base de données pour trouver des correspondances.

## Fonctionnalités

- **Téléchargement de photo** : L'utilisateur peut télécharger une photo d'une personne disparue.
- **Reconnaissance faciale** : L'application compare la photo téléchargée avec les visages enregistrés dans la base de données.
- **Notification** : En cas de correspondance trouvée, une notification est envoyée à l'utilisateur qui a téléchargé l'image.
- **Interface utilisateur simple** : Utilisation de React pour l'interface utilisateur et Flask pour le backend.

## Tech Stack

- **Frontend** : React.js, Tailwind CSS
- **Backend** : Flask
- **Machine Learning** : DeepFace pour la reconnaissance faciale
- **Base de données** : Firebase Firestore pour le stockage des informations utilisateur et des photos
- **Notifications** : Firebase Cloud Messaging pour les notifications en temps réel
- **Déploiement** : Firebase, GitHub

## Installation

### Prérequis

- Node.js et npm
- Python et pip
- Firebase Account

### Frontend (React)

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/zineb-elarbaoui/missing-person-finder.git
