from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from pathlib import Path
import time

# Ajouter le répertoire parent au path pour importer les modules
sys.path.append(str(Path(__file__).parent.parent))

from chatbot.chatbot_logic import ChatbotLogic
from portfolio_data import get_portfolio_context

app = Flask(__name__)
CORS(app)

# Configuration pour Vercel (timeout 30 secondes)
VERCEL_TIMEOUT = 30

# Initialiser le chatbot
chatbot = ChatbotLogic()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint pour le chatbot"""
    start_time = time.time()
    
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message requis'}), 400
        
        user_message = data['message']
        
        # Vérifier le timeout
        if time.time() - start_time > VERCEL_TIMEOUT:
            return jsonify({'error': 'Timeout - requête trop longue'}), 408
        
        # Obtenir le contexte du portfolio
        portfolio_context = get_portfolio_context()
        
        # Vérifier le timeout
        if time.time() - start_time > VERCEL_TIMEOUT:
            return jsonify({'error': 'Timeout - requête trop longue'}), 408
        
        # Générer la réponse
        response = chatbot.generate_response(user_message, portfolio_context)
        
        # Vérifier le timeout final
        if time.time() - start_time > VERCEL_TIMEOUT:
            return jsonify({'error': 'Timeout - requête trop longue'}), 408
        
        return jsonify({
            'response': response,
            'status': 'success',
            'execution_time': round(time.time() - start_time, 2)
        })
        
    except Exception as e:
        print(f"Erreur dans l'API chat: {str(e)}")
        return jsonify({
            'error': 'Erreur interne du serveur',
            'details': str(e),
            'execution_time': round(time.time() - start_time, 2)
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