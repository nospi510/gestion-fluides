import sys
import os

# Ajouter le répertoire du projet au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User

# Créer une instance de l'application Flask
app = create_app()

# Fonction pour créer un utilisateur test
def create_test_user():
    with app.app_context():
        # Vérifier si l'utilisateur test existe déjà
        if User.query.filter_by(username='test').first():
            print("L'utilisateur 'test' existe déjà.")
            return
        
        # Créer un nouvel utilisateur
        new_user = User(username='test', name='test', role='ingenieur')
        new_user.set_password('test')  # Utilisation de la méthode pour hacher le mot de passe

        # Ajouter et valider l'utilisateur
        db.session.add(new_user)
        db.session.commit()
        
        print("Utilisateur 'test' créé avec succès.")

if __name__ == '__main__':
    create_test_user()
