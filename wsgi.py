import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire web au chemin
web_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'web'))
sys.path.insert(0, web_path)

# Charger les variables d'environnement
load_dotenv()

# Importer l'application Flask
from api import app

# Variable pour Gunicorn (Render)
application = app

# Configuration pour Vercel
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 