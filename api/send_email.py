from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Health check endpoint
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "active",
        "service": "Bird Rescue API",
        "endpoints": {
            "POST /api/send_email": "Send email to rescuers"
        }
    })

# Email sending endpoint
@app.route('/api/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        # SMTP Configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "perozhizni@gmail.com"
        sender_password = "bmzo ggza nxuv biqc"  # App password
        
        # Create message
        msg = MIMEText(data.get("message", ""))
        msg["Subject"] = data.get("subject", "Bird Rescue Request")
        msg["From"] = sender_email
        msg["To"] = data.get("to", "pozitivgame88@gmail.com")
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        return jsonify({"status": "success"}), 200
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run()