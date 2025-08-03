#!/usr/bin/env node
/**
 * Debug de l'API Gemini
 */

async function debugAPI() {
  console.log('🔍 Debug de l\'API Gemini');
  console.log('=' * 50);
  
  // Test 1 : Vérifier la variable d'environnement
  console.log('📋 Test 1 : Variable d\'environnement');
  console.log('GOOGLE_API_KEY:', process.env.GOOGLE_API_KEY ? '✅ Configurée' : '❌ Non configurée');
  
  if (process.env.GOOGLE_API_KEY) {
    console.log('Longueur de la clé:', process.env.GOOGLE_API_KEY.length);
    console.log('Début de la clé:', process.env.GOOGLE_API_KEY.substring(0, 10) + '...');
  }
  
  // Test 2 : Test direct de l'API
  console.log('\n📋 Test 2 : Test direct de l\'API');
  
  if (!process.env.GOOGLE_API_KEY) {
    console.log('❌ Pas de clé API, test impossible');
    return;
  }
  
  try {
    console.log('🔄 Test de l\'API Gemini...');
    
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${process.env.GOOGLE_API_KEY}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: 'Dis-moi bonjour en français'
          }]
        }]
      })
    });
    
    console.log('📊 Status:', response.status);
    console.log('📊 OK:', response.ok);
    
    if (response.ok) {
      const data = await response.json();
      console.log('✅ API fonctionnelle !');
      console.log('Réponse:', data.candidates[0].content.parts[0].text);
    } else {
      const errorText = await response.text();
      console.log('❌ Erreur API:', errorText);
    }
    
  } catch (error) {
    console.log('❌ Erreur:', error.message);
  }
  
  // Test 3 : Test de la fonction complète
  console.log('\n📋 Test 3 : Test de la fonction complète');
  
  const event = {
    httpMethod: 'POST',
    body: JSON.stringify({ message: 'Quel est ton numéro de téléphone ?' })
  };
  
  try {
    const { handler } = require('./netlify/functions/api.js');
    const result = await handler(event, {});
    
    console.log('📊 Status:', result.statusCode);
    console.log('📊 Body:', result.body.substring(0, 200) + '...');
    
    if (result.statusCode === 200) {
      const response = JSON.parse(result.body);
      console.log('📝 Réponse complète:', response.response);
    }
    
  } catch (error) {
    console.log('❌ Erreur fonction:', error.message);
  }
}

async function testCléAPI() {
  console.log('\n🔑 Test de la Clé API');
  console.log('=' * 50);
  
  // Test avec une clé de test (à remplacer par votre vraie clé)
  const testKey = 'AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y';
  
  console.log('🔄 Test avec la clé fournie...');
  
  try {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${testKey}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: 'Dis-moi bonjour'
          }]
        }]
      })
    });
    
    console.log('📊 Status:', response.status);
    
    if (response.ok) {
      const data = await response.json();
      console.log('✅ Clé de test fonctionnelle !');
      console.log('Réponse:', data.candidates[0].content.parts[0].text);
    } else {
      const errorText = await response.text();
      console.log('❌ Erreur avec la clé de test:', errorText);
    }
    
  } catch (error) {
    console.log('❌ Erreur:', error.message);
  }
}

async function main() {
  await debugAPI();
  await testCléAPI();
  
  console.log('\n' + '=' * 50);
  console.log('📋 Diagnostic :');
  console.log('1. Si la clé API n\'est pas configurée → Configurez-la dans Netlify');
  console.log('2. Si la clé API est invalide → Créez une nouvelle clé sur Google AI Studio');
  console.log('3. Si l\'API fonctionne mais pas la fonction → Problème dans le code');
  console.log('4. Si rien ne fonctionne → Problème de réseau ou de configuration');
  
  console.log('\n🔧 Solutions :');
  console.log('1. Allez sur https://makersuite.google.com/app/apikey');
  console.log('2. Créez une nouvelle clé API');
  console.log('3. Configurez-la dans Netlify (Site settings > Environment variables)');
  console.log('4. Redéployez le site');
}

if (require.main === module) {
  main().catch(console.error);
} 