# Architecture Vercel Optimisée

## 🏗️ Vue d'ensemble

Cette architecture résout le problème de taille de déploiement (>250MB) en utilisant une approche serverless pure.

## 📁 Structure des fichiers

```
portfolio/
├── api/
│   ├── chat.py              # API serverless Vercel
│   └── requirements.txt     # Dépendances minimales
├── index.html              # Frontend statique
├── vercel.json             # Configuration Vercel
├── .vercelignore           # Fichiers à ignorer
└── [autres fichiers...]    # Fichiers Render (conservés)
```

## 🔧 Composants

### 1. API Serverless (`api/chat.py`)
- **Taille** : ~5MB (vs 250MB précédent)
- **Dépendances** : Seulement `google-generativeai`
- **Fonctionnalité** : Chatbot avec contexte intégré
- **Endpoint** : `/api/chat`

### 2. Frontend (`index.html`)
- **Type** : Statique (pas de serveur)
- **API** : Appelle `/api/chat`
- **Interface** : Chatbot intégré

### 3. Configuration (`vercel.json`)
```json
{
  "version": 2,
  "functions": {
    "api/chat.py": {
      "runtime": "python3.9"
    }
  },
  "routes": [
    {
      "src": "/api/chat",
      "dest": "/api/chat.py"
    },
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

## 🚀 Avantages

### Performance
- ✅ **Déploiement rapide** (~5MB vs 250MB)
- ✅ **Cold start rapide** (pas de Flask)
- ✅ **Scalabilité automatique**

### Simplicité
- ✅ **Moins de dépendances**
- ✅ **Pas de serveur web**
- ✅ **Configuration minimale**

### Compatibilité
- ✅ **Fichiers Render conservés**
- ✅ **Fonctionne sur Vercel ET Render**
- ✅ **API identique**

## 🔄 Migration depuis l'ancienne architecture

### Avant (Flask)
```python
# wsgi.py + web/api.py + chatbot_logic.py
# Taille: ~250MB
# Dépendances: Flask, LangChain, FAISS, etc.
```

### Après (Serverless)
```python
# api/chat.py
# Taille: ~5MB
# Dépendances: google-generativeai seulement
```

## 🧪 Tests

### Test local
```bash
python -c "from api.chat import generate_response; print(generate_response('Qui es-tu ?'))"
```

### Test API
```bash
python test_vercel_api.py
```

## 📊 Comparaison

| Aspect | Ancienne | Nouvelle |
|--------|----------|----------|
| Taille | ~250MB | ~5MB |
| Dépendances | 10+ | 1 |
| Démarrage | Lent | Rapide |
| Complexité | Élevée | Faible |
| Maintenance | Difficile | Facile |

## 🎯 Résultat

- **Problème résolu** : Plus d'erreur de taille >250MB
- **Performance améliorée** : Déploiement et démarrage plus rapides
- **Maintenance simplifiée** : Moins de dépendances à gérer
- **Fonctionnalité identique** : Chatbot fonctionne parfaitement

---

**Cette architecture est optimale pour Vercel ! 🚀** 