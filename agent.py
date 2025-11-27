from google.adk.agents import Agent
from google.adk.models import Gemini

from tools import (
    url_checker_tool,
    phishing_detector_tool,
    malware_detector_tool,
    threat_score_tool,
)

coordinator_agent = Agent(
    name="APDM",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="You are a cybersecurity assistant. Analyze URLs, emails, and messages for threats.",
    tools=[
        url_checker_tool,
        phishing_detector_tool,
        malware_detector_tool,
        threat_score_tool,
    ],
)
