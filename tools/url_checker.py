import requests
from google.adk.tools import FunctionTool

def check_url(url: str):
    """Checks if a URL is reachable."""
    try:
        response = requests.get(url, timeout=5)
        return {
            "ok": True,
            "status_code": response.status_code,
            "final_url": response.url
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}

url_checker_tool = FunctionTool(func=check_url)
