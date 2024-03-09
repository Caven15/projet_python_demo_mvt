from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from config import SECRET_KEY, URL_DB

from app.models.db.db_model import Base
from app.models.db.db_model import User

# Initialisation de l'application Flask
app = Flask(__name__)

# Mettre en place une session SQLAlchemy
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB

login_manager = LoginManager()
login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))

# Initialisation de CSRFProtect pour la protection contre les attaques CSRF
csrf = CSRFProtect(app)

# Définir la variable pour vérifier la connexion à la base de données
db_connected = False

# Essayer de se connecter à la base de données
try:
    # Initialisation de SQLAlchemy avec l'application Flask
    db = SQLAlchemy(app)
    
    # Création d'un moteur de base de données SQLAlchemy à partir de l'URL de la base de données
    engine = create_engine(URL_DB)
    
    # Récupération des métadonnées de la base de données à partir du modèle de données Base
    metadata = Base.metadata
    
    # Marquer la connexion à la base de données comme établie
    db_connected = True
except SQLAlchemyError as e:
    # En cas d'erreur SQLAlchemy, afficher un message d'erreur
    print(f"Erreur de connexion à la base de données : \n {e}")

if db_connected:
    # permet de supprimer et de recréer la base de donnée.
    # metadata.drop_all(bind=engine)
    # metadata.create_all(bind=engine)
    
    from app.routes import other, auth, task, user
    
    print('----------------------')
    print("Connexion db établie !")
    print('----------------------')
