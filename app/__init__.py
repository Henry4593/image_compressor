from flask import Flask
from app.utils.db_utils import DatabaseUtil
from flask_cors import CORS
from app.utils.logging_utils import init_logging
import os


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("APP_SECRET_KEY")
    CORS(app)
    # Configure logging
    from .routes.auth_routes import auth
    from .routes.main_routes import main
    from .routes.compression_routes import compress
    from .utils.image_utils import CompressImage

    init_logging(app)
    app.logger.info("Creating the database...")
    handle_database = DatabaseUtil()
    handle_database.create_database()
    app.logger.info("Connecting to the database...")
    handle_database.connect()
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(compress)

    app.config["CURRENT_USER"] = ""
    app.logger.info("Blueprints registered and app configured.")

    return app

