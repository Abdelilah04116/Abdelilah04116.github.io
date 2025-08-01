from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from pathlib import Path
import time
import json

# Ajouter le répertoire parent au path pour importer les modules
sys.path.append(str(Path(__file__).parent.parent))

# Import optimisé pour Vercel
try:
    from portfolio_data_vercel import get_portfolio_context
except ImportError:
    try:
        from portfolio_data import get_portfolio_context
    except ImportError:
        def get_portfolio_context():
            return "Informations sur Abdelilah Ourti - AI Engineer"

app = Flask(__name__)
CORS(app)

# Configuration pour Vercel (timeout 30 secondes)
VERCEL_TIMEOUT = 30

# Initialiser le chatbot de manière simplifiée
class SimpleChatbot:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
    
    def generate_response(self, user_message, context):
        """Génère une réponse simple basée sur le contexte"""
        try:
            # Logique simplifiée pour éviter les dépendances volumineuses
            if "nom" in user_message.lower() or "qui" in user_message.lower():
                return "Je m'appelle Abdelilah Ourti, je suis un AI Engineer spécialisé en Machine Learning et Data Science."
            
            elif "compétences" in user_message.lower() or "technologies" in user_message.lower():
                return "Mes compétences techniques incluent Python, TensorFlow, PyTorch, LangChain, FastAPI, et bien d'autres technologies IA et web."
            
            elif "projets" in user_message.lower():
                return "J'ai réalisé de nombreux projets incluant des chatbots IA, des systèmes de reconnaissance d'images, des analyses de sentiments, et des plateformes RAG."
            
            elif "formation" in user_message.lower() or "études" in user_message.lower():
                return "Je suis actuellement en Cycle Ingénieur en Intelligence Artificielle à l'ENIAD (École Nationale de l'Intelligence Artificielle et du Digital) à Berkane."
            
            elif "expérience" in user_message.lower():
                return "J'ai travaillé chez CYGNN GROUP comme AI Engineer spécialisé en systèmes multi-agents et RAG, et chez SMART AUTOMATION TECHNOLOGIES."
            
            elif "contact" in user_message.lower() or "email" in user_message.lower():
                return "Vous pouvez me contacter à abdelilahourti@gmail.com ou sur GitHub: https://github.com/Abdelilah04116"
            
            else:
                return "Bonjour ! Je suis Abdelilah Ourti, AI Engineer. Je peux vous parler de mes compétences, projets, formation et expérience. Que souhaitez-vous savoir ?"
                
        except Exception as e:
            return f"Désolé, je rencontre une difficulté technique. Veuillez réessayer. Erreur: {str(e)}"

# Initialiser le chatbot
chatbot = SimpleChatbot()

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
        'message': 'Chatbot API is running',
        'version': '1.0.0',
        'optimized': True
    })

@app.route('/api/info', methods=['GET'])
def info():
    """Endpoint d'informations sur le chatbot"""
    return jsonify({
        'name': 'Abdelilah Ourti Chatbot',
        'version': '1.0.0',
        'description': 'Chatbot IA pour portfolio',
        'features': [
            'Réponses sur le profil professionnel',
            'Informations sur les compétences',
            'Détails des projets',
            'Contact et formation'
        ],
        'optimized_for_vercel': True
    })

if __name__ == '__main__':
    app.run(debug=True) 