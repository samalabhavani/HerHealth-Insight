# 🌸 HerHealth Insight

### A Privacy-Conscious Women's Health Tracking & Awareness Platform

**Hackathon:** recHERsion'26 — ACM-W, NITK Surathkal

**Problem Statement:** PS1 — Women's Healthcare

**Team Size:** 2 Members

## Problem Statement

Many women find it difficult to consistently track menstrual cycles, record symptoms, and identify recurring health patterns. This can make it harder to communicate their health history during medical consultations.

## Our Solution

HerHealth Insight is a Python-based web application that helps women track menstrual cycle dates, record symptoms, visualize health patterns, and download personal health records.

## Key Features

1. **Symptom Tracker:** Record symptoms, severity levels, dates, and additional notes.
2. **Menstrual Cycle Tracker:** Save period start dates and calculate average cycle intervals.
3. **Health Insights Dashboard:** Visualize symptom frequency and average severity.
4. **Downloadable Health Reports:** Export symptom and menstrual cycle records as CSV files.

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- JSON for local data storage

## Installation

Clone or download this repository.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## How It Works

1. Open the application.
2. Enter and save symptom details.
3. Record menstrual period start dates.
4. View calculated cycle intervals and symptom charts.
5. Download CSV reports.

## Privacy and Limitations

- Health records are stored locally in JSON files.
- The project does not require user accounts or external health-data APIs.
- Local JSON storage is intended for a single-user prototype, not secure multi-user deployment.
- The application does not diagnose medical conditions.
- Use fictional records for demonstrations.

## Future Scope

- Secure user authentication
- Encrypted health-data storage
- Improved menstrual cycle visualization
- Personalized educational resources
- Clinician-friendly report generation

## Disclaimer

HerHealth Insight is an educational health-tracking prototype. It is not a medical diagnostic tool and does not replace professional medical advice.
