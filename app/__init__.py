from flask import Flask, render_template
from .main import main as main_blueprint
from .api import api as api_blueprint
from .auth import auth as auth_blueprint
from flask_login import LoginManager

def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ashdfgaksjdhfg'
    app.register_error_handler(404, page_not_found)

    # LOGIN MANAGER
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return None

    # REGISTER BLUEPRINTS
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app