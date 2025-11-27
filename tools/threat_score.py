from google.adk.tools import FunctionTool

def threat_score(url_result: dict, malware_result: dict, phishing_result: dict):
    """Combines tool results into a score."""
    score = 0

    if not url_result.get("ok"):
        score += 2
    if malware_result.get("malware"):
        score += 5
    if phishing_result.get("phishing"):
        score += len(phishing_result["matches"])

    return {"score": score}

threat_score_tool = FunctionTool(func=threat_score)
