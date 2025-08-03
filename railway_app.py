#!/usr/bin/env python3
"""
Application Flask pour Railway - Portfolio avec Chatbot IA
"""

from flask import Flask, request, jsonify, render_template_string
import os
import json
import requests
from datetime import datetime
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
PORT = int(os.environ.get('PORT', 5000))
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Contexte du portfolio
PORTFOLIO_CONTEXT = """
Tu es l'assistant IA d'Abdelilah Ourti. Voici mes informations complètes :

INFORMATIONS PERSONNELLES :
- Nom complet : Abdelilah Ourti
- Téléphone : +33 6 XX XX XX XX (remplacez par votre vrai numéro)
- Email : abdellah.ourti@email.com (remplacez par votre vrai email)
- Localisation : France
- Nationalité : Marocaine

FORMATION :
- Master en IA et Deep Learning
- Spécialisation en Computer Vision et Machine Learning
- Formations certifiées en développement IA

COMPÉTENCES TECHNIQUES :
- Langages : Python, JavaScript, Java, C++
- IA/ML : TensorFlow, PyTorch, Scikit-learn, OpenCV
- Cloud : AWS, Docker, Kubernetes, CI/CD
- Web : React, Node.js, Flask, Django
- Bases de données : MySQL, MongoDB, PostgreSQL

PROJETS RÉALISÉS :
1. Système de Reconnaissance de Fleurs en temps réel
   - Technologies : Python, OpenCV, TensorFlow
   - Fonctionnalités : Détection, classification, interface web

2. Analyse de Sentiments avec NLP
   - Technologies : Python, NLTK, Transformers
   - Applications : Analyse de commentaires, feedback

3. Chatbot ENIAD intelligent
   - Technologies : Python, LangChain, RAG
   - Fonctionnalités : Réponses contextuelles, apprentissage

4. Applications Computer Vision industrielles
   - Technologies : OpenCV, PyTorch, AWS
   - Applications : Contrôle qualité, détection d'objets

EXPÉRIENCE PROFESSIONNELLE :
- Développeur IA freelance (2023-présent)
  * Projets Computer Vision pour entreprises
  * Systèmes de reconnaissance d'images
  * Développement d'applications IA

- Projets académiques et personnels
  * Recherche en Deep Learning
  * Publications et contributions open source

CONTACT ET RÉSEAUX :
- LinkedIn : Abdelilah Ourti
- GitHub : Abdelilah04116
- Portfolio : https://abdelilah-ourti.railway.app
- Disponible pour : Collaborations, projets, opportunités

INSTRUCTIONS :
- Réponds de manière naturelle et professionnelle en français
- Donne des détails précis sur mes compétences et projets
- Si on demande mes coordonnées, fournis-les
- Parle de mon expérience de manière détaillée
- Sois toujours utile et précis
- Utilise un ton professionnel mais accessible
- Comprends le contexte de la question et réponds intelligemment
"""

