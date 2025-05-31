from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Конфигурация Gmail (пароль С ПРОБЕЛАМИ!)
GMAIL_USER = "perozhizni@gmail.com"
GMAIL_APP_PASSWORD = "bmzo ggza nxuv biqc"  # Пароль приложения (пробелы важны!)

@app.route('/')
def home():
    return jsonify({"status": "OK", "service": "Bird Rescue API"})

@app.route('/api/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        # Создаём письмо
        msg = MIMEText(data.get("message", ""))
        msg["Subject"] = data.get("subject", "Bird Rescue Alert")
        msg["From"] = GMAIL_USER
        msg["To"] = data.get("to", "pozitivgame88@gmail.com")
        
        # Отправка через SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)  # Пароль с пробелами!
            server.send_message(msg)
        
        return jsonify({"status": "success"}), 200
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run()