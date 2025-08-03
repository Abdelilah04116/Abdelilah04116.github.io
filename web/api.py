import os
import sys
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ajouter le répertoire parent au chemin pour importer le module chatbot
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__, static_folder='../assets')
CORS(app)  # Permet les requêtes cross-origin

# Initialiser le chatbot avec gestion d'erreur
try:
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        logger.error("GOOGLE_API_KEY non trouvée dans les variables d'environnement")
        chatbot = None
    else:
        from chatbot.chatbot_logic import PortfolioChatbot
        chatbot = PortfolioChatbot(google_api_key=api_key)
        logger.info("Chatbot initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation du chatbot: {e}")
    chatbot = None

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
    
    # Vérifier si le chatbot est initialisé
    if chatbot is None:
        logger.error("Chatbot non initialisé")
        return jsonify({
            'error': 'Service temporairement indisponible. Vérifiez la configuration de l\'API.'
        }), 503
    
    try:
        logger.info(f"Traitement de la question: {data['message'][:50]}...")
        # Récupérer la réponse du chatbot
        response, _ = chatbot.get_answer(data['message'])
        logger.info("Réponse générée avec succès")
        return jsonify({'response': response})
    except Exception as e:
        logger.error(f"Erreur lors du traitement de la question: {e}")
        return jsonify({
            'error': 'Désolé, je ne peux pas répondre pour le moment. Vérifiez votre connexion ou réessayez plus tard.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)