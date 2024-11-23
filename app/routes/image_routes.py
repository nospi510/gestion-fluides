from flask import Blueprint, request, jsonify, send_from_directory, render_template, redirect, url_for
from app.models import Image, db
import os
from app.routes.middleware import role_required

bp = Blueprint('image_routes', __name__, url_prefix='/images')

UPLOAD_FOLDER = 'app/static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route('/', methods=['GET'])
@role_required(['technicien', 'ingenieur'])
def get_all_images():
    """Affiche la liste de toutes les images."""
    images = Image.query.all()
    return render_template('images/list.html', images=images)

@bp.route('/<int:id>', methods=['GET'])
@role_required(['technicien', 'ingenieur'])
def get_image_details(id):
    """Affiche les détails d'une image spécifique."""
    image = Image.query.get_or_404(id)
    return render_template('images/detail.html', image=image)

@bp.route('/upload', methods=['GET', 'POST'])
@role_required(['technicien', 'ingenieur'])
def upload_image():
    """Téléverse une nouvelle image."""
    if request.method == 'POST':
        file = request.files.get('image')
        if not file or file.filename == '':
            return render_template('images/upload.html', error="Aucun fichier sélectionné.")
        
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        new_image = Image(filename=file.filename)
        db.session.add(new_image)
        db.session.commit()
        return redirect(url_for('image_routes.get_all_images'))
    
    return render_template('images/upload.html')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@role_required(['ingenieur'])
def edit_image(id):
    """Modifie les informations d'une image existante."""
    image = Image.query.get_or_404(id)
    if request.method == 'POST':
        new_filename = request.form.get('filename')
        if new_filename and new_filename != image.filename:
            old_filepath = os.path.join(UPLOAD_FOLDER, image.filename)
            new_filepath = os.path.join(UPLOAD_FOLDER, new_filename)
            if os.path.exists(old_filepath):
                os.rename(old_filepath, new_filepath)
            image.filename = new_filename
        
        db.session.commit()
        return redirect(url_for('image_routes.get_image_details', id=id))
    
    return render_template('images/edit.html', image=image)

@bp.route('/<int:id>/delete', methods=['POST'])
@role_required(['ingenieur'])
def delete_image(id):
    """Supprime une image."""
    image = Image.query.get_or_404(id)
    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": f"Image {id} supprimée avec succès."}), 200
