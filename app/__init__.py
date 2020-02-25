from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads

from config import DevConfig

db = SQLAlchemy()
images = UploadSet('images', IMAGES)


def create_app(config_class=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    configure_uploads(app, images)

    from app.models import Profile
    with app.app_context():
        db.create_all()

    from app.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app
