#!/usr/bin/env python3
"""
Script de test pour vérifier la configuration Vercel
"""

import os
import sys
from pathlib import Path

def test_vercel_config():
    """Test de la configuration Vercel"""
    
    print("🧪 Test de la configuration Vercel...")
    
    # Vérifier les fichiers requis
    required_files = [
        "vercel.json",
        "requirements-vercel.txt",
        "api/chat.py",
        "api/__init__.py",
        "index.html",
        "portfolio_data.py",
        "chatbot/chatbot_logic.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Fichiers manquants: {missing_files}")
        return False
    
    print("✅ Tous les fichiers requis sont présents")
    
    # Vérifier vercel.json
    try:
        import json
        with open("vercel.json", "r") as f:
            config = json.load(f)
        
        required_keys = ["version", "builds", "routes"]
        for key in required_keys:
            if key not in config:
                print(f"❌ Clé manquante dans vercel.json: {key}")
                return False
        
        print("✅ Configuration vercel.json valide")
        
    except Exception as e:
        print(f"❌ Erreur dans vercel.json: {e}")
        return False
    
    # Vérifier requirements-vercel.txt
    try:
        with open("requirements-vercel.txt", "r") as f:
            requirements = f.read()
        
        essential_packages = [
            "Flask",
            "langchain",
            "google-generativeai",
            "faiss-cpu"
        ]
        
        for package in essential_packages:
            if package not in requirements:
                print(f"❌ Package manquant: {package}")
                return False
        
        print("✅ Requirements Vercel valides")
        
    except Exception as e:
        print(f"❌ Erreur dans requirements-vercel.txt: {e}")
        return False
    
    # Vérifier l'API endpoint
    try:
        with open("api/chat.py", "r") as f:
            api_code = f.read()
        
        required_elements = [
            "from flask import",
            "@app.route('/api/chat'",
            "chatbot.generate_response"
        ]
        
        for element in required_elements:
            if element not in api_code:
                print(f"❌ Élément manquant dans api/chat.py: {element}")
                return False
        
        print("✅ API endpoint configuré correctement")
        
    except Exception as e:
        print(f"❌ Erreur dans api/chat.py: {e}")
        return False
    
    # Vérifier les variables d'environnement
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("⚠️  Variable d'environnement GOOGLE_API_KEY non trouvée")
        print("   Assurez-vous de la configurer dans Vercel")
    else:
        print("✅ Variable d'environnement GOOGLE_API_KEY trouvée")
    
    print("\n🎉 Configuration Vercel prête pour le déploiement!")
    print("\n📋 Prochaines étapes:")
    print("1. Poussez votre code vers GitHub")
    print("2. Connectez votre repo à Vercel")
    print("3. Configurez la variable GOOGLE_API_KEY dans Vercel")
    print("4. Déployez!")
    
    return True

def test_local_api():
    """Test local de l'API (optionnel)"""
    
    print("\n🔧 Test local de l'API...")
    
    try:
        # Test d'import
        sys.path.append(str(Path(__file__).parent))
        from api.chat import app
        
        print("✅ API Flask importée avec succès")
        
        # Test de création du client
        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/api/health')
            if response.status_code == 200:
                print("✅ Health endpoint fonctionne")
            else:
                print(f"❌ Health endpoint erreur: {response.status_code}")
        
    except Exception as e:
        print(f"⚠️  Test local échoué: {e}")
        print("   Cela peut être normal si les dépendances ne sont pas installées")

if __name__ == "__main__":
    success = test_vercel_config()
    
    if success:
        # Test local optionnel
        try:
            test_local_api()
        except:
            pass
        
        print("\n🚀 Prêt pour le déploiement Vercel!")
    else:
        print("\n❌ Veuillez corriger les erreurs avant le déploiement")
        sys.exit(1) 