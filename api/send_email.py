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
        
        # Получаем данные из запроса
        to_email = data.get('to', 'pozitivgame88@gmail.com')  # Ваш email по умолчанию
        subject = data.get('subject', 'Запрос на помощь птице')
        message = data.get('message', '')
        
        # Настройки SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_user = os.getenv('EMAIL_USER')
        email_password = os.getenv('EMAIL_PASSWORD')
        
        # Формируем письмо
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = email_user
        msg['To'] = to_email
        
        # Отправка
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
        
        return jsonify({'status': 'success', 'message': 'Email sent successfully'}), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run()