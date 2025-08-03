#!/usr/bin/env node
/**
 * Test de détection des mots-clés
 */

async function testDetection() {
  console.log('🧪 Test de Détection des Mots-clés');
  console.log('=' * 50);
  
  const testQuestions = [
    'Qui es-tu ?',
    'Quelles sont tes compétences ?',
    'Parle-moi de tes projets',
    'Quelle est ta formation ?',
    'Comment te contacter ?',
    'Quelle est ton expérience ?',
    'Peux-tu me parler de ton CV ?',
    'Où puis-je voir ton GitHub ?',
    'Comment te joindre sur LinkedIn ?',
    'Bonjour, comment ça va ?',
    'Tu connais Python ?',
    'Quel est ton parcours ?',
    'Salut !',
    'Hello !',
    'Parle-moi de tes technologies',
    'Quel est ton travail ?',
    'Tu as quel diplôme ?',
    'Comment t\'envoyer un email ?',
    'Tu fais quoi comme métier ?',
    'Montre-moi ton code'
  ];
  
  let successCount = 0;
  let totalCount = 0;
  
  for (const question of testQuestions) {
    totalCount++;
    
    const event = {
      httpMethod: 'POST',
      body: JSON.stringify({ message: question })
    };
    
    try {
      const { handler } = require('./netlify/functions/api.js');
      const result = await handler(event, {});
      
      if (result.statusCode === 200) {
        const response = JSON.parse(result.body);
        const responseText = response.response;
        
        // Vérifier si la réponse est différente de la réponse par défaut
        const isDefaultResponse = responseText.includes('Que souhaitez-vous savoir spécifiquement ?');
        
        if (!isDefaultResponse) {
          console.log(`✅ "${question}" → Détection réussie`);
          successCount++;
        } else {
          console.log(`❌ "${question}" → Réponse par défaut`);
        }
        
        console.log(`   Réponse: ${responseText.substring(0, 80)}...`);
      } else {
        console.log(`❌ "${question}" → Erreur ${result.statusCode}`);
      }
    } catch (error) {
      console.log(`❌ "${question}" → Erreur: ${error.message}`);
    }
    
    console.log(''); // Ligne vide pour séparer
  }
  
  console.log('=' * 50);
  console.log(`📊 Résultats: ${successCount}/${totalCount} détections réussies`);
  console.log(`📈 Taux de réussite: ${Math.round((successCount/totalCount)*100)}%`);
  
  if (successCount > totalCount * 0.7) {
    console.log('🎉 Détection fonctionnelle !');
  } else {
    console.log('⚠️ Problème de détection détecté');
  }
}

async function testSpecificCases() {
  console.log('\n🧪 Test de Cas Spécifiques');
  console.log('=' * 50);
  
  const specificTests = [
    { question: 'Qui es-tu ?', expected: 'identité' },
    { question: 'Tes compétences ?', expected: 'compétences' },
    { question: 'Tes projets ?', expected: 'projets' },
    { question: 'Ta formation ?', expected: 'formation' },
    { question: 'Ton contact ?', expected: 'contact' },
    { question: 'Ton expérience ?', expected: 'expérience' },
    { question: 'Ton CV ?', expected: 'CV' },
    { question: 'Ton GitHub ?', expected: 'GitHub' },
    { question: 'Ton LinkedIn ?', expected: 'LinkedIn' },
    { question: 'Bonjour !', expected: 'salutation' }
  ];
  
  for (const test of specificTests) {
    const event = {
      httpMethod: 'POST',
      body: JSON.stringify({ message: test.question })
    };
    
    try {
      const { handler } = require('./netlify/functions/api.js');
      const result = await handler(event, {});
      
      if (result.statusCode === 200) {
        const response = JSON.parse(result.body);
        const responseText = response.response;
        
        // Vérifier si la réponse contient des mots-clés spécifiques
        let detected = 'non détecté';
        
        if (responseText.includes('passionné par le Deep Learning')) detected = 'identité';
        else if (responseText.includes('compétences principales')) detected = 'compétences';
        else if (responseText.includes('projets passionnants')) detected = 'projets';
        else if (responseText.includes('Master en IA')) detected = 'formation';
        else if (responseText.includes('LinkedIn') && responseText.includes('GitHub')) detected = 'contact';
        else if (responseText.includes('développeur IA')) detected = 'expérience';
        else if (responseText.includes('ingénieur en IA avec un Master')) detected = 'CV';
        else if (responseText.includes('GitHub (Abdelilah04116)')) detected = 'GitHub';
        else if (responseText.includes('profil LinkedIn')) detected = 'LinkedIn';
        else if (responseText.includes('Bonjour !')) detected = 'salutation';
        
        const success = detected === test.expected;
        console.log(`${success ? '✅' : '❌'} "${test.question}" → ${detected} (attendu: ${test.expected})`);
      }
    } catch (error) {
      console.log(`❌ "${test.question}" → Erreur: ${error.message}`);
    }
  }
}

async function main() {
  await testDetection();
  await testSpecificCases();
  
  console.log('\n' + '=' * 50);
  console.log('📋 Recommandations:');
  console.log('1. Si la détection fonctionne, redéployez');
  console.log('2. Si problème, vérifiez les logs Netlify');
  console.log('3. Testez en production après déploiement');
}

if (require.main === module) {
  main().catch(console.error);
} 