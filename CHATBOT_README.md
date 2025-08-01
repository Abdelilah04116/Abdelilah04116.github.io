# 🤖 Chatbot Portfolio - Abdelilah Ourti

## 📋 Description

Ce chatbot IA est intégré au portfolio d'Abdelilah Ourti et permet aux visiteurs de poser des questions sur son profil, ses compétences, ses projets et son expérience professionnelle.

## 🚀 Fonctionnalités

- **Interface intuitive** : Bouton de chat flottant sur le portfolio
- **Réponses intelligentes** : Basées sur les données structurées du portfolio
- **Support multilingue** : Réponses en français et anglais
- **Contexte enrichi** : Utilise toutes les informations du portfolio
- **API REST** : Endpoint `/api/chat` pour les requêtes

## 🏗️ Architecture

### Fichiers principaux :
- `portfolio_data.py` : Données structurées du portfolio
- `chatbot/chatbot_logic.py` : Logique du chatbot avec Google Gemini
- `web/api.py` : API Flask pour le chatbot
- `index.html` : Interface utilisateur intégrée

### Technologies utilisées :
- **Google Gemini 2.0 Flash** : Modèle de langage
- **LangChain** : Framework pour les applications IA
- **FAISS** : Base de données vectorielle
- **Flask** : API REST
- **Vue.js** : Interface utilisateur

## 🔧 Configuration

### Variables d'environnement :
```bash
GOOGLE_API_KEY=AIzaSyAE_7Y0cA46UZxXa2vxToKkJcTBi8m97Rs
```

### Installation des dépendances :
```bash
pip install -r requirements.txt
```

## 🧪 Test du chatbot

Pour tester le chatbot localement :

```bash
python test_chatbot.py
```

## 📡 API Endpoints

### POST `/api/chat`
Envoie une question au chatbot et reçoit une réponse.

**Request :**
```json
{
  "message": "Quelles sont les compétences d'Abdelilah ?"
}
```

**Response :**
```json
{
  "response": "Abdelilah Ourti maîtrise plusieurs technologies..."
}
```

## 💬 Exemples de questions

Le chatbot peut répondre à des questions comme :

- "Quel est le nom complet d'Abdelilah ?"
- "Quelles sont ses compétences en programmation ?"
- "Parle-moi de ses projets principaux"
- "Quelle est son expérience professionnelle ?"
- "Quels sont les témoignages sur son travail ?"
- "Quelles technologies maîtrise-t-il ?"
- "Où a-t-il étudié ?"
- "Combien de projets a-t-il réalisés ?"

## 🎯 Données indexées

Le chatbot a accès à toutes les informations du portfolio :

- **Informations personnelles** : Nom, titre, formation, expérience
- **Compétences** : Langages de programmation, frameworks, outils
- **Projets** : Descriptions, technologies utilisées, liens GitHub
- **Expérience professionnelle** : Postes, entreprises, périodes
- **Témoignages** : Avis de collègues, professeurs, managers
- **Contact** : Email, téléphone, réseaux sociaux

## 🚀 Déploiement

Le chatbot est automatiquement déployé avec le portfolio sur Render :

1. **Build Command** : `pip install -r requirements.txt`
2. **Start Command** : `gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`
3. **Variables d'environnement** : `GOOGLE_API_KEY` configurée

## 🔒 Sécurité

- La clé API Google est stockée dans les variables d'environnement
- Validation des entrées utilisateur
- Gestion des erreurs robuste
- Limitation des requêtes (timeout 120s)

## 📱 Interface utilisateur

Le chatbot apparaît comme un bouton flottant en bas à droite du portfolio. L'interface inclut :

- **Bouton toggle** : Ouvre/ferme le chat
- **Zone de messages** : Historique des conversations
- **Indicateur de frappe** : "L'assistant écrit..."
- **Zone de saisie** : Pour poser des questions
- **Bouton d'envoi** : Envoie la question

## 🎨 Personnalisation

Le style du chatbot peut être modifié dans le CSS de `index.html` :

```css
#chatbot-toggle {
  /* Style du bouton flottant */
}

#chatbot-container {
  /* Style du conteneur principal */
}

.chat-message {
  /* Style des messages */
}
```

## 📞 Support

Pour toute question ou problème avec le chatbot, contactez Abdelilah Ourti :
- Email : abdelilahourti@gmail.com
- GitHub : https://github.com/Abdelilah04116 