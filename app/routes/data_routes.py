from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .. import db
from app.models import FluidData
from datetime import datetime
from app.routes.middleware import role_required

bp = Blueprint('data_routes', __name__, url_prefix='/data')


@bp.route('/', methods=['GET'])
@role_required(['technicien', 'ingenieur'])
def get_all_data():
    """Affiche la liste de toutes les données fluides."""
    data = FluidData.query.all()
    return render_template('data/list.html', data=data)

@bp.route('/<int:id>', methods=['GET'])
@role_required(['technicien', 'ingenieur'])
def get_data_details(id):
    """Affiche les détails d'une donnée fluide spécifique."""
    data = FluidData.query.get_or_404(id)
    return render_template('data/detail.html', data=data)

@bp.route('/create', methods=['GET', 'POST'])
@role_required(['technicien', 'ingenieur'])
def create_data():
    """Crée une nouvelle donnée fluide."""
    if request.method == 'POST':
        date = request.form.get('date')
        debit_list = request.form.getlist('debit')  # Récupère toutes les valeurs de débit
        pression_list = request.form.getlist('pression')  # Récupère toutes les valeurs de pression

        if not debit_list or not pression_list:
            return render_template('data/create.html', error="Le débit et la pression sont obligatoires.")
        
        if len(debit_list) != len(pression_list):
            return render_template('data/create.html', error="Le nombre de débits et de pressions ne correspond pas.")

        # Création des nouveaux enregistrements
        for debit, pression in zip(debit_list, pression_list):
            new_data = FluidData(
                date=datetime.strptime(date, '%Y-%m-%dT%H:%M') if date else datetime.utcnow(),
                debit=float(debit),
                pression=float(pression)
            )
            db.session.add(new_data)
        
        db.session.commit()
        return redirect(url_for('data_routes.get_all_data'))

    # Calculer la date actuelle pour pré-remplir le champ
    today_date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M')
    return render_template('data/create.html', today_date=today_date)


@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@role_required(['ingenieur'])
def edit_data(id):
    """Modifie les informations d'une donnée fluide existante."""
    data = FluidData.query.get_or_404(id)
    
    if request.method == 'POST':
        # Correction du format de la date
        if request.form.get('date'):
            data.date = datetime.strptime(request.form.get('date'), '%Y-%m-%dT%H:%M')
        data.debit = float(request.form.get('debit'))
        data.pression = float(request.form.get('pression'))
        db.session.commit()
        return redirect(url_for('data_routes.get_data_details', id=data.id))
    
    return render_template('data/edit.html', data=data)

@bp.route('/<int:id>/delete', methods=['POST'])
@role_required(['ingenieur'])
def delete_data(id):
    """Supprime une donnée fluide."""
    data = FluidData.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": f"Donnée fluide {id} supprimée avec succès."}), 200
