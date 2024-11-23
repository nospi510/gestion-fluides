from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration de la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://nick:passer@localhost:3306/fluide_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation de l'extension SQLAlchemy
    db.init_app(app)

    # Importer et enregistrer les blueprints à l'intérieur de create_app
    from .routes.data_routes import bp as data_bp
    from .routes.image_routes import bp as image_bp
    from .routes.report_routes import bp as report_bp
    from .routes.credits_routes import bp as credits_bp
    from .routes.routes import bp as index_bp  

    app.register_blueprint(data_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(credits_bp)
    app.register_blueprint(index_bp) 

    # Création des tables si elles n'existent pas
    with app.app_context():
        db.create_all()

    return app
