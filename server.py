from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import hashlib
import secrets

app = Flask(__name__)
CORS(app)

# File paths
USERS_FILE = 'users.json'
TICKETS_FILE = 'tickets.json'

# Hardcoded admin credentials
ADMINS = {
    'admin1': hashlib.sha256('admin123'.encode()).hexdigest(),
    'admin2': hashlib.sha256('admin456'.encode()).hexdigest()
}

# Initialize data files
def init_files():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f)
    
    if not os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, 'w') as f:
            json.dump([], f)

def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def load_tickets():
    with open(TICKETS_FILE, 'r') as f:
        return json.load(f)

def save_tickets(tickets):
    with open(TICKETS_FILE, 'w') as f:
        json.dump(tickets, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token():
    return secrets.token_hex(32)

# In-memory token storage (in production, use Redis or database)
active_tokens = {}

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Nom d\'utilisateur et mot de passe requis'}), 400

    users = load_users()

    if username in users:
        return jsonify({'error': 'Nom d\'utilisateur déjà pris'}), 400

    users[username] = {
        'password': hash_password(password),
        'role': 'user',
        'created_at': datetime.now().isoformat()
    }

    save_users(users)
    return jsonify({'message': 'Utilisateur créé avec succès'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Nom d\'utilisateur et mot de passe requis'}), 400

    # Check if admin
    if username in ADMINS:
        if ADMINS[username] == hash_password(password):
            token = generate_token()
            active_tokens[token] = {'username': username, 'role': 'admin'}
            return jsonify({
                'token': token,
                'username': username,
                'role': 'admin'
            }), 200
        else:
            return jsonify({'error': 'Identifiants incorrects'}), 401

    # Check regular users
    users = load_users()
    if username not in users:
        return jsonify({'error': 'Utilisateur non trouvé'}), 401

    if users[username]['password'] != hash_password(password):
        return jsonify({'error': 'Mot de passe incorrect'}), 401

    token = generate_token()
    active_tokens[token] = {'username': username, 'role': 'user'}

    return jsonify({
        'token': token,
        'username': username,
        'role': 'user'
    }), 200

@app.route('/api/tickets', methods=['POST'])
def create_ticket():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Non autorisé'}), 401

    token = auth_header.split(' ')[1]
    if token not in active_tokens:
        return jsonify({'error': 'Token invalide'}), 401

    user_info = active_tokens[token]
    data = request.json

    discord_username = data.get('discord_username')
    reason = data.get('reason')
    additional_info = data.get('additional_info', '')

    if not discord_username or not reason:
        return jsonify({'error': 'Pseudo Discord et raison requis'}), 400

    tickets = load_tickets()
    
    ticket_id = len(tickets) + 1
    new_ticket = {
        'id': ticket_id,
        'username': user_info['username'],
        'discord_username': discord_username,
        'reason': reason,
        'additional_info': additional_info,
        'status': 'open',
        'created_at': datetime.now().isoformat()
    }

    tickets.append(new_ticket)
    save_tickets(tickets)

    return jsonify({'message': 'Ticket créé avec succès', 'ticket_id': ticket_id}), 201

@app.route('/api/admin/tickets', methods=['GET'])
def get_all_tickets():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Non autorisé'}), 401

    token = auth_header.split(' ')[1]
    if token not in active_tokens:
        return jsonify({'error': 'Token invalide'}), 401

    user_info = active_tokens[token]
    if user_info['role'] != 'admin':
        return jsonify({'error': 'Accès admin requis'}), 403

    tickets = load_tickets()
    return jsonify({'tickets': tickets}), 200

if __name__ == '__main__':
    init_files()
    print("Serveur démarré sur http://localhost:5000")
    print("\nComptes admin:")
    print("  - admin1 / admin123")
    print("  - admin2 / admin456")
    app.run(debug=True, port=5000)