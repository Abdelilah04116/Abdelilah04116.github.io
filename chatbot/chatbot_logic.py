import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from chatbot.rag_pipeline import RAGPipeline
import sys

# Ajouter le répertoire parent au chemin pour importer portfolio_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from portfolio_data import get_portfolio_context

load_dotenv()

class PortfolioChatbot:
    def __init__(self, google_api_key=None):
        self.api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
        self.vectorstore_path = "chatbot/vectorstore"
        self.portfolio_context = get_portfolio_context()
        self._load_vectorstore()

    def _load_vectorstore(self):
        try:
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=self.api_key
            )

            index_path = os.path.join(self.vectorstore_path, "index.faiss")

            # Vérifie si l'index existe
            if os.path.exists(index_path):
                print("[INFO] FAISS index found. Loading it...")
                self.vectorstore = FAISS.load_local(
                    self.vectorstore_path,
                    embeddings,
                    allow_dangerous_deserialization=True
                )
            else:
                print("[WARNING] FAISS index not found. Rebuilding the vectorstore...")
                pipeline = RAGPipeline(google_api_key=self.api_key)
                pipeline.build_vectorstore()

                # Recharge après génération
                if os.path.exists(index_path):
                    self.vectorstore = FAISS.load_local(
                        self.vectorstore_path,
                        embeddings,
                        allow_dangerous_deserialization=True
                    )
                else:
                    print("[ERROR] Failed to create FAISS index. Using fallback mode.")
                    # Mode fallback sans vectorstore
                    self.vectorstore = None
                    return
        except Exception as e:
            print(f"[ERROR] Error loading vectorstore: {e}")
            self.vectorstore = None
            return

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=self.api_key,
            temperature=0.3
        )

        # Initialiser la chaîne QA seulement si le vectorstore est disponible
        if self.vectorstore is not None:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                retriever=self.vectorstore.as_retriever()
            )
        else:
            self.qa_chain = None

    def get_answer(self, query: str):
        # Créer un prompt enrichi avec le contexte du portfolio
        enhanced_query = f"""
        Contexte du portfolio d'Abdelilah Ourti:
        {self.portfolio_context}
        
        Question de l'utilisateur: {query}
        
        Réponds de manière professionnelle et détaillée en te basant sur les informations du portfolio d'Abdelilah Ourti. 
        Si la question concerne des informations qui ne sont pas dans le portfolio, dis-le poliment.
        Réponds en français sauf si l'utilisateur pose la question en anglais.
        """
        
        try:
            # Vérifier si la chaîne QA est disponible
            if self.qa_chain is not None:
                result = self.qa_chain({"query": enhanced_query})
                return result["result"], []
            else:
                # Mode fallback : utiliser directement le LLM
                print("[INFO] Using fallback mode without vectorstore")
                response = self.llm.invoke(enhanced_query)
                return response.content, []
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {e}")
            return "Désolé, je n'ai pas pu traiter votre demande pour le moment. Pouvez-vous reformuler votre question ?", []

    def reset_conversation(self):
        # Aucun historique à gérer pour Gemini dans cette config
        pass

    def update_knowledge_base(self) -> bool:
        pipeline = RAGPipeline(google_api_key=self.api_key)
        return pipeline.build_vectorstore()
