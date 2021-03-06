from flask_cors import CORS

from app import app
from app.constants import Config
from app.factories.database import init_db_app
from app.factories.mail import init_mail_app
from app.utils import fill_database

if __name__ == '__main__':
    app.config.from_object(Config())
    init_db_app(app)
    init_mail_app(app)
    with app.app_context():
        fill_database()
    CORS(app)
    app.run()
