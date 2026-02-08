# Système de Gestion de Tickets - Plan de Développement

## Fichiers à créer

1. **index.html** - Page d'accueil avec menu de navigation et sélecteur de langue
2. **login.html** - Page de connexion pour utilisateurs et admins
3. **register.html** - Page d'inscription pour nouveaux utilisateurs
4. **create-ticket.html** - Page de création de tickets pour utilisateurs connectés
5. **admin-dashboard.html** - Tableau de bord admin pour voir tous les tickets
6. **style.css** - Styles globaux avec thème noir/blanc/gris
7. **script.js** - Logique frontend (menu, langue, validation)
8. **server.py** - Backend Python Flask pour authentification et gestion des tickets
9. **requirements.txt** - Dépendances Python

## Structure de données

### Utilisateurs
- username
- password (hashé)
- role (user/admin)

### Tickets
- id
- user_id
- discord_username
- reason
- additional_info
- created_at
- status

### Admins hardcodés
- Admin 1: username="admin1", password="admin123"
- Admin 2: username="admin2", password="admin456"

## Fonctionnalités

1. Sélecteur de langue (FR/EN) en haut à gauche
2. Menu hamburger avec options Login/Register
3. Système d'authentification utilisateur
4. Création de tickets (utilisateurs connectés uniquement)
5. Dashboard admin (accès restreint aux 2 admins)
6. Stockage des données en JSON