# Configuration Netlify - Variable d'Environnement

## 🚨 Problème Identifié

L'erreur `GOOGLE_API_KEY non configurée` indique que la variable d'environnement n'est pas configurée dans Netlify.

## 🔧 Solution : Configuration de la Variable d'Environnement

### Étape 1 : Accéder aux Paramètres Netlify

1. **Connectez-vous** à [Netlify](https://app.netlify.com)
2. **Sélectionnez** votre site déployé
3. **Cliquez** sur l'onglet **"Site settings"** (⚙️)

### Étape 2 : Ajouter la Variable d'Environnement

1. **Dans le menu de gauche**, cliquez sur **"Environment variables"**
2. **Cliquez** sur **"Add a variable"**
3. **Remplissez** les champs :
   - **Key** : `GOOGLE_API_KEY`
   - **Value** : `AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y`
4. **Cliquez** sur **"Save"**

### Étape 3 : Redéployer

1. **Retournez** à l'onglet **"Deploys"**
2. **Cliquez** sur **"Trigger deploy"** → **"Deploy site"**
3. **Attendez** que le déploiement se termine

## 📋 Configuration Complète

### Variables d'Environnement Requises

| Variable | Valeur | Description |
|----------|--------|-------------|
| `GOOGLE_API_KEY` | `AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y` | Clé API Google Gemini |

### Paramètres de Build

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| **Build command** | `npm run build` | Commande de build |
| **Publish directory** | `.` | Dossier de publication |
| **Node version** | `18` | Version de Node.js |

## 🧪 Test de la Configuration

### Test 1 : Vérification de la Variable
```bash
# Test de l'API après configuration
curl -X POST https://votre-site.netlify.app/.netlify/functions/api \
  -H "Content-Type: application/json" \
  -d '{"message": "Qui es-tu ?"}'
```

### Test 2 : Test Local avec Variable
```bash
# Définir la variable localement
export GOOGLE_API_KEY="AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y"

# Tester l'API
node test_netlify.js
```

## 🔍 Vérification des Logs

### Voir les Logs Netlify
1. **Dans Netlify**, allez dans **"Functions"**
2. **Cliquez** sur **"api"**
3. **Vérifiez** les logs pour voir les erreurs

### Logs Attendus (Après Configuration)
```
🚀 Handler appelé avec méthode: POST
📨 Message reçu: Qui es-tu ?
🤖 Génération de réponse pour: Qui es-tu ?
✅ Réponse générée: Je suis l'assistant IA d'Abdelilah Ourti...
📤 Réponse envoyée
```

## 🚨 Erreurs Possibles

### Erreur 1 : Variable non trouvée
```
❌ Erreur: GOOGLE_API_KEY non configurée
```
**Solution** : Vérifiez que la variable est bien ajoutée dans Netlify

### Erreur 2 : Clé API invalide
```
❌ Erreur: Erreur API: 401 - Unauthorized
```
**Solution** : Vérifiez que la clé API est correcte

### Erreur 3 : Redéploiement nécessaire
```
❌ Erreur: Variable d'environnement non disponible
```
**Solution** : Redéployez le site après avoir ajouté la variable

## 📱 Interface Utilisateur Netlify

### Capture d'Écran de Configuration

```
Site settings > Environment variables
┌─────────────────────────────────────┐
│ Add a variable                      │
├─────────────────────────────────────┤
│ Key:    GOOGLE_API_KEY              │
│ Value:  AIzaSyAESAzLncervSl2KLwRhMwy2Yu5151lG5Y │
│         [Save]                      │
└─────────────────────────────────────┘
```

## 🎯 Résultat Attendu

Après configuration :
- ✅ **Variable configurée** dans Netlify
- ✅ **Redéploiement** automatique
- ✅ **API fonctionnelle** avec la clé
- ✅ **Chatbot opérationnel**

## 🆘 Support

### Si la configuration ne fonctionne pas

1. **Vérifiez** que la variable est bien ajoutée
2. **Redéployez** manuellement le site
3. **Vérifiez** les logs des fonctions
4. **Testez** avec une requête curl

### Commandes de Debug
```bash
# Vérifier les variables d'environnement
netlify env:list

# Voir les logs en temps réel
netlify logs --tail

# Tester la fonction localement
netlify dev
```

---

**Une fois la variable `GOOGLE_API_KEY` configurée dans Netlify, votre chatbot devrait fonctionner parfaitement ! 🚀** 