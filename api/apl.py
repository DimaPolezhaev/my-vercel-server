from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'running',
        'message': 'Сервер для отправки email работает',
        'endpoints': {
            'POST /api/send_email': 'Отправка email'
        }
    })

if __name__ == '__main__':
    app.run()