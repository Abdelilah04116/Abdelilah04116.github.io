# 🚀 Guide de Déploiement Fly.io

## 📋 Prérequis

1. **Compte Fly.io** : https://fly.io
2. **Fly CLI** : Installer avec `curl -L https://fly.io/install.sh | sh`
3. **Compte GitHub** : Votre code doit être sur GitHub
4. **Clé API Gemini** : https://makersuite.google.com/app/apikey

## 🛠️ Configuration

### 1. Installer Fly CLI

```bash
# Windows (PowerShell)
iwr https://fly.io/install.ps1 -useb | iex

# macOS/Linux
curl -L https://fly.io/install.sh | sh

# Vérifier l'installation
fly version
```

### 2. Se connecter à Fly.io

```bash
fly auth signup
# ou si vous avez déjà un compte
fly auth login
```

### 3. Préparer le Repository

```bash
# Ajouter les nouveaux fichiers
git add fly.toml
git add fly_app.py
git add Dockerfile
git add .dockerignore
git add FLY_DEPLOYMENT.md

# Commiter les changements
git commit -m "Add Fly.io deployment configuration"

# Pousser vers GitHub
git push origin main
```

### 4. Déployer sur Fly.io

```bash
# Créer l'application (remplacez 'portfolio-chatbot' par votre nom)
fly launch --name portfolio-chatbot

# Répondre aux questions :
# - Would you like to copy its configuration to the new app? → No
# - Would you like to set up a Postgresql database now? → No
# - Would you like to set up an Upstash Redis database now? → No
# - Would you like to deploy now? → Yes
```

### 5. Configurer les Variables d'Environnement

```bash
# Ajouter la clé API Gemini
fly secrets set GOOGLE_API_KEY="votre-clé-api-gemini"

# Vérifier les secrets
fly secrets list
```

### 6. Déployer l'Application

```bash
# Déployer
fly deploy

# Vérifier le statut
fly status

# Voir les logs
fly logs
```

## 🔧 Personnalisation

### Modifier vos Informations

Éditez le fichier `fly_app.py` et modifiez :

```python
# Ligne 25-30 : Vos vraies informations
- Téléphone : +33 6 XX XX XX XX (remplacez par votre vrai numéro)
- Email : abdellah.ourti@email.com (remplacez par votre vrai email)
```

### Modifier l'URL du Portfolio

Dans `fly_app.py`, ligne 95 :
```python
- Portfolio : https://portfolio-chatbot.fly.dev
```

### Modifier le nom de l'application

Dans `fly.toml`, ligne 5 :
```toml
app = "votre-nom-app"
```

## 🧪 Test

### Test Local (Optionnel)

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python fly_app.py

# Tester l'API
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quel est ton numéro de téléphone ?"}'
```

### Test en Production

```bash
# Ouvrir l'application
fly open

# Tester l'endpoint de santé
curl https://portfolio-chatbot.fly.dev/health
```

## 📊 Monitoring

### Logs Fly.io

```bash
# Voir les logs en temps réel
fly logs

# Voir les logs d'une machine spécifique
fly logs -i <machine-id>
```

### Métriques

```bash
# Voir les métriques
fly status

# Voir les machines
fly machines list
```

### Endpoint de Santé

Votre application expose un endpoint de santé :
```
https://portfolio-chatbot.fly.dev/health
```

## 🔄 Redéploiement

```bash
# Redéployer après modifications
git add .
git commit -m "Update portfolio information"
git push origin main
fly deploy
```

## 🚨 Dépannage

### Problème : Application ne démarre pas

```bash
# Vérifier les logs
fly logs

# Vérifier le statut
fly status

# Redémarrer l'application
fly apps restart portfolio-chatbot
```

### Problème : Chatbot ne répond pas

```bash
# Vérifier les secrets
fly secrets list

# Tester l'endpoint de santé
curl https://portfolio-chatbot.fly.dev/health

# Voir les logs pour les erreurs API
fly logs
```

### Problème : Assets non trouvés

```bash
# Vérifier que le dossier assets/ est présent
ls -la assets/

# Tester une image
curl https://portfolio-chatbot.fly.dev/assets/images/python-icon.png
```

## 🎯 Avantages Fly.io

- ✅ **Gratuit** : 3 VMs, 3GB RAM, 160GB storage
- ✅ **Très rapide** : Edge computing global
- ✅ **Auto-scaling** : S'adapte au trafic
- ✅ **Docker** : Déploiement flexible
- ✅ **SSL** : HTTPS automatique
- ✅ **Variables d'environnement** : Sécurisées
- ✅ **Monitoring** : Logs et métriques intégrés

## 📞 Support

- **Documentation Fly.io** : https://fly.io/docs
- **Discord Fly.io** : https://discord.gg/flyio
- **GitHub Issues** : Pour les problèmes techniques

## 🔧 Commandes Utiles

```bash
# Voir toutes les applications
fly apps list

# Voir les machines
fly machines list

# Redémarrer une machine
fly machines restart <machine-id>

# Supprimer l'application
fly apps destroy portfolio-chatbot

# Voir les variables d'environnement
fly config env

# Ouvrir l'application dans le navigateur
fly open
```

---

**🎉 Votre portfolio avec chatbot IA est maintenant prêt sur Fly.io !**

**URL finale :** `https://portfolio-chatbot.fly.dev` 