import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from tools.traffic import get_route_traffic


result = get_route_traffic(
    18.5204,
    73.8567,
    18.9220,
    72.8347
)

print(result)