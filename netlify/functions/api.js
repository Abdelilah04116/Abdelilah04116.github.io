// Vraie IA intelligente avec Gemini
async function generateResponse(question) {
  try {
    console.log(`🤖 Question reçue: ${question}`);
    
    const apiKey = process.env.GOOGLE_API_KEY;
    if (!apiKey) {
      console.log('⚠️ Clé API non configurée, utilisation du mode fallback');
      return "Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets et mon expérience. Que souhaitez-vous savoir ?";
    }
    
    // Contexte complet avec vos vraies informations
    const context = `
    Tu es l'assistant IA d'Abdelilah Ourti. Voici mes informations complètes :
    
    INFORMATIONS PERSONNELLES :
    - Nom complet : Abdelilah Ourti
    - Téléphone : +33 6 XX XX XX XX (remplacez par votre vrai numéro)
    - Email : abdellah.ourti@email.com (remplacez par votre vrai email)
    - Localisation : France
    - Nationalité : Marocaine
    
    FORMATION :
    - Master en IA et Deep Learning
    - Spécialisation en Computer Vision et Machine Learning
    - Formations certifiées en développement IA
    
    COMPÉTENCES TECHNIQUES :
    - Langages : Python, JavaScript, Java, C++
    - IA/ML : TensorFlow, PyTorch, Scikit-learn, OpenCV
    - Cloud : AWS, Docker, Kubernetes, CI/CD
    - Web : React, Node.js, Flask, Django
    - Bases de données : MySQL, MongoDB, PostgreSQL
    
    PROJETS RÉALISÉS :
    1. Système de Reconnaissance de Fleurs en temps réel
       - Technologies : Python, OpenCV, TensorFlow
       - Fonctionnalités : Détection, classification, interface web
    
    2. Analyse de Sentiments avec NLP
       - Technologies : Python, NLTK, Transformers
       - Applications : Analyse de commentaires, feedback
    
    3. Chatbot ENIAD intelligent
       - Technologies : Python, LangChain, RAG
       - Fonctionnalités : Réponses contextuelles, apprentissage
    
    4. Applications Computer Vision industrielles
       - Technologies : OpenCV, PyTorch, AWS
       - Applications : Contrôle qualité, détection d'objets
    
    EXPÉRIENCE PROFESSIONNELLE :
    - Développeur IA freelance (2023-présent)
      * Projets Computer Vision pour entreprises
      * Systèmes de reconnaissance d'images
      * Développement d'applications IA
    
    - Projets académiques et personnels
      * Recherche en Deep Learning
      * Publications et contributions open source
    
    CONTACT ET RÉSEAUX :
    - LinkedIn : Abdelilah Ourti
    - GitHub : Abdelilah04116
    - Portfolio : https://abdelilah-ourti.netlify.app
    - Disponible pour : Collaborations, projets, opportunités
    
    INSTRUCTIONS :
    - Réponds de manière naturelle et professionnelle en français
    - Donne des détails précis sur mes compétences et projets
    - Si on demande mes coordonnées, fournis-les
    - Parle de mon expérience de manière détaillée
    - Sois toujours utile et précis
    - Utilise un ton professionnel mais accessible
    - Comprends le contexte de la question et réponds intelligemment
    `;
    
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: `${context}\n\nQuestion de l'utilisateur: ${question}\n\nRéponse intelligente:`
          }]
        }]
      })
    });
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error(`Erreur API: ${response.status} - ${errorText}`);
      throw new Error(`Erreur API: ${response.status}`);
    }
    
    const data = await response.json();
    const answer = data.candidates[0].content.parts[0].text;
    
    console.log(`✅ Réponse générée: ${answer.substring(0, 100)}...`);
    return answer;
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return "Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets et mon expérience. Que souhaitez-vous savoir ?";
  }
}

exports.handler = async (event, context) => {
  // CORS headers
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
  };

  // Handle preflight requests
  if (event.httpMethod === 'OPTIONS') {
    console.log('✅ OPTIONS request traitée');
    return {
      statusCode: 200,
      headers,
      body: ''
    };
  }

  // Handle POST requests
  if (event.httpMethod === 'POST') {
    try {
      console.log(`🚀 Handler appelé avec méthode: ${event.httpMethod}`);
      console.log(`📝 Body: ${event.body}`);
      
      const data = JSON.parse(event.body);
      const message = data.message;
      
      if (!message) {
        console.log('❌ Aucun message fourni');
        return {
          statusCode: 400,
          headers,
          body: JSON.stringify({ error: 'Aucun message fourni' })
        };
      }
      
      console.log(`📨 Message reçu: ${message}`);
      
      const response_text = await generateResponse(message);
      
      console.log(`📤 Réponse envoyée`);
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ response: response_text })
      };
      
    } catch (error) {
      console.error(`❌ Erreur dans le handler: ${error.message}`);
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ error: error.message })
      };
    }
  }

  // Handle other methods
  console.log(`❌ Méthode non autorisée: ${event.httpMethod}`);
  return {
    statusCode: 405,
    headers,
    body: JSON.stringify({ error: 'Méthode non autorisée' })
  };
}; 