// IA intelligente avec fallback amélioré
async function generateResponse(question) {
  try {
    console.log(`🤖 Question reçue: ${question}`);
    
    const apiKey = process.env.GOOGLE_API_KEY;
    if (!apiKey) {
      console.log('⚠️ Clé API non configurée, utilisation du mode intelligent local');
      return generateIntelligentResponse(question);
    }
    
    // Essayer l'API Gemini d'abord
    try {
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
      
      if (response.ok) {
        const data = await response.json();
        const answer = data.candidates[0].content.parts[0].text;
        console.log(`✅ Réponse Gemini générée: ${answer.substring(0, 100)}...`);
        return answer;
      } else {
        throw new Error(`Erreur API: ${response.status}`);
      }
      
    } catch (apiError) {
      console.log(`⚠️ Erreur API Gemini: ${apiError.message}, utilisation du mode local`);
      return generateIntelligentResponse(question);
    }
    
  } catch (error) {
    console.error(`❌ Erreur générale: ${error.message}`);
    return generateIntelligentResponse(question);
  }
}

// Système de réponses intelligentes local (fallback)
function generateIntelligentResponse(question) {
  const lowerQuestion = question.toLowerCase().trim();
  
  // Informations personnelles
  if (lowerQuestion.includes('téléphone') || lowerQuestion.includes('numéro') || lowerQuestion.includes('phone')) {
    return "Mon numéro de téléphone est +33 6 XX XX XX XX (remplacez par votre vrai numéro). Vous pouvez également me contacter par email à abdellah.ourti@email.com ou via LinkedIn (Abdelilah Ourti).";
  }
  
  if (lowerQuestion.includes('email') || lowerQuestion.includes('mail') || lowerQuestion.includes('courriel')) {
    return "Mon adresse email est abdellah.ourti@email.com. N'hésitez pas à me contacter pour des opportunités de collaboration ou des projets intéressants en IA.";
  }
  
  if (lowerQuestion.includes('contact') || lowerQuestion.includes('joindre') || lowerQuestion.includes('contacter')) {
    return "Vous pouvez me contacter de plusieurs façons : par téléphone au +33 6 XX XX XX XX, par email à abdellah.ourti@email.com, via LinkedIn (Abdelilah Ourti) ou GitHub (Abdelilah04116). Je suis toujours ouvert aux collaborations !";
  }
  
  // Formation et expérience
  if (lowerQuestion.includes('formation') || lowerQuestion.includes('diplôme') || lowerQuestion.includes('étude') || lowerQuestion.includes('master')) {
    return "J'ai un Master en IA et Deep Learning avec une spécialisation en Computer Vision et Machine Learning. J'ai également suivi des formations certifiées en développement IA et je continue à me former sur les nouvelles technologies.";
  }
  
  if (lowerQuestion.includes('expérience') || lowerQuestion.includes('travail') || lowerQuestion.includes('emploi') || lowerQuestion.includes('carrière')) {
    return "Je travaille comme développeur IA freelance depuis 2023. J'ai développé plusieurs projets passionnants : systèmes de reconnaissance d'images, applications Computer Vision pour l'industrie, chatbots intelligents, et des outils d'analyse de sentiments. J'ai également une expérience en recherche en Deep Learning et en contributions open source.";
  }
  
  // Compétences et technologies
  if (lowerQuestion.includes('compétence') || lowerQuestion.includes('skill') || lowerQuestion.includes('savoir-faire') || lowerQuestion.includes('technologie')) {
    return "Mes compétences principales incluent Python, JavaScript, Java, C++, TensorFlow, PyTorch, OpenCV, AWS, Docker, Kubernetes, React, Node.js, Flask, Django, et bien d'autres technologies. Je suis spécialisé en Machine Learning, Deep Learning, Computer Vision et développement d'applications IA.";
  }
  
  if (lowerQuestion.includes('python') || lowerQuestion.includes('tensorflow') || lowerQuestion.includes('pytorch') || lowerQuestion.includes('opencv')) {
    return "Je maîtrise parfaitement Python, TensorFlow, PyTorch, OpenCV et bien d'autres technologies IA. Ces outils me permettent de développer des applications avancées en Computer Vision, Machine Learning et Deep Learning. J'ai utilisé ces technologies dans mes projets de reconnaissance de fleurs, d'analyse de sentiments et d'applications industrielles.";
  }
  
  // Projets
  if (lowerQuestion.includes('projet') || lowerQuestion.includes('travail') || lowerQuestion.includes('réalisation') || lowerQuestion.includes('développé')) {
    return "J'ai développé plusieurs projets passionnants : 1) Un système de reconnaissance de fleurs en temps réel avec Python et OpenCV, 2) Une analyse de sentiments avec NLP et Transformers, 3) Un chatbot ENIAD intelligent avec LangChain et RAG, 4) Des applications Computer Vision pour l'industrie. Chaque projet démontre mes compétences en IA et développement.";
  }
  
  // Localisation et informations personnelles
  if (lowerQuestion.includes('habite') || lowerQuestion.includes('où') || lowerQuestion.includes('localisation') || lowerQuestion.includes('ville')) {
    return "J'habite en France et je suis de nationalité marocaine. Je suis disponible pour des projets en remote ou sur site, et je peux me déplacer pour des opportunités intéressantes.";
  }
  
  if (lowerQuestion.includes('qui') && (lowerQuestion.includes('es-tu') || lowerQuestion.includes('êtes-vous') || lowerQuestion.includes('tu'))) {
    return "Je suis Abdelilah Ourti, ingénieur en IA passionné par le Deep Learning et la Computer Vision. J'ai un Master en IA et je travaille comme développeur freelance. Je développe des applications intelligentes et je suis toujours à la recherche de nouveaux défis technologiques.";
  }
  
  // Salutations
  if (lowerQuestion.includes('bonjour') || lowerQuestion.includes('salut') || lowerQuestion.includes('hello')) {
    return "Bonjour ! Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets, ma formation ou mon expérience. Que souhaitez-vous savoir ?";
  }
  
  // Réponse par défaut intelligente
  return "Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets, ma formation ou mon expérience. Que souhaitez-vous savoir spécifiquement ?";
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