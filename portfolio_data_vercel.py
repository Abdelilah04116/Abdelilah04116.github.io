"""
Données personnelles d'Abdelilah Ourti optimisées pour Vercel
"""

PORTFOLIO_DATA = {
    "personal_info": {
        "name": "Abdelilah Ourti",
        "title": "AI Engineer",
        "specialization": "Machine Learning and Data Science",
        "education": "ENIAD - AI Engineering",
        "experience_years": "1+ Years",
        "projects_completed": "47+",
        "happy_clients": "30+",
        "location": "Morocco",
        "address": "Marrakech, Morocco",
        "email": "abdelilahourti@gmail.com",
        "phone": "+212 770539777",
        "github": "https://github.com/Abdelilah04116",
        "kaggle": "https://www.kaggle.com/abdelilahourti",
        "linkedin": "https://www.linkedin.com/in/Ourti-Abdelilah"
    },
    
    "formation": [
        {
            "annee": "2023 – Présent",
            "diplome": "Cycle Ingénieur en Intelligence Artificielle",
            "etablissement": "École Nationale de l'Intelligence Artificielle et du Digital (ENIAD), Berkane",
            "details": [
                "Formation approfondie en IA, ML et Data Science",
                "Application à des cas concrets avec des partenaires industriels"
            ]
        },
        {
            "annee": "2021 – 2023",
            "diplome": "DEUST en Mathématiques, Informatique et Physique",
            "etablissement": "Faculté des Sciences et Techniques, Errachidia",
            "details": [
                "Algorithmes, programmation, algèbre linéaire, analyse mathématique, statistiques"
            ]
        }
    ],
    
    "competences_techniques": {
        "expert": ["Python", "NumPy", "Pandas", "Matplotlib", "TensorFlow", "Keras", "SQL", "Scikit-learn"],
        "avance": ["Java", "Talend", "Power BI", "Git", "FastAPI", "Crewai", "LangChain", "LangGraph"],
        "intermediaire": ["BERT", "GPT", "NLTK", "spaCy", "Transformer models", "fine-tuning"]
    },
    
    "projets_professionnels": [
        {
            "annee": "2025",
            "titre": "Assistant IA basé sur un LLM (RAG)",
            "details": [
                "Pipeline RAG avec Ollama",
                "Prétraitement et génération d'embeddings",
                "API REST avec FastAPI pour QA contextuelle"
            ]
        },
        {
            "annee": "2024",
            "titre": "Segmentation des clients pour e-commerce",
            "details": [
                "Clustering avec DBSCAN, K-means",
                "Encodage de variables catégorielles",
                "Évaluation par Silhouette Score et Indice de Davies-Bouldin"
            ]
        }
    ],
    
    "experience": [
        {
            "company": "CYGNN GROUP",
            "position": "AI Engineer specialising in multi-agents systems",
            "period": "2025 - Present",
            "description": "Développement d'un système multi-agent avancé pour le contrôle dynamique d'une interface web intelligente."
        },
        {
            "company": "SMART AUTOMATION TECHNOLOGIES",
            "position": "AI Engineer",
            "period": "2024",
            "description": "Conception d'un assistant conversationnel multi-agent pour améliorer la fidélisation client."
        }
    ],
    
    "langues": {
        "francais": "B2",
        "anglais": "B1"
    },
    
    "soft_skills": ["Leadership", "Résolution de problèmes", "Gestion de projet"]
}

def get_portfolio_context():
    """Retourne le contexte du portfolio optimisé pour Vercel"""
    context = f"""
    Informations sur Abdelilah Ourti - AI Engineer:
    
    Nom: {PORTFOLIO_DATA['personal_info']['name']}
    Titre: {PORTFOLIO_DATA['personal_info']['title']}
    Spécialisation: {PORTFOLIO_DATA['personal_info']['specialization']}
    Formation: {PORTFOLIO_DATA['personal_info']['education']}
    Expérience: {PORTFOLIO_DATA['personal_info']['experience_years']}
    Projets: {PORTFOLIO_DATA['personal_info']['projects_completed']} réalisés
    Clients: {PORTFOLIO_DATA['personal_info']['happy_clients']} clients satisfaits
    Localisation: {PORTFOLIO_DATA['personal_info']['location']}
    Adresse: {PORTFOLIO_DATA['personal_info']['address']}
    Email: {PORTFOLIO_DATA['personal_info']['email']}
    Téléphone: {PORTFOLIO_DATA['personal_info']['phone']}
    GitHub: {PORTFOLIO_DATA['personal_info']['github']}
    Kaggle: {PORTFOLIO_DATA['personal_info']['kaggle']}
    
    Formation:
    """
    
    for formation in PORTFOLIO_DATA['formation']:
        context += f"\n- {formation['diplome']} ({formation['annee']})"
        context += f"\n  Établissement: {formation['etablissement']}"
        for detail in formation['details']:
            context += f"\n  • {detail}"
    
    context += "\n\nCompétences techniques par niveau:"
    context += f"\n- Expert: {', '.join(PORTFOLIO_DATA['competences_techniques']['expert'])}"
    context += f"\n- Avancé: {', '.join(PORTFOLIO_DATA['competences_techniques']['avance'])}"
    context += f"\n- Intermédiaire: {', '.join(PORTFOLIO_DATA['competences_techniques']['intermediaire'])}"
    
    context += "\n\nLangues:"
    for langue, niveau in PORTFOLIO_DATA['langues'].items():
        context += f"\n- {langue.capitalize()}: {niveau}"
    
    context += f"\n\nSoft Skills: {', '.join(PORTFOLIO_DATA['soft_skills'])}"
    
    context += "\n\nExpérience professionnelle:"
    for exp in PORTFOLIO_DATA['experience']:
        context += f"\n- {exp['position']} chez {exp['company']} ({exp['period']}): {exp['description']}"
    
    context += "\n\nProjets professionnels récents:"
    for projet in PORTFOLIO_DATA['projets_professionnels']:
        context += f"\n- {projet['titre']} ({projet['annee']}):"
        for detail in projet['details']:
            context += f"\n  • {detail}"
    
    return context 