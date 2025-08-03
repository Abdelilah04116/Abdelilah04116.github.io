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
Abdelilah Ourti - Ingénieur en IA spécialisé en Deep Learning et Computer Vision.
Formation: Master en IA et Deep Learning
Compétences: Python, TensorFlow, PyTorch, OpenCV, AWS, Docker
Projets: Reconnaissance de Fleurs, Analyse de Sentiments, Chatbot ENIAD
Expérience: Développeur IA, projets freelance Computer Vision
Contact: LinkedIn Abdelilah Ourti, GitHub Abdelilah04116
"""

def generate_response(question):
    """Génère une réponse avec Gemini"""
    model = setup_gemini()
    if not model:
        return "Désolé, le service n'est pas disponible pour le moment."
    
    prompt = f"""
    Tu es l'assistant IA d'Abdelilah Ourti, ingénieur en IA.
    
    Contexte: {PORTFOLIO_CONTEXT}
    
    Question: {question}
    
    Réponds de manière professionnelle en français, sauf si la question est en anglais.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Désolé, je n'ai pas pu traiter votre demande: {str(e)}"

# Point d'entrée Vercel Functions (syntaxe la plus simple)
def handler(request, response):
    # CORS headers
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    # OPTIONS request
    if request.method == 'OPTIONS':
        response.status = 200
        response.body = ''
        return
    
    # POST request
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            if not message:
                response.status = 400
                response.body = json.dumps({'error': 'Aucun message fourni'})
                return
            
            response_text = generate_response(message)
            response.body = json.dumps({'response': response_text})
            
        except Exception as e:
            response.status = 500
            response.body = json.dumps({'error': str(e)})
    else:
        response.status = 405
        response.body = json.dumps({'error': 'Méthode non autorisée'}) 