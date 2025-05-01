import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .extensions import api, db, migrate, bcrypt, jwt
from .routes import profile_ns, login_ns, search_ns, history_ns

# Load environment variables from .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_key")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable modification tracking for performance

    # Enable Debug mode (can also use `FLASK_ENV=development` in terminal)
    app.config['DEBUG'] = True  # Add this line to enable debug mode programmatically

    # Validate configurations to make sure necessary settings are available
    if not app.config['SQLALCHEMY_DATABASE_URI']:
        raise RuntimeError("DATABASE_URI is not set in environment variables. Please check your .env file.")
    
    if not app.config["JWT_SECRET_KEY"]:
        raise RuntimeError("JWT_SECRET_KEY is not set in environment variables. Please check your .env file.")

    # Initialize Extensions (API, Database, Migrations, etc.)
    api.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Add Namespaces to the API (Define routes and views)
    api.add_namespace(profile_ns)
    api.add_namespace(login_ns)
    api.add_namespace(search_ns)
    api.add_namespace(history_ns)

    return app
