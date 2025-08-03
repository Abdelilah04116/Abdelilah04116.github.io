#!/usr/bin/env node
/**
 * Script de test pour l'API Netlify
 */

const { GoogleGenerativeAI } = require('@google/generative-ai');

// Configuration Gemini
const genAI = new GoogleGenerativeAI('AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y');

// Contexte du portfolio
const PORTFOLIO_CONTEXT = `
Abdelilah Ourti - Ingénieur en IA
Formation: Master en IA et Deep Learning
Compétences: Python, TensorFlow, PyTorch, OpenCV, AWS, Docker
Projets: Reconnaissance de Fleurs, Analyse de Sentiments, Chatbot ENIAD
Expérience: Développeur IA, projets freelance Computer Vision
Contact: LinkedIn Abdelilah Ourti, GitHub Abdelilah04116
`;

async function testAPI() {
  console.log('🧪 Test de l\'API Netlify');
  console.log('=' * 50);
  
  try {
    console.log('✅ Configuration Gemini...');
    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash-exp" });
    
    const testQuestion = "Qui es-tu ?";
    console.log(`📝 Question de test: ${testQuestion}`);
    
    const prompt = `
    Tu es l'assistant IA d'Abdelilah Ourti, ingénieur en IA.
    
    Contexte: ${PORTFOLIO_CONTEXT}
    
    Question: ${testQuestion}
    
    Réponds de manière professionnelle en français, sauf si la question est en anglais.
    `;
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    
    console.log(`🤖 Réponse: ${text.substring(0, 100)}...`);
    console.log('✅ Test réussi!');
    
    return true;
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return false;
  }
}

async function testFunction() {
  console.log('\n🧪 Test de la fonction Netlify');
  console.log('=' * 50);
  
  try {
    // Simuler l'événement Netlify
    const event = {
      httpMethod: 'POST',
      body: JSON.stringify({ message: 'Qui es-tu ?' })
    };
    
    const context = {};
    
    // Importer et tester la fonction
    const { handler } = require('./netlify/functions/api.js');
    const result = await handler(event, context);
    
    console.log(`✅ Status: ${result.statusCode}`);
    console.log(`📤 Réponse: ${result.body.substring(0, 100)}...`);
    
    return result.statusCode === 200;
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return false;
  }
}

async function main() {
  console.log('🚀 Test de Déploiement Netlify');
  console.log('=' * 50);
  
  // Test de l'API Gemini
  const success1 = await testAPI();
  
  // Test de la fonction Netlify
  const success2 = await testFunction();
  
  console.log('\n' + '=' * 50);
  console.log('📊 Résultats:');
  console.log(`API Gemini: ${success1 ? '✅' : '❌'}`);
  console.log(`Fonction Netlify: ${success2 ? '✅' : '❌'}`);
  
  if (success1 && success2) {
    console.log('\n🎉 Tous les tests réussis!');
    console.log('📋 Prêt pour le déploiement Netlify');
  } else {
    console.log('\n⚠️ Problèmes détectés');
  }
  
  console.log('\n📋 Prochaines étapes:');
  console.log('1. Poussez le code sur GitHub');
  console.log('2. Connectez votre repo à Netlify');
  console.log('3. Configurez la variable GOOGLE_API_KEY');
  console.log('4. Déployez!');
}

if (require.main === module) {
  main().catch(console.error);
} 