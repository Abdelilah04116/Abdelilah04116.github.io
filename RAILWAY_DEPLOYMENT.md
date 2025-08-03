# 🚀 Guide de Déploiement Railway

## 📋 Prérequis

1. **Compte Railway** : https://railway.app
2. **Compte GitHub** : Votre code doit être sur GitHub
3. **Clé API Gemini** : https://makersuite.google.com/app/apikey

## 🛠️ Configuration

### 1. Préparer le Repository

```bash
# Ajouter les nouveaux fichiers
git add railway.json
git add railway_app.py
git add requirements-railway.txt
git add Procfile-railway
git add RAILWAY_DEPLOYMENT.md

# Commiter les changements
git commit -m "Add Railway deployment configuration"

# Pousser vers GitHub
git push origin main
```

### 2. Déployer sur Railway

1. **Aller sur Railway** : https://railway.app
2. **Se connecter** avec votre compte GitHub
3. **Cliquer "New Project"**
4. **Choisir "Deploy from GitHub repo"**
5. **Sélectionner votre repository** : `Abdelilah_ourti.github.io`
6. **Cliquer "Deploy Now"**

### 3. Configurer les Variables d'Environnement

1. **Dans votre projet Railway**, aller dans l'onglet "Variables"
2. **Ajouter la variable** :
   - **Nom** : `GOOGLE_API_KEY`
   - **Valeur** : Votre clé API Gemini
3. **Cliquer "Add"**

### 4. Configurer le Domaine

1. **Dans l'onglet "Settings"**
2. **Section "Domains"**
3. **Cliquer "Generate Domain"**
4. **Votre URL sera** : `https://votre-projet.railway.app`

## 🔧 Personnalisation

### Modifier vos Informations

Éditez le fichier `railway_app.py` et modifiez :

```python
# Ligne 25-30 : Vos vraies informations
- Téléphone : +33 6 XX XX XX XX (remplacez par votre vrai numéro)
- Email : abdellah.ourti@email.com (remplacez par votre vrai email)
```

### Modifier l'URL du Portfolio

Dans `railway_app.py`, ligne 95 :
```python
- Portfolio : https://abdelilah-ourti.railway.app
```

## 🧪 Test

### Test Local (Optionnel)

```bash
# Installer les dépendances
pip install -r requirements-railway.txt

# Lancer l'application
python railway_app.py

# Tester l'API
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quel est ton numéro de téléphone ?"}'
```

### Test en Production

1. **Aller sur votre URL Railway**
2. **Tester le chatbot** avec différentes questions
3. **Vérifier les logs** dans Railway Dashboard

## 📊 Monitoring

### Logs Railway

1. **Dashboard Railway** → Onglet "Deployments"
2. **Cliquer sur le dernier déploiement**
3. **Voir les logs en temps réel**

### Endpoint de Santé

Votre application expose un endpoint de santé :
```
https://votre-projet.railway.app/health
```

## 🔄 Redéploiement Automatique

Railway redéploie automatiquement quand vous poussez sur GitHub :

```bash
git add .
git commit -m "Update portfolio information"
git push origin main
```

## 🚨 Dépannage

### Problème : Application ne démarre pas

1. **Vérifier les logs** dans Railway Dashboard
2. **Vérifier requirements-railway.txt** est présent
3. **Vérifier railway_app.py** est le point d'entrée

### Problème : Chatbot ne répond pas

1. **Vérifier GOOGLE_API_KEY** dans les variables
2. **Tester l'endpoint /health**
3. **Vérifier les logs** pour les erreurs API

### Problème : Assets non trouvés

1. **Vérifier le dossier assets/** est présent
2. **Vérifier les permissions** des fichiers
3. **Tester l'URL** : `/assets/images/votre-image.png`

## 🎯 Avantages Railway

- ✅ **Gratuit** : 500 heures/mois
- ✅ **Simple** : Déploiement en 1 clic
- ✅ **Rapide** : Build et déploiement automatiques
- ✅ **Monitoring** : Logs et métriques intégrés
- ✅ **SSL** : HTTPS automatique
- ✅ **Variables d'environnement** : Sécurisées
- ✅ **Pas de limite de taille** : Contrairement à Vercel

## 📞 Support

- **Documentation Railway** : https://docs.railway.app
- **Discord Railway** : https://discord.gg/railway
- **GitHub Issues** : Pour les problèmes techniques

---

**🎉 Votre portfolio avec chatbot IA est maintenant prêt sur Railway !** 