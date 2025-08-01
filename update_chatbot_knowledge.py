#!/usr/bin/env python3
"""
Script pour mettre à jour la base de connaissances du chatbot
avec les nouvelles données du portfolio
"""

import os
import sys
from pathlib import Path

# Ajouter le répertoire chatbot au path
sys.path.append(str(Path(__file__).parent / "chatbot"))

from rag_pipeline import RAGPipeline

def update_chatbot_knowledge():
    """Met à jour la base de connaissances du chatbot"""
    
    print("🔄 Mise à jour de la base de connaissances du chatbot...")
    
    try:
        # Initialiser le pipeline RAG
        rag_pipeline = RAGPipeline()
        
        # Reconstruire le vectorstore avec les nouvelles données
        success = rag_pipeline.build_vectorstore()
        
        if success:
            print("✅ Base de connaissances mise à jour avec succès!")
            print("📚 Les nouvelles données incluent:")
            print("   - Formation académique détaillée")
            print("   - Projets professionnels récents")
            print("   - Compétences techniques par niveau")
            print("   - Expérience professionnelle complète")
            print("   - Témoignages et références")
            print("   - Informations de contact et liens")
        else:
            print("❌ Erreur lors de la mise à jour de la base de connaissances")
            return False
            
    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    update_chatbot_knowledge() 