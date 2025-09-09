# AutoPPE-Analyst
Auto-analysis of PPE logs using multiple agents with human oversight built using **Microsoft AutoGen’s framework**.  
It automates data cleaning, analysis, and report generation, while allowing a human supervisor to review and approve final outputs.

---

## Features

- **Automated PPE Log Processing**
  - Cleans and standardizes raw PPE logs.
  - Flags invalid or missing entries.

- **Automated Analysis**
  - Computes compliance rates.
  - Identifies high-risk workers.
  - Detects trends and patterns in PPE usage.

- **Stakeholder-ready Reports**
  - Generates executive summaries, key findings, and actionable recommendations.
  - Includes visualizations and contextual insights.

- **Human-in-the-loop**
  - `UserProxyAgent` reviews and approves the final report.
  - Ensures accountability and reduces the risk of automated errors.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MonikaSinghal-22/AutoPPE-Analyst.git
```

```bash
cd AutoPPE-Analyst
```

Install dependencies:
```bash
pip install -r requirements.txt
```
Add your .env file with Gemini API keys.

Usage
Run the full workflow on a sample CSV:

```bash
python main.py
```

Agents run in the following order:
DataPreparer → Analyst → Reporter → UserProxy

The UserProxyAgent reviews the final report for approval.