from dotenv import load_dotenv
from server import mcp
load_dotenv()


app = mcp.streamable_http_app()