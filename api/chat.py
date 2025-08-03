import os
import json
import google.generativeai as genai

# Configuration Gemini
def setup_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return None
    
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-2.0-flash-exp')
    except Exception as e:
        print(f"Erreur Gemini: {e}")
        return None

# Contexte du portfolio (version simplifiée)
PORTFOLIO_CONTEXT = """
Abdelilah Ourti - Ingénieur en IA

FORMATION:
- Master en Intelligence Artificielle et Deep Learning
- Spécialisation en Computer Vision et NLP
- Formation en MLOps et déploiement

COMPÉTENCES TECHNIQUES:
- Langages: Python, JavaScript, Java, C++
- ML/DL: TensorFlow, PyTorch, Scikit-learn, Keras
- Computer Vision: OpenCV, PyTorch3D, Open3D
- NLP: Transformers, SpaCy, NLTK
- Cloud: AWS, Docker, Kubernetes
- Outils: Git, Jira, Power BI, Tableau

PROJETS RÉCENTS:
1. Système de Reconnaissance de Fleurs en Temps Réel
2. Analyse de Sentiments avec RAG et CrewAI
3. Chatbot Intelligent pour ENIAD
4. Pipeline MLOps avec MLflow et DVC

EXPÉRIENCE:
- Développeur IA chez plusieurs entreprises
- Projets freelance en Computer Vision
- Expertise en déploiement de modèles ML

CONTACT:
- Email: disponible sur demande
- LinkedIn: Abdelilah Ourti
- GitHub: Abdelilah04116
"""

def generate_response(question):
    """Génère une réponse avec Gemini"""
    model = setup_gemini()
    if not model:
        return "Désolé, le service n'est pas disponible pour le moment."
    
    prompt = f"""
    Tu es l'assistant IA d'Abdelilah Ourti, ingénieur en IA spécialisé en Deep Learning et Computer Vision.
    
    Contexte du portfolio:
    {PORTFOLIO_CONTEXT}
    
    Question: {question}
    
    Instructions:
    1. Réponds de manière professionnelle et détaillée
    2. Base tes réponses sur les informations du portfolio
    3. Réponds en français sauf si la question est en anglais
    4. Sois concis mais informatif
    5. Utilise un ton professionnel et amical
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Désolé, je n'ai pas pu traiter votre demande: {str(e)}"

# Point d'entrée pour Vercel
def handler(request, response):
    # Configuration CORS
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    # Gestion des requêtes OPTIONS (preflight)
    if request.method == 'OPTIONS':
        response.status = 200
        return
    
    # Gestion des requêtes POST
    if request.method == 'POST':
        try:
            # Lire le corps de la requête
            data = json.loads(request.body)
            
            # Extraire le message
            message = data.get('message', '')
            if not message:
                response.status = 400
                response.body = json.dumps({'error': 'Aucun message fourni'})
                return
            
            # Générer la réponse
            response_text = generate_response(message)
            response.body = json.dumps({'response': response_text}, ensure_ascii=False)
            
        except Exception as e:
            response.status = 500
            response.body = json.dumps({'error': f'Erreur serveur: {str(e)}'})
    else:
        response.status = 405
        response.body = json.dumps({'error': 'Méthode non autorisée'}) 