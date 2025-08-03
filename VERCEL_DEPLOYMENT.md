# Guide de Déploiement Vercel

Ce guide vous aide à déployer votre portfolio avec chatbot sur Vercel.

## 🚀 Étapes de Déploiement

### 1. Préparation

1. **Installer Vercel CLI** (optionnel mais recommandé) :
   ```bash
   npm install -g vercel
   ```

2. **Vérifier les fichiers de configuration** :
   - ✅ `vercel.json` - Configuration Vercel
   - ✅ `requirements-vercel.txt` - Dépendances Python
   - ✅ `wsgi.py` - Point d'entrée de l'application
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
   - **Build Command** : `pip install -r requirements-vercel.txt`
   - **Output Directory** : (laisser vide)
   - **Install Command** : `pip install -r requirements-vercel.txt`

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

## 🔧 Configuration Avancée

### Optimisations pour Vercel

1. **Limites de Vercel** :
   - **Timeout** : 10 secondes pour les fonctions serverless
   - **Taille** : 50MB maximum par fonction
   - **Mémoire** : 1024MB maximum

2. **Gestion du Vectorstore** :
   - Le vectorstore sera recréé à chaque déploiement
   - Utilisez le mode fallback si nécessaire

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