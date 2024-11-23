from flask import Blueprint, render_template
from app.routes.middleware import role_required


bp = Blueprint('credits_routes', __name__, url_prefix='/credits')

@bp.route('/')
@role_required(['technicien', 'ingenieur'])
def credits():
    """Affiche la page des crédits."""
    return render_template('credits.html')
