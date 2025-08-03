import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Ajouter le répertoire parent au chemin pour importer portfolio_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio_data import get_portfolio_context

load_dotenv()

class PortfolioChatbotSimple:
    def __init__(self, google_api_key=None):
        self.api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
        self.portfolio_context = get_portfolio_context()
        self._setup_gemini()

    def _setup_gemini(self):
        """Configure l'API Gemini"""
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
            print("[INFO] Gemini model configured successfully")
        except Exception as e:
            print(f"[ERROR] Failed to configure Gemini: {e}")
            self.model = None

    def get_answer(self, query: str):
        """Génère une réponse en utilisant directement Gemini"""
        
        if self.model is None:
            return "Désolé, le service n'est pas disponible pour le moment.", []

        # Créer un prompt enrichi avec le contexte du portfolio
        enhanced_query = f"""
        Tu es l'assistant IA d'Abdelilah Ourti, un ingénieur en IA spécialisé en Deep Learning, Computer Vision et Machine Learning.

        Contexte du portfolio d'Abdelilah Ourti:
        {self.portfolio_context}
        
        Question de l'utilisateur: {query}
        
        Instructions:
        1. Réponds de manière professionnelle et détaillée en te basant sur les informations du portfolio d'Abdelilah Ourti
        2. Si la question concerne des informations qui ne sont pas dans le portfolio, dis-le poliment
        3. Réponds en français sauf si l'utilisateur pose la question en anglais
        4. Sois concis mais informatif
        5. Utilise un ton professionnel et amical
        """
        
        try:
            response = self.model.generate_content(enhanced_query)
            return response.text, []
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {e}")
            return "Désolé, je n'ai pas pu traiter votre demande pour le moment. Pouvez-vous reformuler votre question ?", []

    def reset_conversation(self):
        """Réinitialise la conversation (non nécessaire avec cette implémentation)"""
        pass

    def update_knowledge_base(self) -> bool:
        """Met à jour la base de connaissances (non nécessaire avec cette implémentation)"""
        return True 