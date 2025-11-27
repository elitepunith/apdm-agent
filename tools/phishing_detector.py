from google.adk.tools import FunctionTool

PHISHING_KEYWORDS = [
    "verify your account",
    "password",
    "act now",
    "urgent",
    "your account will be closed"
]

def check_phishing(message: str):
    """Detects phishing indicators based on keywords."""
    matches = [k for k in PHISHING_KEYWORDS if k in message.lower()]
    return {
        "phishing": len(matches) > 0,
        "matches": matches
    }

phishing_detector_tool = FunctionTool(func=check_phishing)
