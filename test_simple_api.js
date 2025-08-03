#!/usr/bin/env node
/**
 * Test simple de l'API Gemini
 */

async function testAPI() {
  console.log('🧪 Test Simple de l\'API Gemini');
  console.log('=' * 50);
  
  // Remplacez par votre clé API
  const apiKey = 'AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y';
  
  try {
    console.log('✅ Test avec API key dans l\'URL...');
    
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apiKey}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: 'Dis-moi bonjour en français'
          }]
        }]
      })
    });
    
    console.log(`📊 Status: ${response.status}`);
    
    if (response.ok) {
      const data = await response.json();
      const text = data.candidates[0].content.parts[0].text;
      console.log(`✅ Réponse: ${text}`);
      console.log('🎉 API fonctionnelle !');
      return true;
    } else {
      const errorText = await response.text();
      console.error(`❌ Erreur: ${response.status} - ${errorText}`);
      
      // Test alternatif avec Bearer token
      console.log('\n🔄 Test avec Bearer token...');
      const response2 = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          contents: [{
            parts: [{
              text: 'Dis-moi bonjour en français'
            }]
          }]
        })
      });
      
      console.log(`📊 Status Bearer: ${response2.status}`);
      
      if (response2.ok) {
        const data2 = await response2.json();
        const text2 = data2.candidates[0].content.parts[0].text;
        console.log(`✅ Réponse Bearer: ${text2}`);
        console.log('🎉 API fonctionnelle avec Bearer !');
        return true;
      } else {
        const errorText2 = await response2.text();
        console.error(`❌ Erreur Bearer: ${response2.status} - ${errorText2}`);
        return false;
      }
    }
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return false;
  }
}

async function main() {
  const success = await testAPI();
  
  console.log('\n' + '=' * 50);
  if (success) {
    console.log('✅ Test réussi ! L\'API fonctionne.');
    console.log('📋 Prochaines étapes:');
    console.log('1. Redéployez sur Netlify');
    console.log('2. Testez le chatbot');
  } else {
    console.log('❌ Test échoué. Problèmes possibles:');
    console.log('1. Clé API invalide');
    console.log('2. API non activée');
    console.log('3. Quotas dépassés');
    console.log('4. Projet Google Cloud mal configuré');
    
    console.log('\n🔧 Solutions:');
    console.log('1. Créez une nouvelle clé sur Google AI Studio');
    console.log('2. Activez l\'API Generative Language');
    console.log('3. Vérifiez les quotas du projet');
  }
}

if (require.main === module) {
  main().catch(console.error);
} 