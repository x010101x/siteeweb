# Système de Gestion de Tickets 0x00

Un système complet de gestion de tickets avec authentification utilisateur et interface d'administration.

## Fonctionnalités

- ✅ Sélecteur de langue (Français/Anglais)
- ✅ Menu hamburger stylisé (noir/blanc/gris)
- ✅ Système d'inscription et de connexion
- ✅ Création de tickets pour utilisateurs connectés
- ✅ Dashboard admin pour visualiser tous les tickets
- ✅ 2 comptes admin prédéfinis
- ✅ Stockage des données en JSON

## Installation

### Prérequis
- Python 3.7+
- pip

### Étapes d'installation

1. Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

2. Démarrer le serveur backend :
```bash
python server.py
```

Le serveur démarre sur `http://localhost:5000`

3. Ouvrir `index.html` dans un navigateur web

## Comptes Admin

Deux comptes administrateur sont prédéfinis :

- **Admin 1** : `admin1` / `admin123`
- **Admin 2** : `admin2` / `admin456`

## Utilisation

### Pour les utilisateurs

1. Créer un compte via "S'inscrire"
2. Se connecter avec vos identifiants
3. Créer un ticket en remplissant :
   - Pseudo Discord
   - Raison du ticket
   - Informations supplémentaires

### Pour les administrateurs

1. Se connecter avec un compte admin
2. Accéder automatiquement au dashboard admin
3. Visualiser tous les tickets créés

## Structure des fichiers

```
├── index.html              # Page d'accueil
├── login.html              # Page de connexion
├── register.html           # Page d'inscription
├── create-ticket.html      # Page de création de ticket
├── admin-dashboard.html    # Dashboard administrateur
├── style.css               # Styles globaux
├── script.js               # Logique frontend
├── server.py               # Serveur backend Flask
├── requirements.txt        # Dépendances Python
├── users.json              # Base de données utilisateurs (généré)
└── tickets.json            # Base de données tickets (généré)
```

## Technologies utilisées

- **Frontend** : HTML5, CSS3, JavaScript
- **Backend** : Python, Flask
- **Stockage** : JSON (fichiers locaux)

## Sécurité

- Mots de passe hashés avec SHA-256
- Tokens d'authentification pour les sessions
- Vérification des rôles (user/admin)
- Protection CORS configurée

## Notes

- Les données sont stockées localement dans des fichiers JSON
- Pour une utilisation en production, il est recommandé d'utiliser une vraie base de données
- Les tokens de session sont stockés en mémoire (redémarrage du serveur = déconnexion)