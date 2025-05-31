from flask import jsonify

def handler(request):
    return jsonify({'status': 'ok', 'message': 'Server is running'})