from flask import Flask, render_template
import secrets


def page_not_found():
    return render_template('404.html'), 404





def create_app():
    # Import der Routen
    from app.routes.main import bp_main
    
    # Erstellung der Flask-App
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.secret_key = secrets.token_hex(16)
    
    # Registrierung der Routen
    app.register_blueprint(bp_main)
    app.register_error_handler(404, page_not_found)
    
    
    return app