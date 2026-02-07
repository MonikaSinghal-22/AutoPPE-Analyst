# AutoPPE-Analyst

Auto-analysis of PPE logs using multiple agents built using **Microsoft AutoGen's framework**.  
It automates data cleaning, analysis, and report generation.

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
DataPreparer → Analyst → Reporter

---

## Project Architecture

The system is modular, with agents collaborating to process, analyze, and report on PPE logs. See `architecture.excalidraw` for a visual overview.


## Sample Data

The repository includes `ppe_log_sample.csv` for testing and demonstration purposes.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the terms of the license found in the `LICENSE` file.