import os
import smtplib
from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
load_dotenv()  # для локального запуска

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.json
    recipient = data.get("to")
    subject = data.get("subject", "Сообщение от приложения")
    message = data.get("message", "")

    email_host = os.getenv("EMAIL_HOST")
    email_port = int(os.getenv("EMAIL_PORT"))
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)
        server.quit()
        return jsonify({"success": True, "message": "Письмо отправлено"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
