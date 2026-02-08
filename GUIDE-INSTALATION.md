# 📋 Guide d'Installation et d'Utilisation - Système de Tickets 0x00

## 📁 Organisation du Dossier

Voici comment votre dossier `/workspace/` est organisé :

```
/workspace/
│
├── 🌐 Pages HTML (Frontend)
│   ├── index.html              # Page d'accueil
│   ├── login.html              # Page de connexion
│   ├── register.html           # Page d'inscription
│   ├── create-ticket.html      # Création de tickets
│   └── admin-dashboard.html    # Dashboard administrateur
│
├── 🎨 Styles et Scripts
│   ├── style.css               # Tous les styles (noir/blanc/gris)
│   └── script.js               # Menu hamburger + changement de langue
│
├── 🐍 Backend Python
│   ├── server.py               # Serveur API Flask
│   └── requirements.txt        # Dépendances Python
│
├── 🗄️ Base de données (générés automatiquement)
│   ├── users.json              # Utilisateurs enregistrés
│   └── tickets.json            # Tickets créés
│
├── 🚀 Scripts de démarrage
│   ├── start.sh                # Pour Linux/Mac
│   └── start.bat               # Pour Windows
│
└── 📖 Documentation
    ├── README.md               # Documentation principale
    ├── GUIDE_INSTALLATION.md   # Ce fichier
    └── todo.md                 # Plan de développement
```

---

## 🚀 Méthode 1 : Démarrage Automatique (RECOMMANDÉ)

### Sur Windows :
1. Double-cliquez sur `start.bat`
2. Attendez quelques secondes
3. Ouvrez votre navigateur sur : **http://localhost:8000**

### Sur Linux/Mac :
1. Ouvrez un terminal dans `/workspace/`
2. Exécutez : `./start.sh`
3. Ouvrez votre navigateur sur : **http://localhost:8000**

---

## 🔧 Méthode 2 : Démarrage Manuel

### Étape 1 : Installer les dépendances
```bash
cd /workspace
pip install -r requirements.txt
```

### Étape 2 : Démarrer le serveur backend
**Terminal 1 :**
```bash
cd /workspace
python server.py
```
Vous verrez :
```
Serveur démarré sur http://localhost:5000
Comptes admin:
  - admin1 / admin123
  - admin2 / admin456
```

### Étape 3 : Démarrer le serveur frontend
**Terminal 2 (nouveau terminal) :**
```bash
cd /workspace
python -m http.server 8000
```

### Étape 4 : Ouvrir dans le navigateur
Allez sur : **http://localhost:8000**

---

## 👥 Comptes de Test

### Administrateurs (accès dashboard)
- **Admin 1** : `admin1` / `admin123`
- **Admin 2** : `admin2` / `admin456`

### Utilisateurs normaux
Créez votre propre compte via "S'inscrire"

---

## 🎯 Fonctionnalités

### Pour tous les visiteurs :
✅ Changement de langue (FR/EN) en haut à gauche
✅ Menu hamburger avec options Login/Register

### Pour les utilisateurs connectés :
✅ Créer des tickets avec :
   - Pseudo Discord
   - Raison du ticket
   - Informations supplémentaires

### Pour les administrateurs :
✅ Voir tous les tickets créés
✅ Informations complètes sur chaque ticket
✅ Dashboard séparé

---

## ❓ Problèmes Courants

### La page est blanche quand je double-clique sur index.html
**Solution :** Ne double-cliquez pas sur index.html ! Utilisez `start.bat` (Windows) ou `start.sh` (Linux/Mac)

### "Erreur de connexion au serveur"
**Solution :** Vérifiez que `server.py` est bien démarré (Terminal 1)

### "Port déjà utilisé"
**Solution :** Un autre programme utilise le port 5000 ou 8000. Fermez-le ou changez le port dans `server.py`

---

## 🛑 Arrêter les Serveurs

### Avec les scripts automatiques :
- **Windows** : Appuyez sur une touche dans la fenêtre
- **Linux/Mac** : Appuyez sur `Ctrl+C`

### Manuellement :
Appuyez sur `Ctrl+C` dans chaque terminal

---

## 📞 Support

Si vous rencontrez des problèmes, vérifiez :
1. Python est installé (`python --version`)
2. Les dépendances sont installées (`pip install -r requirements.txt`)
3. Les deux serveurs sont démarrés
4. Vous accédez via `http://localhost:8000` (pas en double-cliquant)

---

## 🔒 Sécurité

⚠️ **Important pour la production :**
- Changez les mots de passe admin
- Utilisez une vraie base de données (PostgreSQL, MySQL)
- Ajoutez HTTPS
- Utilisez des tokens JWT plus sécurisés
- Hashage bcrypt au lieu de SHA-256

Ce système est conçu pour le développement/test local uniquement.