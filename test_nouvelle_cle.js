#!/usr/bin/env node
/**
 * Test de la nouvelle clé API Google Gemini
 */

async function testNouvelleCle() {
  console.log('🧪 Test de la nouvelle clé API');
  console.log('=' * 50);
  
  try {
    // Remplacez par votre nouvelle clé
    const apiKey = 'VOTRE_NOUVELLE_CLE_API';
    
    console.log('✅ Test de l\'API Gemini...');
    
    const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent', {
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
    
    if (!response.ok) {
      const errorText = await response.text();
      console.error(`❌ Erreur API: ${response.status} - ${errorText}`);
      return false;
    }
    
    const data = await response.json();
    const text = data.candidates[0].content.parts[0].text;
    
    console.log(`✅ Réponse: ${text}`);
    console.log('🎉 Clé API valide !');
    
    return true;
    
  } catch (error) {
    console.error(`❌ Erreur: ${error.message}`);
    return false;
  }
}

async function main() {
  console.log('🚀 Test de la Nouvelle Clé API');
  console.log('=' * 50);
  
  const success = await testNouvelleCle();
  
  if (success) {
    console.log('\n✅ Clé API fonctionnelle !');
    console.log('📋 Prochaines étapes:');
    console.log('1. Copiez cette clé dans Netlify');
    console.log('2. Redéployez le site');
    console.log('3. Testez le chatbot');
  } else {
    console.log('\n❌ Problème avec la clé API');
    console.log('📋 Vérifiez:');
    console.log('1. La clé est-elle correcte ?');
    console.log('2. Avez-vous accès à l\'API Gemini ?');
    console.log('3. Le projet est-il activé ?');
  }
}

if (require.main === module) {
  main().catch(console.error);
} 