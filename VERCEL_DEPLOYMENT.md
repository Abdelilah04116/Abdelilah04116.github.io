# Guide de Déploiement Vercel - Architecture Optimisée

Ce guide vous aide à déployer votre portfolio avec chatbot sur Vercel en utilisant une architecture serverless optimisée.

## 🏗️ Architecture

- **Frontend** : `index.html` (statique)
- **API** : `api/chat.py` (Vercel Functions)
- **Dépendances** : `api/requirements.txt` (minimales)

## 🚀 Étapes de Déploiement

### 1. Préparation

1. **Installer Vercel CLI** (optionnel mais recommandé) :
   ```bash
   npm install -g vercel
   ```

2. **Vérifier les fichiers de configuration** :
   - ✅ `vercel.json` - Configuration Vercel Functions
   - ✅ `api/requirements.txt` - Dépendances minimales
   - ✅ `api/chat.py` - API serverless
   - ✅ `.vercelignore` - Fichiers à ignorer

### 2. Configuration des Variables d'Environnement

1. **Aller sur [Vercel Dashboard](https://vercel.com/dashboard)**
2. **Créer un nouveau projet** ou sélectionner votre projet existant
3. **Dans les paramètres du projet** → **Environment Variables**
4. **Ajouter la variable** :
   - **Name** : `GOOGLE_API_KEY`
   - **Value** : Votre clé API Gemini
   - **Environments** : Production, Preview, Development

### 3. Déploiement

#### Option A : Via GitHub (Recommandé)

1. **Pousser votre code sur GitHub**
2. **Connecter votre repo GitHub à Vercel**
3. **Configurer le projet** :
   - **Framework Preset** : Other
   - **Build Command** : (laisser vide - automatique)
   - **Output Directory** : (laisser vide)
   - **Install Command** : (laisser vide - automatique)

**✅ Avantage** : Architecture serverless optimisée (~5MB max)

#### Option B : Via Vercel CLI

```bash
# Dans le répertoire de votre projet
vercel

# Suivre les instructions
# - Link to existing project ou Create new project
# - Confirmer les paramètres
```

### 4. Vérification

1. **Tester l'API** :
   ```bash
   python test_vercel_api.py
   ```

2. **Vérifier les logs** dans le dashboard Vercel

3. **Tester en local** :
   ```bash
   python -c "from api.chat import generate_response; print(generate_response('Qui es-tu ?'))"
   ```

## 🔧 Configuration Avancée

### Optimisations pour Vercel

1. **Limites de Vercel** :
   - **Timeout** : 10 secondes pour les fonctions serverless
   - **Taille** : 250MB maximum par fonction (optimisé à ~5MB)
   - **Mémoire** : 1024MB maximum

2. **Architecture Serverless** :
   - API séparée en Vercel Functions
   - Dépendances minimales (seulement `google-generativeai`)
   - Contexte du portfolio intégré dans le code
   - Pas de Flask ni de serveur web

### Variables d'Environnement Recommandées

```env
GOOGLE_API_KEY=your_gemini_api_key_here
PYTHONPATH=.
```

## 🐛 Dépannage

### Problèmes Courants

1. **"Module not found"** :
   - Vérifiez que `requirements-vercel.txt` contient toutes les dépendances
   - Assurez-vous que `PYTHONPATH=.` est défini

2. **"API Key not found"** :
   - Vérifiez que `GOOGLE_API_KEY` est configurée dans Vercel
   - Redéployez après avoir ajouté la variable

3. **"Timeout"** :
   - Le chatbot peut prendre du temps à initialiser
   - Utilisez le mode fallback si nécessaire

4. **"Vectorstore error"** :
   - Le chatbot fonctionnera en mode fallback
   - Vérifiez les logs pour plus de détails

### Logs et Debug

1. **Voir les logs** :
   - Dashboard Vercel → Functions → Logs
   - Ou via CLI : `vercel logs`

2. **Test local** :
   ```bash
   python wsgi.py
   ```

## 📝 Notes Importantes

- **Compatibilité Render** : Les fichiers Render (`Procfile`, etc.) sont conservés
- **Performance** : Le premier appel peut être lent (cold start)
- **Sécurité** : Ne jamais commiter la clé API dans le code
- **Backup** : Gardez une copie de votre configuration Render

## 🆘 Support

Si vous rencontrez des problèmes :

1. **Vérifiez les logs** dans le dashboard Vercel
2. **Testez en local** avec `python wsgi.py`
3. **Vérifiez la configuration** des variables d'environnement
4. **Consultez la documentation** Vercel pour Python

---

**Bon déploiement ! 🚀** 