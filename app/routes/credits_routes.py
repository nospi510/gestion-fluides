from flask import Blueprint, render_template

bp = Blueprint('credits_routes', __name__, url_prefix='/credits')

@bp.route('/')
def credits():
    """Affiche la page des crédits."""
    return render_template('credits.html')
