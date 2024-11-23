from flask import Blueprint, render_template

# Créer un Blueprint pour l'accueil
bp = Blueprint('index', __name__)

# Définir une route pour la page d'accueil
@bp.route('/')
def index():
    return render_template('index.html')
