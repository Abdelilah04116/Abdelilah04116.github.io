# Script de déploiement Vercel pour Windows PowerShell
Write-Host "🚀 Déploiement Vercel - Portfolio avec Chatbot" -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green

# Vérifier si Vercel CLI est installé
try {
    $vercelVersion = vercel --version
    Write-Host "✅ Vercel CLI installé: $vercelVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Vercel CLI n'est pas installé" -ForegroundColor Red
    Write-Host "📦 Installation de Vercel CLI..." -ForegroundColor Yellow
    npm install -g vercel
}

# Vérifier la configuration
Write-Host "🧪 Test de la configuration..." -ForegroundColor Yellow
python test-vercel-deployment.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Configuration invalide. Veuillez corriger les erreurs." -ForegroundColor Red
    exit 1
}

# Vérifier si on est connecté à Vercel
Write-Host "🔐 Vérification de la connexion Vercel..." -ForegroundColor Yellow
try {
    vercel whoami | Out-Null
    Write-Host "✅ Connecté à Vercel" -ForegroundColor Green
} catch {
    Write-Host "🔑 Connexion à Vercel..." -ForegroundColor Yellow
    vercel login
}

# Déploiement
Write-Host "🚀 Déploiement en cours..." -ForegroundColor Yellow
vercel --prod

Write-Host "✅ Déploiement terminé!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 URLs de votre projet:" -ForegroundColor Cyan
Write-Host "   - Production: https://votre-projet.vercel.app" -ForegroundColor White
Write-Host "   - API: https://votre-projet.vercel.app/api/chat" -ForegroundColor White
Write-Host ""
Write-Host "🔧 Pour vérifier le déploiement:" -ForegroundColor Cyan
Write-Host "   curl https://votre-projet.vercel.app/api/health" -ForegroundColor White
Write-Host ""
Write-Host "📊 Dashboard: https://vercel.com/dashboard" -ForegroundColor Cyan 