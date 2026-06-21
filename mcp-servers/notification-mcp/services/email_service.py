import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"

print("ENV FILE =", env_path)

load_dotenv(env_path)

def send_email(
    recipient: str,
    subject: str,
    message: str

    
):
    
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))

    sender_email = os.getenv("SMTP_EMAIL")
    sender_password = os.getenv("SMTP_PASSWORD")
   

    try:
        msg = MIMEMultipart()

        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(
            MIMEText(
                message,
                "plain"
            )
        )

        server = smtplib.SMTP(
            smtp_server,
            smtp_port
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            recipient,
            msg.as_string()
        )

        server.quit()

        return {
            "status": "success",
            "message": f"Email sent to {recipient}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }