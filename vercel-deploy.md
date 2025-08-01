# 🚀 Guide de Déploiement Vercel - Portfolio avec Chatbot

## 📋 Prérequis

1. **Compte Vercel** : Créez un compte sur [vercel.com](https://vercel.com)
2. **GitHub Repository** : Votre code doit être sur GitHub
3. **Variables d'environnement** : Vous avez déjà configuré `GOOGLE_API_KEY`

## 🔧 Configuration

### 1. Fichiers de Configuration Créés

- ✅ `vercel.json` - Configuration Vercel
- ✅ `requirements-vercel.txt` - Dépendances Python optimisées
- ✅ `api/chat.py` - Endpoint API serverless
- ✅ `api/__init__.py` - Package Python

### 2. Structure du Projet

```
portfolio/
├── api/
│   ├── __init__.py
│   └── chat.py          # Endpoint API Vercel
├── chatbot/
│   ├── chatbot_logic.py
│   ├── docs/
│   └── vectorstore/
├── assets/
├── index.html           # Interface utilisateur
├── portfolio_data.py    # Données du portfolio
├── requirements-vercel.txt
├── vercel.json          # Configuration Vercel
└── README.md
```

## 🚀 Déploiement

### Option 1 : Déploiement via Dashboard Vercel

1. **Connectez votre repository GitHub**
   - Allez sur [vercel.com/dashboard](https://vercel.com/dashboard)
   - Cliquez "New Project"
   - Importez votre repository GitHub

2. **Configuration du projet**
   - **Framework Preset** : Other
   - **Root Directory** : `./` (laisser vide)
   - **Build Command** : `pip install -r requirements-vercel.txt`
   - **Output Directory** : `./` (laisser vide)
   - **Install Command** : `pip install -r requirements-vercel.txt`

3. **Variables d'environnement**
   - `GOOGLE_API_KEY` : Votre clé API Google (déjà configurée)

4. **Déployer**
   - Cliquez "Deploy"

### Option 2 : Déploiement via CLI Vercel

```bash
# Installer Vercel CLI
npm i -g vercel

# Se connecter à Vercel
vercel login

# Déployer
vercel

# Pour la production
vercel --prod
```

## 🔗 URLs de Déploiement

Après le déploiement, vous aurez :

- **URL de production** : `https://votre-projet.vercel.app`
- **URL de preview** : `https://votre-projet-git-main.vercel.app`
- **API Endpoint** : `https://votre-projet.vercel.app/api/chat`

## 🧪 Test du Déploiement

### 1. Test de l'API

```bash
curl -X POST https://votre-projet.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quel est le nom d\'Abdelilah ?"}'
```

### 2. Test de santé

```bash
curl https://votre-projet.vercel.app/api/health
```

### 3. Test de l'interface

Visitez `https://votre-projet.vercel.app` et testez le chatbot.

## ⚙️ Configuration Avancée

### Optimisation des Performances

Le fichier `vercel.json` est configuré pour :

- **Serverless Functions** : API optimisée pour Vercel
- **Static Assets** : `index.html` servi statiquement
- **Routing** : Redirection automatique vers l'API
- **Timeout** : 30 secondes max par requête

### Variables d'Environnement

Dans le dashboard Vercel :

```bash
GOOGLE_API_KEY=AIzaSyAE_7Y0cA46UZxXa2vxToKkJcTBi8m97Rs
```

## 🔍 Monitoring et Logs

### Accès aux Logs

1. **Dashboard Vercel** : Projet → Functions → Logs
2. **CLI** : `vercel logs`

### Métriques

- **Function Calls** : Nombre d'appels API
- **Execution Time** : Temps de réponse
- **Error Rate** : Taux d'erreurs

## 🛠️ Dépannage

### Problèmes Courants

1. **ModuleNotFoundError**
   - Vérifiez `requirements-vercel.txt`
   - Redéployez après modification

2. **Timeout Errors**
   - Augmentez `maxDuration` dans `vercel.json`
   - Optimisez le code du chatbot

3. **CORS Errors**
   - Vérifiez la configuration CORS dans `api/chat.py`

4. **API Key Issues**
   - Vérifiez les variables d'environnement Vercel
   - Testez avec `curl` ou Postman

### Debug

```bash
# Logs en temps réel
vercel logs --follow

# Informations du projet
vercel ls

# Redéploiement forcé
vercel --force
```

## 📊 Comparaison Render vs Vercel

| Aspect | Render | Vercel |
|--------|--------|--------|
| **Type** | Container | Serverless |
| **Performance** | Bonne | Excellente |
| **Cold Start** | Modéré | Rapide |
| **Coût** | Gratuit (limité) | Gratuit (généreux) |
| **Déploiement** | Git push | Git push |
| **Scaling** | Manuel | Automatique |

## 🎯 Avantages Vercel

- ✅ **Déploiement ultra-rapide**
- ✅ **Serverless functions optimisées**
- ✅ **CDN global**
- ✅ **HTTPS automatique**
- ✅ **Preview deployments**
- ✅ **Monitoring intégré**
- ✅ **Gratuit pour projets personnels**

## 🔄 Mise à Jour

Pour mettre à jour le déploiement :

```bash
# Push vers GitHub
git add .
git commit -m "Update portfolio"
git push

# Vercel déploie automatiquement
```

## 📞 Support

En cas de problème :

1. **Logs Vercel** : Dashboard → Functions → Logs
2. **Documentation** : [vercel.com/docs](https://vercel.com/docs)
3. **Community** : [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)

---

*Déploiement Vercel configuré et optimisé pour votre portfolio avec chatbot ! 🚀* 