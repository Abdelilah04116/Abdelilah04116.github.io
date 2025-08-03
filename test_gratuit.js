#!/usr/bin/env node
/**
 * Test de la solution gratuite
 */

async function testGratuit() {
  console.log('🧪 Test de la Solution Gratuite');
  console.log('=' * 50);
  
  // Simuler l'événement Netlify
  const event = {
    httpMethod: 'POST',
    body: JSON.stringify({ message: 'Qui es-tu ?' })
  };
  
  const context = {};
  
  try {
    // Importer et tester la fonction
    const { handler } = require('./netlify/functions/api.js');
    const result = await handler(event, context);
    
    console.log(`✅ Status: ${result.statusCode}`);
    console.log(`📤 Réponse: ${result.body.substring(0, 100)}...`);
    
    if (result.statusCode === 200) {
      console.log('🎉 Test réussi !');
      return true;
    } else {
      console.log('❌ Test échoué');
      return false;
    }
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return false;
  }
}

async function testQuestions() {
  console.log('\n🧪 Test de Différentes Questions');
  console.log('=' * 50);
  
  const questions = [
    'Qui es-tu ?',
    'Quelles sont tes compétences ?',
    'Parle-moi de tes projets',
    'Quelle est ta formation ?',
    'Comment te contacter ?',
    'Quelle est ton expérience ?',
    'Peux-tu me parler de ton CV ?',
    'Où puis-je voir ton GitHub ?',
    'Comment te joindre sur LinkedIn ?',
    'Bonjour, comment ça va ?'
  ];
  
  for (const question of questions) {
    const event = {
      httpMethod: 'POST',
      body: JSON.stringify({ message: question })
    };
    
    try {
      const { handler } = require('./netlify/functions/api.js');
      const result = await handler(event, {});
      
      if (result.statusCode === 200) {
        const response = JSON.parse(result.body);
        console.log(`✅ "${question}" → ${response.response.substring(0, 50)}...`);
      } else {
        console.log(`❌ "${question}" → Erreur ${result.statusCode}`);
      }
    } catch (error) {
      console.log(`❌ "${question}" → Erreur: ${error.message}`);
    }
  }
}

async function main() {
  console.log('🚀 Test de la Solution Gratuite');
  console.log('=' * 50);
  
  // Test de base
  const success1 = await testGratuit();
  
  // Test de différentes questions
  await testQuestions();
  
  console.log('\n' + '=' * 50);
  if (success1) {
    console.log('✅ Solution gratuite fonctionnelle !');
    console.log('📋 Avantages:');
    console.log('- 100% gratuit');
    console.log('- Réponses instantanées');
    console.log('- Pas de dépendance externe');
    console.log('- Réponses personnalisées');
    
    console.log('\n📋 Prochaines étapes:');
    console.log('1. Redéployez sur Netlify');
    console.log('2. Supprimez la variable GOOGLE_API_KEY');
    console.log('3. Testez le chatbot en production');
  } else {
    console.log('❌ Problème détecté');
  }
}

if (require.main === module) {
  main().catch(console.error);
} 