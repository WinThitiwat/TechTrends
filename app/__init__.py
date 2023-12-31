from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from config import Config

def create_app(config_class=Config):
    # Define the Flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    @app.route("/test/")
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>' 
    
    return app

