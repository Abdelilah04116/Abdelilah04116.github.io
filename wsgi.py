import os
import sys
from dotenv import load_dotenv

# Ajouter le répertoire web au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'web')))

# Charger les variables d'environnement
load_dotenv()

# Importer l'application Flask
from api import app

if __name__ == "__main__":
    app.run() 