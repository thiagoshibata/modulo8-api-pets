from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

#importando blueprints
from src.main.routes.pets_routes import pets_route_bp
from src.main.routes.people_routes import person_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pets_route_bp)
app.register_blueprint(person_route_bp)
