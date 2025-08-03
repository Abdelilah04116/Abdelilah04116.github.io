// Système de réponses intelligentes et gratuites
async function generateResponse(question) {
  try {
    console.log(`🤖 Génération de réponse pour: ${question}`);
    
    const lowerQuestion = question.toLowerCase();
    
    // Système de réponses intelligentes pré-définies
    if (lowerQuestion.includes('qui es-tu') || lowerQuestion.includes('présente') || lowerQuestion.includes('qui êtes-vous')) {
      return "Je suis l'assistant IA d'Abdelilah Ourti, ingénieur en IA passionné par le Deep Learning et la Computer Vision. Je peux vous parler de mes projets, compétences et expériences. Que souhaitez-vous savoir ?";
    }
    
    if (lowerQuestion.includes('compétence') || lowerQuestion.includes('skill') || lowerQuestion.includes('technologie')) {
      return "Mes compétences principales incluent : Python, TensorFlow, PyTorch, OpenCV, AWS, Docker, Machine Learning, Deep Learning, Computer Vision, et le développement d'applications IA. Je suis également familier avec les frameworks web et les bases de données.";
    }
    
    if (lowerQuestion.includes('projet') || lowerQuestion.includes('travail') || lowerQuestion.includes('réalisation')) {
      return "J'ai développé plusieurs projets passionnants : 1) Système de Reconnaissance de Fleurs en temps réel, 2) Analyse de Sentiments avec NLP, 3) Chatbot ENIAD intelligent, 4) Applications Computer Vision pour l'industrie. Chaque projet démontre mes compétences en IA et développement.";
    }
    
    if (lowerQuestion.includes('formation') || lowerQuestion.includes('étude') || lowerQuestion.includes('diplôme')) {
      return "J'ai un Master en IA et Deep Learning, avec une formation solide en mathématiques, algorithmes et développement. J'ai également suivi des formations spécialisées en Computer Vision et Machine Learning.";
    }
    
    if (lowerQuestion.includes('contact') || lowerQuestion.includes('joindre') || lowerQuestion.includes('email')) {
      return "Vous pouvez me contacter via LinkedIn (Abdelilah Ourti) ou GitHub (Abdelilah04116). Je suis toujours ouvert aux opportunités de collaboration et aux projets intéressants en IA.";
    }
    
    if (lowerQuestion.includes('expérience') || lowerQuestion.includes('travail') || lowerQuestion.includes('emploi')) {
      return "J'ai travaillé comme développeur IA sur divers projets, incluant des applications Computer Vision, des systèmes de reconnaissance d'images, et des chatbots intelligents. J'ai également une expérience en freelance sur des projets innovants.";
    }
    
    if (lowerQuestion.includes('cv') || lowerQuestion.includes('curriculum') || lowerQuestion.includes('résumé')) {
      return "Je suis Abdelilah Ourti, ingénieur en IA avec un Master en Deep Learning. Spécialisé en Computer Vision, Machine Learning et développement d'applications intelligentes. Expérience en projets freelance et développement d'outils IA innovants.";
    }
    
    if (lowerQuestion.includes('github') || lowerQuestion.includes('portfolio') || lowerQuestion.includes('code')) {
      return "Vous pouvez voir mes projets sur GitHub (Abdelilah04116) où je partage mes travaux en IA, Computer Vision et Machine Learning. Mon portfolio présente mes réalisations et compétences techniques.";
    }
    
    if (lowerQuestion.includes('linkedin') || lowerQuestion.includes('réseau') || lowerQuestion.includes('professionnel')) {
      return "Mon profil LinkedIn (Abdelilah Ourti) présente mon parcours professionnel, mes compétences en IA et mes projets. N'hésitez pas à me contacter pour des opportunités de collaboration.";
    }
    
    // Réponse par défaut intelligente
    return "Je suis l'assistant IA d'Abdelilah Ourti. Je peux vous parler de mes compétences en IA, mes projets, ma formation ou mon expérience. Que souhaitez-vous savoir spécifiquement ?";
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return "Je suis l'assistant IA d'Abdelilah Ourti. Je suis actuellement en maintenance, mais je peux vous dire que je suis ingénieur en IA spécialisé en Deep Learning, Computer Vision et développement d'applications intelligentes.";
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