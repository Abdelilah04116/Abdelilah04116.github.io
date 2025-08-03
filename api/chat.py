import os
import json
import google.generativeai as genai

# Configuration Gemini
def setup_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY non trouvée")
        return None
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        print("✅ Gemini configuré avec succès")
        return model
    except Exception as e:
        print(f"❌ Erreur Gemini: {e}")
        return None

# Contexte du portfolio (version ultra-simplifiée)
PORTFOLIO_CONTEXT = """
Abdelilah Ourti - Ingénieur en IA
Formation: Master en IA et Deep Learning
Compétences: Python, TensorFlow, PyTorch, OpenCV, AWS, Docker
Projets: Reconnaissance de Fleurs, Analyse de Sentiments, Chatbot ENIAD
Expérience: Développeur IA, projets freelance Computer Vision
Contact: LinkedIn Abdelilah Ourti, GitHub Abdelilah04116
"""

def generate_response(question):
    """Génère une réponse avec Gemini"""
    print(f"🤖 Génération de réponse pour: {question}")
    
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
        print(f"✅ Réponse générée: {response.text[:50]}...")
        return response.text
    except Exception as e:
        print(f"❌ Erreur génération: {e}")
        return f"Désolé, je n'ai pas pu traiter votre demande: {str(e)}"

# Point d'entrée Vercel Functions (version garantie)
def handler(request, response):
    print(f"🚀 Handler appelé avec méthode: {request.method}")
    
    # CORS headers
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    # OPTIONS request (preflight)
    if request.method == 'OPTIONS':
        print("✅ OPTIONS request traitée")
        response.status = 200
        response.body = ''
        return
    
    # POST request
    if request.method == 'POST':
        try:
            print(f"📝 Corps de la requête: {request.body}")
            
            # Lire le corps de la requête
            data = json.loads(request.body)
            message = data.get('message', '')
            
            if not message:
                print("❌ Aucun message fourni")
                response.status = 400
                response.body = json.dumps({'error': 'Aucun message fourni'})
                return
            
            print(f"📨 Message reçu: {message}")
            
            # Générer la réponse
            response_text = generate_response(message)
            response_data = {'response': response_text}
            
            print(f"📤 Envoi de la réponse: {response_text[:50]}...")
            response.body = json.dumps(response_data)
            
        except Exception as e:
            print(f"❌ Erreur dans le handler: {e}")
            response.status = 500
            response.body = json.dumps({'error': str(e)})
    else:
        print(f"❌ Méthode non autorisée: {request.method}")
        response.status = 405
        response.body = json.dumps({'error': 'Méthode non autorisée'}) 