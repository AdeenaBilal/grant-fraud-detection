# app.py
from flask import Flask
from flask_cors import CORS
from upload_grantee import upload_grantees_bp
from upload_application import upload_application_bp

#from routes.upload_applications import upload_applications_bp

app = Flask(__name__)
CORS(app)  # <-- THIS LINE IS REQUIRED

#app.register_blueprint(upload_grantees_bp)
app.register_blueprint(upload_grantees_bp, url_prefix="/api")
app.register_blueprint(upload_application_bp, url_prefix="/api")

#app.register_blueprint(upload_applications_bp)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
