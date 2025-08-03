# Guide de Dépannage Vercel

## 🚨 Erreurs Courantes et Solutions

### 1. BODY_NOT_A_STRING_FROM_FUNCTION (502)
**Cause** : La fonction ne retourne pas une réponse valide
**Solution** : Utiliser `api/chat_simple.py` avec la syntaxe Vercel Functions standard

### 2. FUNCTION_INVOCATION_FAILED (500)
**Cause** : Erreur dans le code de la fonction
**Solution** : Vérifier les logs dans le dashboard Vercel

### 3. FUNCTION_INVOCATION_TIMEOUT (504)
**Cause** : La fonction prend trop de temps (>10 secondes)
**Solution** : Optimiser le code, réduire la complexité

### 4. FUNCTION_PAYLOAD_TOO_LARGE (413)
**Cause** : Le payload de la requête est trop volumineux
**Solution** : Réduire la taille des données envoyées

## 🔧 Solutions par Erreur

### Erreur 502 - BODY_NOT_A_STRING_FROM_FUNCTION
```python
# ❌ Incorrect
def handler(request, response):
    response.body = None  # ou pas de body

# ✅ Correct
def handler(request, response):
    response.body = json.dumps({'response': 'test'})
```

### Erreur 500 - FUNCTION_INVOCATION_FAILED
```python
# ❌ Incorrect
def handler(request, response):
    raise Exception("Erreur non gérée")

# ✅ Correct
def handler(request, response):
    try:
        # Code de la fonction
        response.body = json.dumps({'response': 'success'})
    except Exception as e:
        response.status = 500
        response.body = json.dumps({'error': str(e)})
```

### Erreur 504 - FUNCTION_INVOCATION_TIMEOUT
```python
# ❌ Trop lent
def slow_function():
    time.sleep(15)  # > 10 secondes

# ✅ Optimisé
def fast_function():
    # Code optimisé
    return result
```

## 🧪 Tests Locaux

### Test de l'API Simple
```bash
python test_simple_api.py
```

### Test du Handler
```bash
python -c "
from api.chat_simple import handler
# Test manuel du handler
"
```

## 📊 Logs Vercel

### Voir les logs
1. **Dashboard Vercel** → Projet → Functions → Logs
2. **CLI** : `vercel logs`

### Logs utiles
```bash
# Logs en temps réel
vercel logs --follow

# Logs d'une fonction spécifique
vercel logs --function=api/chat_simple.py
```

## 🔄 Solutions de Contournement

### 1. Version Ultra-Simple
Si l'API complexe ne fonctionne pas, utiliser `api/chat_simple.py`

### 2. Test en Local
Toujours tester en local avant de déployer :
```bash
python test_simple_api.py
```

### 3. Variables d'Environnement
Vérifier que `GOOGLE_API_KEY` est configurée dans Vercel

## 📋 Checklist de Déploiement

- [ ] Code testé en local
- [ ] Variables d'environnement configurées
- [ ] Fichier `vercel.json` correct
- [ ] Dépendances minimales dans `requirements.txt`
- [ ] Handler retourne une réponse valide
- [ ] Gestion d'erreurs implémentée

## 🆘 Support

### Si rien ne fonctionne
1. **Vérifier les logs** Vercel
2. **Tester en local** avec `test_simple_api.py`
3. **Simplifier le code** au maximum
4. **Utiliser la version simple** `api/chat_simple.py`

### Contact
- **Documentation Vercel** : https://vercel.com/docs
- **Support Vercel** : https://vercel.com/support

---

**Cette architecture simple devrait résoudre tous les problèmes Vercel ! 🚀** 