def generate_ai_response(question):
    """Génère une réponse IA avec Gemini ou fallback local"""
    try:
        if GOOGLE_API_KEY:
            logger.info("🔄 Tentative avec API Gemini...")
            
            response = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GOOGLE_API_KEY}",
                headers={'Content-Type': 'application/json'},
                json={
                    "contents": [{
                        "parts": [{
                            "text": f"{PORTFOLIO_CONTEXT}\n\nQuestion de l'utilisateur: {question}\n\nRéponse intelligente:"
                        }]
                    }]
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['candidates'][0]['content']['parts'][0]['text']
                logger.info("✅ Réponse Gemini générée")
                return answer
            else:
                logger.warning(f"⚠️ Erreur API Gemini: {response.status_code}")
                raise Exception(f"Erreur API: {response.status_code}")
                
        else:
            logger.info("⚠️ Pas de clé API, utilisation du mode local")
            raise Exception("Pas de clé API")
            
    except Exception as e:
        logger.info(f"🔄 Fallback vers mode local: {e}")
        return generate_local_response(question)

def generate_local_response(question):
    """Système de réponses intelligentes local"""
    lower_question = question.lower().strip()
    
    # Informations personnelles
    if any(word in lower_question for word in ['téléphone', 'numéro', 'phone']):
        return "Mon numéro de téléphone est +33 6 XX XX XX XX (remplacez par votre vrai numéro). Vous pouvez également me contacter par email à abdellah.ourti@email.com ou via LinkedIn (Abdelilah Ourti)."
    
    if any(word in lower_question for word in ['email', 'mail', 'courriel']):
        return "Mon adresse email est abdellah.ourti@email.com. N'hésitez pas à me contacter pour des opportunités de collaboration ou des projets intéressants en IA."
    
    if any(word in lower_question for word in ['contact', 'joindre', 'contacter']):
        return "Vous pouvez me contacter de plusieurs façons : par téléphone au +33 6 XX XX XX XX, par email à abdellah.ourti@email.com, via LinkedIn (Abdelilah Ourti) ou GitHub (Abdelilah04116). Je suis toujours ouvert aux collaborations !"
    
    # Formation et expérience
    if any(word in lower_question for word in ['formation', 'diplôme', 'étude', 'master']):
        return "J'ai un Master en IA et Deep Learning avec une spécialisation en Computer Vision et Machine Learning. J'ai également suivi des formations certifiées en développement IA et je continue à me former sur les nouvelles technologies."
    
    if any(word in lower_question for word in ['expérience', 'travail', 'emploi', 'carrière']):
        return "Je travaille comme développeur IA freelance depuis 2023. J'ai développé plusieurs projets passionnants : systèmes de reconnaissance d'images, applications Computer Vision pour l'industrie, chatbots intelligents, et des outils d'analyse de sentiments. J'ai également une expérience en recherche en Deep Learning et en contributions open source."
    
    # Compétences et technologies
    if any(word in lower_question for word in ['compétence', 'skill', 'savoir-faire', 'technologie']):
        return "Mes compétences principales incluent Python, JavaScript, Java, C++, TensorFlow, PyTorch, OpenCV, AWS, Docker, Kubernetes, React, Node.js, Flask, Django, et bien d'autres technologies. Je suis spécialisé en Machine Learning, Deep Learning, Computer Vision et développement d'applications IA."
    
    if any(word in lower_question for word in ['python', 'tensorflow', 'pytorch', 'opencv']):
        return "Je maîtrise parfaitement Python, TensorFlow, PyTorch, OpenCV et bien d'autres technologies IA. Ces outils me permettent de développer des applications avancées en Computer Vision, Machine Learning et Deep Learning. J'ai utilisé ces technologies dans mes projets de reconnaissance de fleurs, d'analyse de sentiments et d'applications industrielles."
    
    # Projets
    if any(word in lower_question for word in ['projet', 'travail', 'réalisation', 'développé']):
        return "J'ai développé plusieurs projets passionnants : 1) Un système de reconnaissance de fleurs en temps réel avec Python et OpenCV, 2) Une analyse de sentiments avec NLP et Transformers, 3) Un chatbot ENIAD intelligent avec LangChain et RAG, 4) Des applications Computer Vision pour l'industrie. Chaque projet démontre mes compétences en IA et développement."
    
    # Localisation et informations personnelles
    if any(word in lower_question for word in ['habite', 'où', 'localisation', 'ville']):
        return "J'habite en France et je suis de nationalité marocaine. Je suis disponible pour des projets en remote ou sur site, et je peux me déplacer pour des opportunités intéressantes."
    
    if 'qui' in lower_question and any(word in lower_question for word in ['es-tu', 'êtes-vous', 'tu']):
        return "Je suis Abdelilah Ourti, ingénieur en IA passionné par le Deep Learning et la Computer Vision. J'ai un Master en IA et je travaille comme développeur freelance. Je développe des applications intelligentes et je suis toujours à la recherche de nouveaux défis technologiques."
    
    # Salutations
    if any(word in lower_question for word in ['bonjour', 'salut', 'hello']):
        return "Bonjour ! Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets, ma formation ou mon expérience. Que souhaitez-vous savoir ?"
    
    # Réponse par défaut intelligente
    return "Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets, ma formation ou mon expérience. Que souhaitez-vous savoir spécifiquement ?"

@app.route('/')
def home():
    """Page d'accueil du portfolio"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Modifier l'URL de l'API pour Railway
        html_content = html_content.replace(
            '/api/chat',
            '/api/chat'
        )
        
        return html_content
    except Exception as e:
        logger.error(f"Erreur lecture index.html: {e}")
        return f"Erreur: {e}", 500

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    """API du chatbot"""
    # CORS headers
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }
    
    # Handle preflight requests
    if request.method == 'OPTIONS':
        return '', 200, headers
    
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Aucun message fourni'}), 400, headers
        
        logger.info(f"📨 Message reçu: {message}")
        
        # Générer la réponse
        response_text = generate_ai_response(message)
        
        logger.info(f"📤 Réponse envoyée: {response_text[:100]}...")
        
        return jsonify({'response': response_text}), 200, headers
        
    except Exception as e:
        logger.error(f"❌ Erreur dans chat API: {e}")
        return jsonify({'error': str(e)}), 500, headers

@app.route('/health')
def health():
    """Endpoint de santé pour Railway"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'api_key_configured': bool(GOOGLE_API_KEY)
    })

@app.route('/assets/<path:filename>')
def assets(filename):
    """Servir les assets statiques"""
    try:
        return app.send_from_directory('assets', filename)
    except Exception as e:
        logger.error(f"Erreur asset {filename}: {e}")
        return f"Asset non trouvé: {filename}", 404

if __name__ == '__main__':
    logger.info(f"🚀 Démarrage de l'application sur le port {PORT}")
    logger.info(f"🔑 Clé API configurée: {bool(GOOGLE_API_KEY)}")
    app.run(host='0.0.0.0', port=PORT, debug=False) 