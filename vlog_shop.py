from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')
from flask_cors import CORS
CORS(app, resources=r'/*')


# Serve index.html
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Serve static files
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Run the Flask app, 使用gunicorn
    # gunicorn -w 4 --bind 0.0.0.0:6612 vlog_shop:app
    app.run(host='0.0.0.0', port=6612)
    