import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)
from services.email_service import send_email
from services.email_service import send_email
import inspect

print("MODULE:", send_email.__module__)
print("FILE:", inspect.getfile(send_email))

print(send_email)
print(send_email.__module__)
result = send_email(
    recipient="abhimsupnekar@gmail.com",
    subject="SMTP Test",
    message="Hello from Notification MCP"
)

print(result)