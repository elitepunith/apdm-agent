
---

# 🔐 **APDM – Adaptive Phishing Defense Mentor**

### **A Multi-Agent Cybersecurity System Powered by Google ADK + Gemini**

APDM (Adaptive Phishing Defense Mentor) is a multi-agent cybersecurity system built to detect **phishing**, **malware links**, **unsafe URLs**, and **suspicious messages**.
It uses **Google ADK**, **Gemini 2.5 Flash Lite**, and **custom tool pipelines** to deliver fast, intelligent threat analysis.

Built as part of **Google’s AI Agents Intensive – Capstone Project (2025)**.

---

# 🌟 **Portfolio Spotlight**

APDM acts as a **real-time AI security mentor**.
It analyzes user input, selects the right tools, merges results, and gives a clear final explanation with a numeric threat score.

The system includes:

* A Gemini-powered APDM Agent
* Google ADK-based orchestration
* URL checker
* Malware detector
* Phishing detector
* Email parser
* Threat score engine

The final output is simple:
**Is it safe or dangerous — and why?**

---

# 📸 **Project Branding & UI**

### **APDM Logo (For README Preview)**

*(Place your image here if needed)*

```
[Insert APDM Banner Image]
```

### **Architecture Demo Screenshot**

```
[Insert CLI Demo Screenshot]
```

---

# 📌 **Table of Contents**

* [🚀 Overview](#-overview)
* [🎯 Problem Statement](#-problem-statement)
* [💡 Solution Overview](#-solution-overview)
* [🧠 Features](#-features)
* [🏗 Architecture](#-architecture)
* [🛠 Tools Used](#-tools-used)
* [🤖 Agents](#-agents)
* [📂 Folder Structure](#-folder-structure)
* [⚙️ Installation](#️-installation)
* [▶️ Running the Project](#️-running-the-project)
* [📊 Example Interactions](#-example-interactions)
* [📝 Evaluation Criteria Coverage](#-evaluation-criteria-coverage)
* [⚠️ Limitations](#️-limitations)
* [🔮 Future Enhancements](#-future-enhancements)
* [📄 License](#-license)

---

# 🚀 **Overview**

APDM is a smart cybersecurity assistant that evaluates:

* URLs
* Emails
* Messages
* Suspicious text

It combines **Gemini reasoning**, **Google ADK orchestration**, and **custom tools** to give a final threat assessment.

---

# 🎯 **Problem Statement**

Cyber threats continue to rise, but beginners lack the skills to identify:

* Phishing
* Malware URLs
* Scam messages
* Suspicious email indicators

There is no AI system that combines:

✔ analysis
✔ education
✔ protection

APDM fills that gap.

---

# 💡 **Solution Overview**

APDM provides:

* Multi-tool threat detection
* Smart reasoning using Gemini
* Combined threat score
* Clear explanations
* Real-time cybersecurity mentoring

---

# 🧠 **Features**

### ✔ URL Safety Analysis

Validates structure, HTTP status, domain safety.

### ✔ Malware Detection

Matches domains against malware patterns.

### ✔ Email Parsing

Extracts emails, links, and suspicious tokens.

### ✔ Phishing Detection

Flags urgency keywords, fraud patterns.

### ✔ Threat Scoring

Scores risk from **0–10**.

### ✔ ADK Multi-Agent Architecture

Gemini agent orchestrates all tools.

---

# 🏗 **Architecture**

```
                        ┌───────────────────────────┐
                        │           USER             │
                        │  (URL / Email / Message)   │
                        └──────────────┬─────────────┘
                                       │
                                       ▼
                        ┌───────────────────────────┐
                        │      InMemoryRunner        │
                        │   (ADK Orchestration)      │
                        └──────────────┬─────────────┘
                                       │
                                       ▼
                   ┌────────────────────────────────────────┐
                   │               APDM AGENT                │
                   │         (Gemini 2.5 Flash Lite)         │
                   │------------------------------------------│
                   │  • Intent understanding                  │
                   │  • Decides which tools to call           │
                   │  • Merges outputs                        │
                   │  • Generates final explanation           │
                   └──────────────┬───────────────────────────┘
                                  │ Tool Calls
                                  ▼
        ┌─────────────────────────────────────────────────────────────────────┐
        │                                TOOLS                                │
        │---------------------------------------------------------------------│
        │  • URL Checker – Validates URL + HTTP status                        │
        │  • Malware Detector – Detects unsafe domains                         │
        │  • Phishing Detector – Flags known phishing patterns                 │
        │  • Email Parser – Extracts emails, tokens, URLs                      │
        │  • Threat Score Tool – Returns final numeric risk (0–10)             │
        └──────────────────────────────┬───────────────────────────────────────┘
                                       │ Tool Results
                                       ▼
                         ┌───────────────────────────────────┐
                         │          APDM AGENT                │
                         │   (Merge + Summary Reasoning)      │
                         └──────────────────┬──────────────────┘
                                            │
                                            ▼
                         ┌───────────────────────────────────┐
                         │               USER                │
                         │   Final Verdict + Explanation     │
                         └───────────────────────────────────┘
```

---

# 🛠 **Tools Used**

| Tool                | Purpose                             |
| ------------------- | ----------------------------------- |
| URL Checker         | Fetches & validates URLs            |
| Malware Detector    | Matches malware patterns            |
| Phishing Detector   | Detects phishing markers            |
| Email Parser        | Extracts and analyzes email content |
| Threat Score Engine | Calculates a final score            |

---

# 🤖 **Agents**

### **Coordinator / APDM Agent**

* Determines intent
* Selects tools
* Merges tool results
* Generates the final explanation

Model:

```
Gemini 2.5 Flash Lite
```

---

# 📂 **Folder Structure**

```
APDM/
│── agent.py
│── run.py
│── requirements.txt
│── README.md
│
└── tools/
     ├── url_checker.py
     ├── malware_detector.py
     ├── malware_link_detector.py
     ├── phishing_detector.py
     ├── email_parser.py
     └── threat_score.py
```

---

# ⚙️ **Installation**

### 1. Clone repo

```
git clone https://github.com/YOUR-USERNAME/APDM.git
cd APDM
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set Gemini API key

```
export GOOGLE_API_KEY="your-key"
```

---

# ▶️ **Running the Project**

```
python run.py
```

Example:

```
analyze this: https://example.com
```

---

# 📊 **Example Interactions**

### Input:

```
analyze this URL: http://free-gift-claim-now.xyz/login
```

### Output:

```
⚠️ High Risk (Score: 9/10)

- Suspicious domain (.xyz)
- Phishing keywords: “claim", “gift”
- Known malicious pattern detected

Recommendation:
Do NOT open this URL.
```

---

# 📝 **Evaluation Criteria Coverage**

✔ Clear pitch
✔ Working multi-agent system
✔ ADK-based orchestration
✔ Custom cybersecurity tools
✔ Strong reasoning through Gemini
✔ Clean structure, easy evaluation
✔ Ready for deployment/demo

---

# ⚠️ **Limitations**

* Rule-based detection (not ML trained)
* No real-time sandbox analysis
* Cannot detect zero-day threats

---

# 🔮 **Future Enhancements**

* Add ML-based phishing classifier
* Add browser extension
* Add sandbox URL execution
* Add user learning memory
* Add threat timeline history

---

# 📄 **License**

Licensed under **CC-BY-SA 4.0**, as required by the competition rules.

---
