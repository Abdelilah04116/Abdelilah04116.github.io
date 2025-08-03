// Contexte du portfolio
const PORTFOLIO_CONTEXT = `
Abdelilah Ourti - Ingénieur en IA
Formation: Master en IA et Deep Learning
Compétences: Python, TensorFlow, PyTorch, OpenCV, AWS, Docker
Projets: Reconnaissance de Fleurs, Analyse de Sentiments, Chatbot ENIAD
Expérience: Développeur IA, projets freelance Computer Vision
Contact: LinkedIn Abdelilah Ourti, GitHub Abdelilah04116
`;

async function generateResponse(question) {
  try {
    console.log(`🤖 Génération de réponse pour: ${question}`);
    
    const apiKey = process.env.GOOGLE_API_KEY;
    if (!apiKey) {
      throw new Error('GOOGLE_API_KEY non configurée');
    }
    
    const prompt = `
    Tu es l'assistant IA d'Abdelilah Ourti, ingénieur en IA.
    
    Contexte: ${PORTFOLIO_CONTEXT}
    
    Question: ${question}
    
    Réponds de manière professionnelle en français, sauf si la question est en anglais.
    `;
    
    const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: prompt
          }]
        }]
      })
    });
    
    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Erreur API: ${response.status} - ${errorText}`);
    }
    
    const data = await response.json();
    const text = data.candidates[0].content.parts[0].text;
    
    console.log(`✅ Réponse générée: ${text.substring(0, 50)}...`);
    return text;
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return `Désolé, je n'ai pas pu traiter votre demande: ${error.message}`;
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