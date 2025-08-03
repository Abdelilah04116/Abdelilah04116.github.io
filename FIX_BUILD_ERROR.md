# Correction de l'Erreur de Build Netlify

## 🚨 Problème Identifié

L'erreur de build Netlify indique que le package `@google/generative-ai@^0.3.2` n'est pas trouvé.

## 🔧 Solution Appliquée

### 1. Correction du package.json

**Avant (incorrect) :**
```json
{
  "dependencies": {
    "@google/generative-ai": "^0.3.2"
  }
}
```

**Après (correct) :**
```json
{
  "dependencies": {
    "@google/generativeai": "^0.2.1"
  }
}
```

### 2. Correction des imports

**Dans `netlify/functions/api.js` :**
```javascript
// Avant
const { GoogleGenerativeAI } = require('@google/generative-ai');

// Après
const { GoogleGenerativeAI } = require('@google/generativeai');
```

**Dans `test_netlify.js` :**
```javascript
// Avant
const { GoogleGenerativeAI } = require('@google/generative-ai');

// Après
const { GoogleGenerativeAI } = require('@google/generativeai');
```

## 🚀 Étapes de Correction

### 1. Test Local
```bash
# Installer les dépendances
npm install

# Vérifier que l'installation fonctionne
npm list @google/generativeai
```

### 2. Test de l'API
```bash
# Tester l'API locale
node test_netlify.js
```

### 3. Redéploiement
```bash
# Poussez les corrections
git add .
git commit -m "Fix: Correct Google Generative AI package name"
git push origin main
```

## 🔍 Vérification

### Vérifiez que le package est correct
```bash
# Vérifier la version disponible
npm view @google/generativeai versions --json

# Vérifier l'installation
npm list @google/generativeai
```

### Test de l'API
```bash
# Test local
node test_netlify.js

# Test en production (après déploiement)
curl -X POST https://votre-site.netlify.app/.netlify/functions/api \
  -H "Content-Type: application/json" \
  -d '{"message": "Qui es-tu ?"}'
```

## 📊 Différences de Packages

| Package | Version | Statut |
|---------|---------|--------|
| `@google/generative-ai` | `^0.3.2` | ❌ Non trouvé |
| `@google/generativeai` | `^0.2.1` | ✅ Disponible |

## 🎯 Résultat Attendu

Après correction :
- ✅ **Build Netlify** : Succès
- ✅ **Installation npm** : Pas d'erreur
- ✅ **API** : Fonctionnelle
- ✅ **Chatbot** : Opérationnel

## 🆘 Si le Problème Persiste

### 1. Vérifiez les logs Netlify
```bash
netlify logs --tail
```

### 2. Testez avec une version spécifique
```json
{
  "dependencies": {
    "@google/generativeai": "0.2.1"
  }
}
```

### 3. Alternative : Utiliser fetch API
Si le package pose toujours problème, on peut utiliser l'API REST directement :
```javascript
const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.GOOGLE_API_KEY}`
  },
  body: JSON.stringify({
    contents: [{
      parts: [{
        text: prompt
      }]
    }]
  })
});
```

---

**Cette correction devrait résoudre définitivement l'erreur de build Netlify ! 🚀** 