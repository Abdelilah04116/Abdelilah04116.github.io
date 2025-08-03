# Guide de Déploiement Netlify - Portfolio avec Assistant IA

## 🎯 Vue d'Ensemble

Déploiement de votre portfolio avec assistant IA sur Netlify en utilisant les Netlify Functions.

## 🏗️ Architecture

```
portfolio/
├── netlify.toml              # Configuration Netlify
├── package.json              # Dépendances Node.js
├── netlify/functions/api.js  # Fonction serverless
├── index.html               # Frontend (inchangé)
├── assets/                  # Ressources statiques
└── test_netlify.js          # Tests
```

## 🚀 Étapes de Déploiement

### 1. Préparation Locale

```bash
# Installer les dépendances
npm install

# Tester en local
npm run dev

# Tester l'API
node test_netlify.js
```

### 2. Déploiement sur Netlify

#### Option A: Via GitHub (Recommandé)

1. **Poussez le code sur GitHub**
   ```bash
   git add .
   git commit -m "Add Netlify deployment"
   git push origin main
   ```

2. **Connectez votre repo à Netlify**
   - Allez sur [netlify.com](https://netlify.com)
   - Cliquez sur "New site from Git"
   - Choisissez votre repo GitHub
   - Configurez les paramètres :
     - **Build command**: `npm run build`
     - **Publish directory**: `.`

3. **Configurez les variables d'environnement**
   - Dans Netlify Dashboard → Site settings → Environment variables
   - Ajoutez : `GOOGLE_API_KEY` = `AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y`

#### Option B: Via Netlify CLI

```bash
# Installer Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Déployer
netlify deploy --prod
```

## 🔧 Configuration

### netlify.toml
```toml
[build]
  publish = "."
  command = ""

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/api/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[functions]
  directory = "netlify/functions"
```

### package.json
```json
{
  "dependencies": {
    "@google/generative-ai": "^0.3.2"
  },
  "devDependencies": {
    "netlify-cli": "^17.0.0"
  }
}
```

## 🧪 Tests

### Test Local
```bash
# Test de l'API
node test_netlify.js

# Test du serveur local
npm run dev
```

### Test en Production
```bash
# Test de l'API
curl -X POST https://votre-site.netlify.app/.netlify/functions/api \
  -H "Content-Type: application/json" \
  -d '{"message": "Qui es-tu ?"}'
```

## 🔍 Dépannage

### Problèmes Courants

1. **Erreur 404 sur l'API**
   - Vérifiez que la fonction est dans `netlify/functions/api.js`
   - Vérifiez la configuration `netlify.toml`

2. **Erreur de clé API**
   - Vérifiez que `GOOGLE_API_KEY` est configurée dans Netlify
   - Vérifiez que la clé est valide

3. **Erreur de build**
   - Vérifiez que `package.json` est correct
   - Vérifiez les logs de build dans Netlify

### Logs Netlify

```bash
# Voir les logs en temps réel
netlify logs --tail

# Voir les logs des fonctions
netlify logs --functions
```

## 📊 Avantages Netlify

| Aspect | Avantage |
|--------|----------|
| **Performance** | CDN global, chargement rapide |
| **Fonctions** | Serverless functions intégrées |
| **Déploiement** | Automatique depuis GitHub |
| **HTTPS** | Certificat SSL gratuit |
| **Domaines** | Sous-domaines personnalisés |
| **Logs** | Monitoring complet |

## 🎯 Résultat Final

Après déploiement :
- ✅ **Site principal** : `https://votre-site.netlify.app`
- ✅ **API** : `https://votre-site.netlify.app/.netlify/functions/api`
- ✅ **Chatbot** : Fonctionnel dans l'interface
- ✅ **Images** : Toutes les assets servies correctement

## 🆘 Support

### Si rien ne fonctionne
1. **Vérifiez les logs** Netlify
2. **Testez en local** avec `npm run dev`
3. **Vérifiez** les variables d'environnement
4. **Contactez** le support Netlify

---

**Cette configuration Netlify devrait déployer votre portfolio avec assistant IA parfaitement ! 🚀** 