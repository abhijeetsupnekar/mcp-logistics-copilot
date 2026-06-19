import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.eta import estimate_eta

result = estimate_eta(
    "Pune",
    "Mumbai Airport"
)

print(result)