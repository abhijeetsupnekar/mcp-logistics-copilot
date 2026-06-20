def send_notification(
    recipient: str,
    message: str
):
    return {
        "status": "success",
        "recipient": recipient,
        "message": message,
        "result": "Notification sent"
    }