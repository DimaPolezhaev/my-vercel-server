import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/api/send_email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        
        # Конфигурация SMTP для Gmail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_user = 'perozhizni@gmail.com'
        email_password = 'bmzo ggza nxuv biqc'  # Пароль приложения
        
        # Формирование письма
        msg = MIMEText(data.get('message', ''), 'plain', 'utf-8')
        msg['Subject'] = data.get('subject', 'Запрос на помощь птице')
        msg['From'] = email_user
        msg['To'] = data.get('to', 'pozitivgame88@gmail.com')
        
        # Отправка письма
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
        
        return jsonify({'status': 'success'}), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run()