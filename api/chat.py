import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import time

# Données du portfolio intégrées directement
PORTFOLIO_DATA = {
    "name": "Abdelilah Ourti",
    "title": "AI Engineer",
    "specialization": "Machine Learning and Data Science",
    "education": "ENIAD - AI Engineering",
    "experience_years": "1+ Years",
    "projects_completed": "47+",
    "location": "Morocco",
    "address": "Marrakech, Morocco",
    "email": "abdelilahourti@gmail.com",
    "phone": "+212 770539777",
    "github": "https://github.com/Abdelilah04116",
    "kaggle": "https://www.kaggle.com/abdelilahourti",
    "linkedin": "https://www.linkedin.com/in/Ourti-Abdelilah",
    
    "formation": [
        {
            "annee": "2023 – Présent",
            "diplome": "Cycle Ingénieur en Intelligence Artificielle",
            "etablissement": "ENIAD, Berkane"
        },
        {
            "annee": "2021 – 2023",
            "diplome": "DEUST en Mathématiques, Informatique et Physique",
            "etablissement": "Faculté des Sciences et Techniques, Errachidia"
        }
    ],
    
    "competences": {
        "expert": ["Python", "NumPy", "Pandas", "TensorFlow", "Keras", "SQL", "Scikit-learn"],
        "avance": ["Java", "Power BI", "Git", "FastAPI", "LangChain", "LangGraph"],
        "intermediaire": ["BERT", "GPT", "NLTK", "spaCy", "Transformer models"]
    },
    
    "experience": [
        {
            "company": "CYGNN GROUP",
            "position": "AI Engineer specialising in multi-agents systems",
            "period": "2025 - Present"
        },
        {
            "company": "SMART AUTOMATION TECHNOLOGIES",
            "position": "AI Engineer",
            "period": "2024"
        }
    ],
    
    "projets": [
        "Assistant IA basé sur un LLM (RAG) - 2025",
        "Segmentation des clients pour e-commerce - 2024",
        "Développement d'un modèle de scoring - 2024",
        "Classification de Fake News - 2024"
    ],
    
    "langues": {"francais": "B2", "anglais": "B1"},
    "soft_skills": ["Leadership", "Résolution de problèmes", "Gestion de projet"]
}

def generate_response(user_message):
    """Génère une réponse basée sur les données intégrées"""
    message_lower = user_message.lower()
    
    # Nom et identité
    if any(word in message_lower for word in ["nom", "qui", "appelle", "identité"]):
        return f"Je m'appelle {PORTFOLIO_DATA['name']}, je suis un {PORTFOLIO_DATA['title']} spécialisé en {PORTFOLIO_DATA['specialization']}."
    
    # Compétences
    elif any(word in message_lower for word in ["compétences", "technologies", "skills", "maîtrise"]):
        expert = ", ".join(PORTFOLIO_DATA['competences']['expert'][:5])
        avance = ", ".join(PORTFOLIO_DATA['competences']['avance'][:5])
        return f"Mes compétences techniques incluent : Expert en {expert}. Avancé en {avance}."
    
    # Projets
    elif any(word in message_lower for word in ["projets", "réalisations", "travaux"]):
        projets = ", ".join(PORTFOLIO_DATA['projets'][:3])
        return f"J'ai réalisé de nombreux projets incluant : {projets}."
    
    # Formation
    elif any(word in message_lower for word in ["formation", "études", "diplôme", "école"]):
        formation = PORTFOLIO_DATA['formation'][0]
        return f"Je suis actuellement en {formation['diplome']} ({formation['annee']}) à {formation['etablissement']}."
    
    # Expérience
    elif any(word in message_lower for word in ["expérience", "travail", "emploi", "entreprise"]):
        exp = PORTFOLIO_DATA['experience'][0]
        return f"J'ai travaillé chez {exp['company']} comme {exp['position']} ({exp['period']})."
    
    # Contact
    elif any(word in message_lower for word in ["contact", "email", "téléphone", "github"]):
        return f"Vous pouvez me contacter à {PORTFOLIO_DATA['email']} ou sur GitHub : {PORTFOLIO_DATA['github']}"
    
    # Localisation
    elif any(word in message_lower for word in ["où", "localisation", "adresse", "maroc"]):
        return f"Je suis basé à {PORTFOLIO_DATA['address']}, {PORTFOLIO_DATA['location']}."
    
    # Langues
    elif any(word in message_lower for word in ["langues", "français", "anglais", "niveau"]):
        langues = ", ".join([f"{lang.capitalize()} {niveau}" for lang, niveau in PORTFOLIO_DATA['langues'].items()])
        return f"Je parle {langues}."
    
    # Soft skills
    elif any(word in message_lower for word in ["soft skills", "qualités", "personnalité"]):
        skills = ", ".join(PORTFOLIO_DATA['soft_skills'])
        return f"Mes soft skills incluent : {skills}."
    
    # Réponse par défaut
    else:
        return f"Bonjour ! Je suis {PORTFOLIO_DATA['name']}, {PORTFOLIO_DATA['title']}. Je peux vous parler de mes compétences, projets, formation et expérience. Que souhaitez-vous savoir ?"

class ChatbotHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Gérer les requêtes CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        """Gérer les requêtes GET"""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if path == '/api/health':
            response = {
                'status': 'healthy',
                'message': 'Chatbot API is running',
                'version': '3.0.0',
                'optimized': True,
                'size': 'ultra-minimal-no-deps'
            }
        elif path == '/api/info':
            response = {
                'name': f"{PORTFOLIO_DATA['name']} Chatbot",
                'version': '3.0.0',
                'description': 'Chatbot IA ultra-minimal sans dépendances',
                'features': [
                    'Réponses sur le profil professionnel',
                    'Informations sur les compétences',
                    'Détails des projets',
                    'Contact et formation',
                    'Ultra-minimal sans Flask'
                ],
                'optimized_for_vercel': True,
                'no_external_dependencies': True
            }
        elif path == '/api/profile':
            response = {
                'personal_info': {
                    'name': PORTFOLIO_DATA['name'],
                    'title': PORTFOLIO_DATA['title'],
                    'specialization': PORTFOLIO_DATA['specialization'],
                    'email': PORTFOLIO_DATA['email'],
                    'github': PORTFOLIO_DATA['github'],
                    'location': PORTFOLIO_DATA['location']
                },
                'formation': PORTFOLIO_DATA['formation'],
                'competences': PORTFOLIO_DATA['competences'],
                'experience': PORTFOLIO_DATA['experience'],
                'projets': PORTFOLIO_DATA['projets']
            }
        else:
            response = {'error': 'Endpoint not found'}
            self.send_response(404)
        
        self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
    
    def do_POST(self):
        """Gérer les requêtes POST pour le chatbot"""
        if self.path == '/api/chat':
            try:
                # Lire le contenu de la requête
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                
                # Parser le JSON
                data = json.loads(post_data.decode('utf-8'))
                user_message = data.get('message', '')
                
                # Générer la réponse
                response_text = generate_response(user_message)
                
                # Préparer la réponse
                response = {
                    'response': response_text,
                    'status': 'success',
                    'version': '3.0.0'
                }
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
                
            except Exception as e:
                error_response = {
                    'error': 'Erreur interne du serveur',
                    'details': str(e)
                }
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}, ensure_ascii=False).encode('utf-8'))

# Point d'entrée pour Vercel
def handler(request, context):
    """Handler pour Vercel serverless functions"""
    return ChatbotHandler()

# Pour les tests locaux
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8000), ChatbotHandler)
    print("Serveur démarré sur http://localhost:8000")
    server.serve_forever() 