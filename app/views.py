from app import app
from flask import render_template, jsonify, request


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/copymail', methods=['POST'])
def handle_ajax():
    file = request.files['file']
    file_type = type(file)

    res = {
        'status': 'WHATEVER',
        'file_type': str(file_type)
    }

    return jsonify(res)
