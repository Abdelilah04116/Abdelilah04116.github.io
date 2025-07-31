import os
import sys
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Ajouter le répertoire parent au chemin pour importer le module chatbot
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from chatbot.chatbot_logic import PortfolioChatbot

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__, static_folder='../assets')
CORS(app)  # Permet les requêtes cross-origin

# Initialiser le chatbot
api_key = os.getenv("GOOGLE_API_KEY", "")
chatbot = PortfolioChatbot(google_api_key=api_key)

@app.route('/')
def index():
    return send_from_directory('..', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('..', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': 'Aucun message fourni'}), 400
    
    try:
        # Récupérer la réponse du chatbot
        response, _ = chatbot.get_answer(data['message'])
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)