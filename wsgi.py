import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire web au chemin
web_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'web'))
sys.path.insert(0, web_path)

# Charger les variables d'environnement
load_dotenv()

try:
    # Importer l'application Flask
    from api import app
    print("✅ Flask app imported successfully")
except ImportError as e:
    print(f"❌ Error importing Flask app: {e}")
    sys.exit(1)

# Variable pour Gunicorn
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 