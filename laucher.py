#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur automatique pour le système de tickets 0x00
Lance automatiquement le backend et le frontend en un seul clic
"""

import subprocess
import sys
import time
import webbrowser
import os

def print_banner():
    """Affiche la bannière de démarrage"""
    print("\n" + "="*60)
    print("        Système de Gestion de Tickets 0x00")
    print("="*60 + "\n")

def check_python():
    """Vérifie que Python est installé"""
    print("✓ Python détecté:", sys.version.split()[0])

def install_dependencies():
    """Installe les dépendances si nécessaire"""
    print("\n[1/4] Vérification des dépendances...")
    try:
        import flask
        import flask_cors
        print("✓ Dépendances déjà installées")
    except ImportError:
        print("⚠ Installation des dépendances en cours...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "flask-cors", "pyjwt"])
            print("✓ Dépendances installées avec succès")
        except Exception as e:
            print(f"✗ Erreur lors de l'installation: {e}")
            print("  Essayez manuellement: pip install flask flask-cors pyjwt")
            input("\nAppuyez sur Entrée pour continuer quand même...")

def start_backend():
    """Démarre le serveur backend Flask"""
    print("\n[2/4] Démarrage du serveur Backend (API)...")
    try:
        # Lancer server.py dans un sous-processus
        process = subprocess.Popen(
            [sys.executable, "server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        time.sleep(3)  # Attendre que le serveur démarre
        print("✓ Backend démarré sur http://localhost:5000")
        return process
    except Exception as e:
        print(f"✗ Erreur lors du démarrage du backend: {e}")
        return None

def start_frontend():
    """Démarre le serveur frontend"""
    print("\n[3/4] Démarrage du serveur Frontend (Web)...")
    try:
        # Lancer le serveur HTTP Python
        process = subprocess.Popen(
            [sys.executable, "-m", "http.server", "8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        time.sleep(2)  # Attendre que le serveur démarre
        print("✓ Frontend démarré sur http://localhost:8000")
        return process
    except Exception as e:
        print(f"✗ Erreur lors du démarrage du frontend: {e}")
        return None

def open_browser():
    """Ouvre le navigateur automatiquement"""
    print("\n[4/4] Ouverture du navigateur...")
    time.sleep(2)
    try:
        webbrowser.open("http://localhost:8000")
        print("✓ Navigateur ouvert")
    except:
        print("⚠ Impossible d'ouvrir le navigateur automatiquement")
        print("  Ouvrez manuellement: http://localhost:8000")

def print_info():
    """Affiche les informations importantes"""
    print("\n" + "="*60)
    print("                ✓ SYSTÈME PRÊT !")
    print("="*60)
    print("\n📍 URLs:")
    print("   • Site Web: http://localhost:8000")
    print("   • API Backend: http://localhost:5000")
    print("\n👤 Comptes Admin:")
    print("   • Utilisateur: admin1  |  Mot de passe: admin123")
    print("   • Utilisateur: admin2  |  Mot de passe: admin456")
    print("\n⚠ IMPORTANT:")
    print("   • NE FERMEZ PAS cette fenêtre !")
    print("   • Les serveurs tournent en arrière-plan")
    print("   • Pour arrêter: Fermez cette fenêtre ou Ctrl+C")
    print("\n" + "="*60 + "\n")

def main():
    """Fonction principale"""
    # Changer vers le répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print_banner()
    check_python()
    install_dependencies()
    
    # Démarrer les serveurs
    backend_process = start_backend()
    if not backend_process:
        print("\n✗ Échec du démarrage du backend")
        print("  Vérifiez que le fichier server.py existe")
        input("\nAppuyez sur Entrée pour quitter...")
        return
    
    frontend_process = start_frontend()
    if not frontend_process:
        print("\n✗ Échec du démarrage du frontend")
        input("\nAppuyez sur Entrée pour quitter...")
        if backend_process:
            backend_process.terminate()
        return
    
    # Ouvrir le navigateur
    open_browser()
    
    # Afficher les informations
    print_info()
    
    # Garder le script actif
    try:
        print("⏳ Serveurs en cours d'exécution...")
        print("   (Appuyez sur Ctrl+C pour arrêter)\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⚠ Arrêt des serveurs en cours...")
        if backend_process:
            backend_process.terminate()
        if frontend_process:
            frontend_process.terminate()
        time.sleep(1)
        print("✓ Serveurs arrêtés. Au revoir !\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n✗ Erreur inattendue: {e}")
        input("\nAppuyez sur Entrée pour quitter...")