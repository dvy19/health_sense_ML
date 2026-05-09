from flask import Flask
import os
import sys



from routes.disease_routes import disease_bp

app = Flask(__name__)
app.register_blueprint(disease_bp)


