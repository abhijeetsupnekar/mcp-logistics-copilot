from services.email_service import send_email


def send_notification(
    recipient: str,
    message: str
):
    return send_email(
        recipient=recipient,
        subject="Logistics Copilot Notification",
        message=message
    )