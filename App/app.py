from flask import Flask
from datetime import datetime
import os
from App.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    
    # Configuration
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config.update(
        SECRET_KEY='supersecretkey',
        UPLOAD_FOLDER=os.path.join(base_dir, 'uploads'),
        MAX_CONTENT_LENGTH=128 * 1024 * 1024
    )

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register context processors
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # Register blueprints
    register_blueprints(app)

    return app

# Create the application instance
app = create_app()
