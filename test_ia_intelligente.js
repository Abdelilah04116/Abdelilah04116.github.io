#!/usr/bin/env node
/**
 * Test de la vraie IA intelligente
 */

async function testIAIntelligente() {
  console.log('🧪 Test de la Vraie IA Intelligente');
  console.log('=' * 50);
  
  const testQuestions = [
    'Quel est ton numéro de téléphone ?',
    'Comment je peux te joindre ?',
    'Parle-moi de ton expérience',
    'Qu\'est-ce que tu sais faire ?',
    'Montre-moi tes projets',
    'Tu as quel diplôme ?',
    'Tu travailles où ?',
    'Tu habites où ?',
    'Tu fais quoi comme métier ?',
    'Tu connais quelles technologies ?',
    'Peux-tu me donner ton email ?',
    'Quelle est ta formation ?',
    'Raconte-moi ton parcours',
    'Tu es disponible pour des projets ?',
    'Comment te contacter ?',
    'Tu maîtrises Python ?',
    'Parle-moi de tes compétences',
    'Quels sont tes projets récents ?',
    'Tu as de l\'expérience en freelance ?',
    'Peux-tu me parler de ton CV ?'
  ];
  
  console.log('📋 Questions de test intelligentes :');
  testQuestions.forEach((q, i) => {
    console.log(`${i + 1}. ${q}`);
  });
  
  console.log('\n' + '=' * 50);
  console.log('🚀 Test en cours...');
  console.log('=' * 50);
  
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
        
        // Vérifier si la réponse est intelligente (pas la réponse par défaut)
        const isIntelligentResponse = !responseText.includes('Que souhaitez-vous savoir ?') && 
                                    responseText.length > 50;
        
        if (isIntelligentResponse) {
          console.log(`✅ "${question}"`);
          console.log(`   Réponse: ${responseText.substring(0, 100)}...`);
          successCount++;
        } else {
          console.log(`❌ "${question}" → Réponse générique`);
          console.log(`   Réponse: ${responseText.substring(0, 100)}...`);
        }
      } else {
        console.log(`❌ "${question}" → Erreur ${result.statusCode}`);
      }
    } catch (error) {
      console.log(`❌ "${question}" → Erreur: ${error.message}`);
    }
    
    console.log(''); // Ligne vide pour séparer
  }
  
  console.log('=' * 50);
  console.log(`📊 Résultats: ${successCount}/${totalCount} réponses intelligentes`);
  console.log(`📈 Taux de réussite: ${Math.round((successCount/totalCount)*100)}%`);
  
  if (successCount > totalCount * 0.8) {
    console.log('🎉 IA Intelligente fonctionnelle !');
  } else if (successCount > totalCount * 0.5) {
    console.log('⚠️ IA partiellement fonctionnelle');
  } else {
    console.log('❌ Problème avec l\'IA détecté');
  }
}

async function testQuestionsSpecifiques() {
  console.log('\n🧪 Test de Questions Spécifiques');
  console.log('=' * 50);
  
  const specificTests = [
    { 
      question: 'Quel est ton numéro de téléphone ?', 
      expected: 'téléphone' 
    },
    { 
      question: 'Comment je peux te joindre ?', 
      expected: 'contact' 
    },
    { 
      question: 'Parle-moi de ton expérience', 
      expected: 'expérience' 
    },
    { 
      question: 'Tu as quel diplôme ?', 
      expected: 'formation' 
    },
    { 
      question: 'Tu habites où ?', 
      expected: 'localisation' 
    }
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
        
        // Vérifier si la réponse contient les informations attendues
        let detected = 'non détecté';
        
        if (responseText.includes('+33') || responseText.includes('téléphone')) detected = 'téléphone';
        else if (responseText.includes('LinkedIn') || responseText.includes('GitHub')) detected = 'contact';
        else if (responseText.includes('freelance') || responseText.includes('expérience')) detected = 'expérience';
        else if (responseText.includes('Master') || responseText.includes('diplôme')) detected = 'formation';
        else if (responseText.includes('France') || responseText.includes('localisation')) detected = 'localisation';
        
        const success = detected === test.expected;
        console.log(`${success ? '✅' : '❌'} "${test.question}" → ${detected} (attendu: ${test.expected})`);
        
        if (!success) {
          console.log(`   Réponse: ${responseText.substring(0, 80)}...`);
        }
      }
    } catch (error) {
      console.log(`❌ "${test.question}" → Erreur: ${error.message}`);
    }
  }
}

async function main() {
  await testIAIntelligente();
  await testQuestionsSpecifiques();
  
  console.log('\n' + '=' * 50);
  console.log('📋 Recommandations:');
  console.log('1. Si l\'IA fonctionne, redéployez');
  console.log('2. Personnalisez vos informations dans le code');
  console.log('3. Configurez votre clé API Gemini');
  console.log('4. Testez en production');
  
  console.log('\n🔧 Pour personnaliser :');
  console.log('- Remplacez le numéro de téléphone');
  console.log('- Remplacez l\'email');
  console.log('- Ajoutez vos vraies informations');
  console.log('- Modifiez le contexte selon vos besoins');
}

if (require.main === module) {
  main().catch(console.error);
} 