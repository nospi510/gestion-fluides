from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.models import Report, db

bp = Blueprint('report_routes', __name__, url_prefix='/reports')

@bp.route('/', methods=['GET'])
def get_all_reports():
    """Affiche la liste de tous les rapports."""
    reports = Report.query.all()
    return render_template('reports/list.html', reports=reports)

@bp.route('/<int:id>', methods=['GET'])
def get_report_details(id):
    """Affiche les détails d'un rapport spécifique."""
    report = Report.query.get_or_404(id)
    return render_template('reports/detail.html', report=report)

@bp.route('/create', methods=['GET', 'POST'])
def create_report():
    """Crée un nouveau rapport."""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        observations = request.form.get('observations')
        if not title or not content:
            return render_template('reports/create.html', error="Titre et contenu sont obligatoires.")
        
        new_report = Report(title=title, content=content, observations=observations)
        db.session.add(new_report)
        db.session.commit()
        return redirect(url_for('report_routes.get_all_reports'))
    
    return render_template('reports/create.html')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_report(id):
    """Modifie les informations d'un rapport existant."""
    report = Report.query.get_or_404(id)
    if request.method == 'POST':
        report.title = request.form.get('title')
        report.content = request.form.get('content')
        report.observations = request.form.get('observations')
        db.session.commit()
        return redirect(url_for('report_routes.get_report_details', id=id))
    
    return render_template('reports/edit.html', report=report)

@bp.route('/<int:id>/delete', methods=['POST'])
def delete_report(id):
    """Supprime un rapport."""
    report = Report.query.get_or_404(id)
    db.session.delete(report)
    db.session.commit()
    return jsonify({"message": f"Rapport {id} supprimé avec succès."}), 200
