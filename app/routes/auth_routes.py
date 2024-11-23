from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from app.models import db, User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['role'] = user.role
            session['name'] = user.name  
            flash('Connexion réussie.', 'success')
            return redirect(url_for('index.index'))
        else:
            flash('Identifiant ou mot de passe incorrect.', 'danger')

    return render_template('auth/login.html')

@auth_routes.route('/logout')
def logout():
    session.clear()
    flash('Déconnexion réussie.', 'success')
    return redirect(url_for('auth_routes.login'))

@auth_routes.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        role = request.form.get('role')

        if User.query.filter_by(username=username).first():
            flash('Cet identifiant est déjà utilisé.', 'danger')
        else:
            new_user = User(username=username, name=name, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Utilisateur créé avec succès.', 'success')
            return redirect(url_for('auth_routes.login'))

    return render_template('auth/create_user.html')
