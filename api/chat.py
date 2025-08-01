from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer les modules
sys.path.append(str(Path(__file__).parent.parent))

from chatbot.chatbot_logic import ChatbotLogic
from portfolio_data import get_portfolio_context

app = Flask(__name__)
CORS(app)

# Initialiser le chatbot
chatbot = ChatbotLogic()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint pour le chatbot"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message requis'}), 400
        
        user_message = data['message']
        
        # Obtenir le contexte du portfolio
        portfolio_context = get_portfolio_context()
        
        # Générer la réponse
        response = chatbot.generate_response(user_message, portfolio_context)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Erreur dans l'API chat: {str(e)}")
        return jsonify({
            'error': 'Erreur interne du serveur',
            'details': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de santé"""
    return jsonify({
        'status': 'healthy',
        'message': 'Chatbot API is running'
    })

if __name__ == '__main__':
    app.run(debug=True) 