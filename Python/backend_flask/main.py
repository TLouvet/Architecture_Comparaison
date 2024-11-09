from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .flaskenv
load_dotenv()
app = Flask(__name__)

# Les CORS pour permettre à notre front de se connecter
CORS(app, resources={r"/*": {"origins": "*"}})

# Importer et enregistrer les blueprints des contrôleurs
from controllers.author_controller import author_bp
from controllers.user_controller import user_bp

# Enregistrer les blueprints pour chaque contrôleur
app.register_blueprint(author_bp)
app.register_blueprint(user_bp)


# Route de base pour vérifier que l'API est en ligne
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="API is live!")