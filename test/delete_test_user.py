import sys
import os

# Ajouter le répertoire du projet au chemin d'importation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User

# Créer une instance de l'application Flask
app = create_app()

# Fonction pour supprimer l'utilisateur test
def delete_test_user():
    with app.app_context():
        # Chercher l'utilisateur test
        user = User.query.filter_by(username='test').first()
        
        if not user:
            print("L'utilisateur 'test' n'existe pas.")
            return
        
        # Supprimer l'utilisateur
        db.session.delete(user)
        db.session.commit()
        
        print("Utilisateur 'test' supprimé avec succès.")

if __name__ == '__main__':
    delete_test_user()
