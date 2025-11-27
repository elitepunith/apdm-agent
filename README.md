
---

# 🔐 **APDM – Adaptive Phishing Defense Mentor**

### **A Multi-Agent Cybersecurity System Powered by Google ADK + Gemini**

APDM (Adaptive Phishing Defense Mentor) is a multi-agent cybersecurity system built to detect **phishing**, **malware links**, **unsafe URLs**, and **suspicious messages**.
It uses **Google ADK**, **Gemini 2.5 Flash Lite**, and **custom tool pipelines** to deliver fast, intelligent threat analysis.

Built as part of **Google’s AI Agents Intensive – Capstone Project (2025)**.

---

# 🌟 **Portfolio Spotlight**

APDM acts as a **real-time AI security mentor**.
It analyzes user input, selects the right tools, merges results, and provides a clear explanation with a numeric threat score.

The system includes:

* Gemini-powered APDM Agent
* Google ADK orchestration
* URL checker
* Malware detector
* Phishing detector
* Email parser
* Threat score engine

**Final Output:**
➡️ *Is it safe or dangerous — and why?*

---

# 📸 **Project Branding & UI**

### **APDM Logo**

<p align="center">
  <img src="https://raw.githubusercontent.com/elitepunith/apdm-agent/main/images/banner.png" width="350">
</p>

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

It uses **Gemini reasoning**, **Google ADK**, and **custom tools** to provide final threat assessments.

---

# 🎯 **Problem Statement**

Beginners find it difficult to identify:

* Phishing
* Malware URLs
* Scam messages
* Suspicious email content

APDM bridges the gap by combining:

✔ analysis
✔ education
✔ protection

---

# 💡 **Solution Overview**

APDM provides:

* Multi-tool threat detection
* Smart reasoning via Gemini
* Combined threat score
* Clear explanations
* Real-time cybersecurity mentoring

---

# 🧠 **Features**

### ✔ URL Safety Analysis

Validates structure, fetches status, checks domain patterns.

### ✔ Malware Detection

Flags known malicious domains.

### ✔ Email Parsing

Extracts emails, URLs, and metadata.

### ✔ Phishing Detection

Detects urgency cues and scam text.

### ✔ Threat Scoring

Returns a **0–10 risk score**.

### ✔ ADK Multi-Agent Architecture

Gemini orchestrates & merges results.

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
                   │  • Tool selection                        │
                   │  • Output merging                        │
                   │  • Summary generation                   │
                   └──────────────┬───────────────────────────┘
                                  │ Tool Calls
                                  ▼
        ┌─────────────────────────────────────────────────────────────────────┐
        │                                TOOLS                                │
        │---------------------------------------------------------------------│
        │  • URL Checker Tool                                                 │
        │  • Malware Detector Tool                                            │
        │  • Phishing Detector Tool                                           │
        │  • Email Parser Tool                                                │
        │  • Threat Score Tool                                                │
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
| Malware Detector    | Detects unsafe domains              |
| Phishing Detector   | Flags phishing content              |
| Email Parser        | Extracts and analyzes email content |
| Threat Score Engine | Calculates final risk score         |

---

# 🤖 **Agents**

### **Coordinator / APDM Agent**

* Determines intent
* Selects and calls tools
* Merges their outputs
* Produces the final reasoning

Model used:

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
- Phishing keywords detected
- Malicious pattern found

Recommendation:
❗ Do NOT open this URL.
```

---

# 🖥️ **Demo Output**

<p align="center">
  <img src="https://raw.githubusercontent.com/elitepunith/apdm-agent/main/images/demo.png" width="900">
</p>

---

# 📝 **Evaluation Criteria Coverage**

✔ Clear problem
✔ Strong ADK implementation
✔ Multi-tool selection
✔ Clean architecture
✔ Good observability
✔ High-quality reasoning

---

# ⚠️ **Limitations**

* Rule-based logic (no ML training)
* No real-time sandboxing
* Cannot detect zero-day attacks

---

# 🔮 **Future Enhancements**

* ML phishing classifier
* Browser extension
* Sandboxed URL execution
* Memory-based personalization
* Threat history dashboard

---

# 📄 **License**

Licensed under **CC-BY-SA 4.0**, as required by the competition.

---
