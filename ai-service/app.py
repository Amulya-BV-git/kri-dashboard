from flask import Flask, request, jsonify
from sanitizer import sanitize_input

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
@app.route('/')
def home():
    return "API is running"

@app.route('/health')
def health():
    return {"status": "ok"}

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
