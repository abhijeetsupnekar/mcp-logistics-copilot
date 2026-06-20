import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.send_notification import send_notification

result = send_notification(
    "Abhijeet",
    "Truck reached warehouse"
)

print(result)