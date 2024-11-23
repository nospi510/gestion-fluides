from flask import Blueprint, render_template
from app.routes.middleware import role_required


# Créer un Blueprint pour l'accueil
bp = Blueprint('index', __name__)

# Définir une route pour la page d'accueil
@bp.route('/')
@role_required(['technicien', 'ingenieur'])
def index():
    return render_template('index.html')
