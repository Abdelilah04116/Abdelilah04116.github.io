#!/usr/bin/env python3
"""
Test du chatbot portfolio
"""

import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from portfolio_data import get_portfolio_context
from chatbot.chatbot_logic import PortfolioChatbot

def test_chatbot():
    """Test du chatbot avec quelques questions"""
    
    # Charger les variables d'environnement
    load_dotenv()
    
    # Vérifier la clé API
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ Erreur: GOOGLE_API_KEY non trouvée dans les variables d'environnement")
        return
    
    print("✅ Clé API Google trouvée")
    
    try:
        # Initialiser le chatbot
        print("🔄 Initialisation du chatbot...")
        chatbot = PortfolioChatbot(google_api_key=api_key)
        print("✅ Chatbot initialisé avec succès")
        
        # Questions de test
        test_questions = [
            "Quel est le nom complet d'Abdelilah ?",
            "Quelles sont ses compétences en programmation ?",
            "Parle-moi de ses projets principaux",
            "Quelle est son expérience professionnelle ?",
            "Quels sont les témoignages sur son travail ?"
        ]
        
        print("\n🧪 Tests du chatbot:")
        print("=" * 50)
        
        for i, question in enumerate(test_questions, 1):
            print(f"\n❓ Question {i}: {question}")
            try:
                response, _ = chatbot.get_answer(question)
                print(f"🤖 Réponse: {response}")
            except Exception as e:
                print(f"❌ Erreur: {e}")
            
            print("-" * 30)
        
        print("\n✅ Tests terminés !")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation: {e}")

if __name__ == "__main__":
    test_chatbot() 