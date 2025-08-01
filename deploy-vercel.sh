#!/bin/bash

# Script de déploiement Vercel pour le portfolio avec chatbot
echo "🚀 Déploiement Vercel - Portfolio avec Chatbot"
echo "=============================================="

# Vérifier si Vercel CLI est installé
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI n'est pas installé"
    echo "📦 Installation de Vercel CLI..."
    npm install -g vercel
fi

# Vérifier la configuration
echo "🧪 Test de la configuration..."
python test-vercel-deployment.py

if [ $? -ne 0 ]; then
    echo "❌ Configuration invalide. Veuillez corriger les erreurs."
    exit 1
fi

# Vérifier si on est connecté à Vercel
echo "🔐 Vérification de la connexion Vercel..."
vercel whoami &> /dev/null

if [ $? -ne 0 ]; then
    echo "🔑 Connexion à Vercel..."
    vercel login
fi

# Déploiement
echo "🚀 Déploiement en cours..."
vercel --prod

echo "✅ Déploiement terminé!"
echo ""
echo "📋 URLs de votre projet:"
echo "   - Production: https://votre-projet.vercel.app"
echo "   - API: https://votre-projet.vercel.app/api/chat"
echo ""
echo "🔧 Pour vérifier le déploiement:"
echo "   curl https://votre-projet.vercel.app/api/health"
echo ""
echo "📊 Dashboard: https://vercel.com/dashboard" 