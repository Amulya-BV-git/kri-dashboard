 main
from flask_talisman import Talisman
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask import Flask, request, jsonify
from sanitizer import sanitize_input

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
Talisman(app)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)
@app.route('/')
def home():
    return "API is running"

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# Connect middleware
app.before_request(sanitize_input)

# Test API
@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    return jsonify({
        "message": "Input received successfully",
        "data": data
    })

@app.route('/generate-report', methods=['POST'])
@jwt_required()
@limiter.limit("10 per minute")
def generate_report():
    data = request.get_json()
    return jsonify({
        "message": "Report generated successfully",
        "data": data
    })

# Error handler
@app.errorhandler(429)
def rate_limit_exceeded(e):
    return jsonify({
        "error": "Too many requests",
        "retry_after": str(e.description)
    }), 429

if __name__ == '__main__':
    app.run(debug=True)
    @app.after_request
    def add_security_headers(response):
     response.headers['X-Content-Type-Options'] = 'nosniff'
     response.headers['X-Frame-Options'] = 'DENY'
     return response
=======
from flask import Flask
from flask_cors import CORS

from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp
from routes.analyse_document import analyse_bp
from routes.batch_process import batch_bp
from routes.rag import rag_bp

try:
    from services.embedding_service import load_model
except:
    def load_model():
        print(" Embedding model not found, skipping preload")


app = Flask(__name__)
CORS(app)


app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)
app.register_blueprint(analyse_bp)
app.register_blueprint(batch_bp)
app.register_blueprint(rag_bp)

@app.route("/")
def home():
    return {
        "status": "running",
        "message": "AI Service is up "
    }


if __name__ == "__main__":
    load_model()  # preload model (optional)
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5555, debug=True)
 main
