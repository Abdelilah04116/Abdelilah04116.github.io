# 🚀 Déploiement GitHub Pages + Chatbot IA

## 🎯 **Solution Recommandée : GitHub Pages + Netlify Functions**

### **📋 Architecture**

- **Portfolio** : GitHub Pages (statique, gratuit)
- **Chatbot** : Netlify Functions (serverless, gratuit)
- **URLs** : 
  - Portfolio : `https://abdelilah04116.github.io`
  - Chatbot API : `https://abdelilah-ourti.netlify.app/.netlify/functions/api`

## 🛠️ **Étapes de Déploiement**

### **1. Déployer le Portfolio sur GitHub Pages**

#### **A. Préparer le Repository**
```bash
# Votre repo doit être : Abdelilah_ourti.github.io
# OU un repo normal avec GitHub Pages activé
```

#### **B. Activer GitHub Pages**
1. Aller sur votre repo GitHub
2. **Settings** → **Pages**
3. **Source** : Deploy from a branch
4. **Branch** : main
5. **Folder** : / (root)
6. **Save**

#### **C. Modifier l'URL de l'API dans index.html**
```javascript
// Remplacer dans index.html
const API_URL = 'https://abdelilah-ourti.netlify.app/.netlify/functions/api';
```

### **2. Déployer le Chatbot sur Netlify**

#### **A. Garder la configuration Netlify actuelle**
- ✅ `netlify.toml`
- ✅ `netlify/functions/api.js`
- ✅ `package.json`

#### **B. Configurer les variables d'environnement**
1. Aller sur Netlify Dashboard
2. **Site settings** → **Environment variables**
3. Ajouter `GOOGLE_API_KEY` = votre clé Gemini

#### **C. Déployer**
```bash
git add .
git commit -m "Update API URL for GitHub Pages"
git push origin main
```

## 🎯 **Résultat Final**

### **URLs**
- **Portfolio** : `https://abdelilah04116.github.io`
- **Chatbot API** : `https://abdelilah-ourti.netlify.app/.netlify/functions/api`

### **Fonctionnalités**
- ✅ **Portfolio** : Site statique rapide et professionnel
- ✅ **Chatbot IA** : Réponses intelligentes avec Gemini
- ✅ **Responsive** : Fonctionne sur tous les appareils
- ✅ **HTTPS** : Sécurisé automatiquement
- ✅ **Gratuit** : Aucun coût

## 🔧 **Alternative : Tout sur GitHub Pages**

### **Solution avec GitHub Actions + Railway**

#### **A. Créer le workflow GitHub Actions**
Le fichier `.github/workflows/chatbot-api.yml` est déjà créé.

#### **B. Configurer Railway**
1. Créer un compte Railway
2. Créer un projet
3. Obtenir le token Railway
4. Ajouter le secret `RAILWAY_TOKEN` dans GitHub

#### **C. Configurer les variables d'environnement**
Dans Railway :
- `GOOGLE_API_KEY` = votre clé Gemini

#### **D. Modifier l'URL de l'API**
```javascript
// Dans index.html
const API_URL = 'https://votre-app-railway.railway.app/api/chat';
```

## 🚨 **Dépannage**

### **Problème : CORS Error**
```javascript
// Vérifier que l'API a les bons headers CORS
'Access-Control-Allow-Origin': '*'
```

### **Problème : API ne répond pas**
1. Vérifier les logs Netlify/Railway
2. Tester l'endpoint `/health`
3. Vérifier la clé API Gemini

### **Problème : Portfolio ne se charge pas**
1. Vérifier que GitHub Pages est activé
2. Attendre quelques minutes pour le déploiement
3. Vérifier les logs GitHub Actions

## 🎯 **Avantages de cette Approche**

### **GitHub Pages**
- ✅ **Gratuit** : Hébergement illimité
- ✅ **Rapide** : CDN global
- ✅ **Sécurisé** : HTTPS automatique
- ✅ **Simple** : Déploiement automatique

### **Netlify Functions**
- ✅ **Gratuit** : 125k invocations/mois
- ✅ **Serverless** : Pas de serveur à gérer
- ✅ **Scalable** : S'adapte au trafic
- ✅ **IA** : Support complet pour Gemini

## 📞 **Support**

- **GitHub Pages** : https://pages.github.com
- **Netlify Functions** : https://docs.netlify.com/functions/overview/
- **Railway** : https://railway.app

---

**🎉 Votre portfolio avec chatbot IA sera accessible sur GitHub Pages !** 