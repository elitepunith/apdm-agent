from google.adk.tools import Tool
import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

def parse_emails(text: str):
    found = EMAIL_RE.findall(text or "")
    uniq = sorted(set(found))
    return {"text": text, "emails": uniq, "count": len(uniq)}

email_parser_tool = Tool(
    name="email_parser",
    description="Extracts email addresses found in a given text.",
    func=parse_emails,
    input_schema={
        "type":"object",
        "properties": {"text": {"type":"string"}},
        "required": ["text"]
    }
)
