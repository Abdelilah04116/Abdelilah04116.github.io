from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import time

app = Flask(__name__)
CORS(app)

# Configuration pour Vercel (timeout 30 secondes)
VERCEL_TIMEOUT = 30

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
        
        # Générer la réponse
        response = generate_response(user_message)
        
        # Vérifier le timeout final
        if time.time() - start_time > VERCEL_TIMEOUT:
            return jsonify({'error': 'Timeout - requête trop longue'}), 408
        
        return jsonify({
            'response': response,
            'status': 'success',
            'execution_time': round(time.time() - start_time, 2)
        })
        
    except Exception as e:
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
        'version': '2.0.0',
        'optimized': True,
        'size': 'ultra-minimal'
    })

@app.route('/api/info', methods=['GET'])
def info():
    """Endpoint d'informations sur le chatbot"""
    return jsonify({
        'name': f"{PORTFOLIO_DATA['name']} Chatbot",
        'version': '2.0.0',
        'description': 'Chatbot IA ultra-optimisé pour portfolio',
        'features': [
            'Réponses sur le profil professionnel',
            'Informations sur les compétences',
            'Détails des projets',
            'Contact et formation',
            'Ultra-minimal pour Vercel'
        ],
        'optimized_for_vercel': True,
        'no_external_dependencies': True
    })

@app.route('/api/profile', methods=['GET'])
def profile():
    """Endpoint pour obtenir le profil complet"""
    return jsonify({
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
    })

if __name__ == '__main__':
    app.run(debug=True) 