from flask import Flask, request, render_template_string
import logging
from datetime import datetime

app = Flask(__name__)

# Configurer le logging dans un fichier
logging.basicConfig(
    filename="flask_visitors.log",
    level=logging.INFO,
    format='%(asctime)s | IP=%(ip)s | Path=%(path)s | Method=%(method)s | User-Agent=%(ua)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Fonction utilitaire pour logger les visiteurs
def log_visitor():
    ip = request.remote_addr or "unknown"
    path = request.path
    method = request.method
    ua = request.headers.get("User-Agent", "Unknown")
    logging.info("", extra={"ip": ip, "path": path, "method": method, "ua": ua})

@app.before_request
def before_request_logging():
    log_visitor()

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AWS ODC 5</title>
        <style>
            body {display:flex; justify-content:center; align-items:center; height:100vh; font-family:Arial;}
            h1 {color:#0073bb; font-size:4em;}
        </style>
    </head>
    <body>
        <h1>AWS-ODC-5</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

