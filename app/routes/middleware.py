from flask import session, redirect, url_for, flash
from functools import wraps

def role_required(allowed_roles):
    """
    Middleware pour restreindre l'accès à certaines routes en fonction du rôle de l'utilisateur.
    :param allowed_roles: Liste des rôles autorisés['technicien', 'ingenieur']).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Vérification de l'authentification
            if 'role' not in session:
                flash("Vous devez être connecté pour accéder à cette page.", "danger")
                return redirect(url_for('auth_routes.login'))

            # Vérification du rôle
            user_role = session.get('role')
            if user_role not in allowed_roles:
                flash("Vous n'avez pas l'autorisation pour cette action.", "danger")
                return redirect(url_for('index.index'))

            return func(*args, **kwargs)
        return wrapper
    return decorator
