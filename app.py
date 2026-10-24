import json
import os
import streamlit as st

st.set_page_config(
    page_title="HerHealth Insight",
    page_icon="🌸",
    layout="wide"
)

st.title("🌸 HerHealth Insight")

st.subheader("Women's Health Tracking & Awareness Platform")

st.write("Track your menstrual cycle, record symptoms, and understand your health patterns.")

st.success("Welcome to HerHealth Insight!")

# Save symptom data to a JSON file
DATA_FILE = "symptoms.json"

def save_symptom(record):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            records = json.load(file)
    else:
        records = []

    records.append(record)

    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)

# Symptom Tracking
st.header("🩺 Symptom Tracker")

with st.form("symptom_form"):
    date = st.date_input("Select Date")

    symptom = st.selectbox(
        "Select Symptom",
        ["Cramps", "Headache", "Fatigue",
         "Mood Swings", "Bloating", "Other"]
    )

    severity = st.slider(
        "Symptom Severity",
        min_value=1,
        max_value=5,
        value=3
    )

    notes = st.text_area("Additional Notes")

    submitted = st.form_submit_button("Save Symptom")

    
    if submitted:
        record = {
            "date": str(date),
            "symptom": symptom,
            "severity": severity,
            "notes": notes
        }

        save_symptom(record)

        st.success("Symptom saved successfully!")

        st.write("Date:", date)
        st.write("Symptom:", symptom)
        st.write("Severity:", severity)
        st.write("Notes:", notes)

# Menstrual Cycle Tracker
st.header("📅 Menstrual Cycle Tracker")

CYCLE_FILE = "cycles.json"

def save_cycle(record):
    if os.path.exists(CYCLE_FILE):
        with open(CYCLE_FILE, "r") as file:
            cycles = json.load(file)
    else:
        cycles = []

    cycles.append(record)

    with open(CYCLE_FILE, "w") as file:
        json.dump(cycles, file, indent=4)

with st.form("cycle_form"):
    period_date = st.date_input(
        "Select Period Start Date",
        key="period_date"
    )

    cycle_submitted = st.form_submit_button(
        "Save Period Date"
    )

    if cycle_submitted:
        save_cycle({
            "period_start": str(period_date)
        })

        st.success("Period date saved successfully!")

# Display cycle history
if os.path.exists(CYCLE_FILE):
    with open(CYCLE_FILE, "r") as file:
        cycles = json.load(file)

    if cycles:
        import pandas as pd

        df = pd.DataFrame(cycles)
        df["period_start"] = pd.to_datetime(
            df["period_start"]
        )

        df = df.drop_duplicates(
            subset=["period_start"]
        ).sort_values("period_start")

        st.subheader("Cycle History")
        st.dataframe(df, hide_index=True)

        if len(df) >= 2:
            intervals = df["period_start"].diff().dt.days.dropna()

            average_cycle = intervals.mean()

            st.metric(
                "Average Cycle Length",
                f"{average_cycle:.1f} days"
            )

            st.caption(
                "Calculated from recorded period start dates. "
                "This is not a medical diagnosis or a prediction."
            )
        else:
            st.info(
                "Add at least two different period start dates "
                "to calculate your cycle length."
            )

# Health Insights Dashboard
st.header("📊 Health Insights Dashboard")

import pandas as pd
import plotly.express as px

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        symptoms = json.load(file)

    if symptoms:
        df_symptoms = pd.DataFrame(symptoms)

        # Convert severity to numbers
        df_symptoms["severity"] = pd.to_numeric(
            df_symptoms["severity"]
        )

        # Dashboard metrics
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Symptoms Recorded",
                len(df_symptoms)
            )

        with col2:
            st.metric(
                "Average Symptom Severity",
                round(df_symptoms["severity"].mean(), 1)
            )

        # Symptom frequency chart
        st.subheader("Symptom Frequency")

        symptom_counts = (
            df_symptoms["symptom"]
            .value_counts()
            .reset_index()
        )

        symptom_counts.columns = [
            "Symptom", "Count"
        ]

        fig = px.bar(
            symptom_counts,
            x="Symptom",
            y="Count",
            color="Symptom",
            title="Frequency of Recorded Symptoms"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.info("No symptoms recorded yet.")

else:
    st.info(
        "Start recording symptoms to view health insights."
    )


# Downloadable Health Report
st.header("📄 Download Health Report")

st.write(
    "Download your recorded symptoms and menstrual "
    "cycle history for personal reference or consultation."
)

# Download symptom records
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        symptom_records = json.load(file)

    if symptom_records:
        symptom_df = pd.DataFrame(symptom_records)

        st.subheader("Symptom History")
        st.dataframe(symptom_df, hide_index=True)

        symptom_csv = symptom_df.to_csv(index=False)

        st.download_button(
            label="⬇️ Download Symptom Report",
            data=symptom_csv,
            file_name="HerHealth_Symptom_Report.csv",
            mime="text/csv"
        )
    else:
        st.info("No symptom records available.")
else:
    st.info("No symptom records available.")

# Download menstrual cycle records
if os.path.exists(CYCLE_FILE):
    with open(CYCLE_FILE, "r") as file:
        cycle_records = json.load(file)

    if cycle_records:
        cycle_df = pd.DataFrame(cycle_records)

        st.subheader("Menstrual Cycle History")
        st.dataframe(cycle_df, hide_index=True)

        cycle_csv = cycle_df.to_csv(index=False)

        st.download_button(
            label="⬇️ Download Menstrual Cycle Report",
            data=cycle_csv,
            file_name="HerHealth_Cycle_Report.csv",
            mime="text/csv"
        )
    else:
        st.info("No menstrual cycle records available.")
else:
    st.info("No menstrual cycle records available.")

st.caption(
    "Disclaimer: HerHealth Insight is a health tracking "
    "and awareness tool, not a medical diagnostic system."
)
