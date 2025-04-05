import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import pdfkit
import os

# Set Streamlit page configuration
st.set_page_config(page_title="Sleep Quality Analyzer", layout="centered")
st.title("😴 Sleep Quality Analyzer")

# File path
sleep_file = "sleep_data.csv"
expected_columns = ["Date", "Sleep Hours", "Sleep Quality", "Bed Time", "Wake Time"]

# Initialize the file if not exists or is empty
if not os.path.exists(sleep_file) or os.stat(sleep_file).st_size == 0:
    pd.DataFrame(columns=expected_columns).to_csv(sleep_file, index=False)

# Load and validate data
sleep_df = pd.read_csv(sleep_file)

# Handle missing columns
if not all(col in sleep_df.columns for col in expected_columns):
    st.warning("CSV file missing columns. Reinitializing.")
    sleep_df = pd.DataFrame(columns=expected_columns)
    sleep_df.to_csv(sleep_file, index=False)

# Convert date column
sleep_df["Date"] = pd.to_datetime(sleep_df["Date"], errors='coerce')

# --- Sidebar Reminder ---
st.sidebar.header("⏰ Daily Reminder")
if st.sidebar.button("Remind Me to Log Sleep"):
    st.sidebar.success("🛏️ Don’t forget to log your sleep tonight!")

# --- Sleep Tips Generator ---
def get_tip(score):
    if score >= 8:
        return "🌟 Great job! Keep up the healthy routine."
    elif score >= 6:
        return "🕰️ Try improving bedtime consistency."
    else:
        return "📵 Consider avoiding screens and caffeine before bed."

# --- Form Input ---
st.subheader("📝 Log Today’s Sleep")

with st.form("sleep_form"):
    date = st.date_input("Date", value=datetime.now().date())
    hours = st.slider("Sleep Hours", 0, 12, 7)
    quality = st.slider("Sleep Quality (1-10)", 1, 10, 7)
    bed_time = st.time_input("Bed Time")
    wake_time = st.time_input("Wake Time")
    submitted = st.form_submit_button("Log Sleep")

    if submitted:
        new_entry = {
            "Date": pd.to_datetime(date),
            "Sleep Hours": hours,
            "Sleep Quality": quality,
            "Bed Time": bed_time.strftime("%H:%M"),
            "Wake Time": wake_time.strftime("%H:%M")
        }
        sleep_df = pd.concat([sleep_df, pd.DataFrame([new_entry])], ignore_index=True)
        sleep_df.to_csv(sleep_file, index=False)
        st.success("✅ Sleep data logged successfully!")

# --- Data Visualization ---
if not sleep_df.empty:
    st.subheader("📊 Sleep Trends")
    
    sorted_df = sleep_df.dropna(subset=["Date"]).sort_values("Date")

    chart = px.line(sorted_df, x="Date", y="Sleep Hours", title="Hours Slept Over Time", markers=True)
    st.plotly_chart(chart, use_container_width=True)

    quality_chart = px.bar(sorted_df, x="Date", y="Sleep Quality", title="Sleep Quality Over Time")
    st.plotly_chart(quality_chart, use_container_width=True)

    st.subheader("📄 Sleep Log")
    st.dataframe(sorted_df.sort_values("Date", ascending=False), use_container_width=True)

    # Tip based on last sleep quality
    st.subheader("💡 Personalized Sleep Tip")
    try:
        last_quality = int(sleep_df["Sleep Quality"].iloc[-1])
        st.info(get_tip(last_quality))
    except:
        st.info("No valid sleep quality found for tip generation.")

# --- Export Options ---
st.subheader("📤 Export Options")

col1, col2 = st.columns(2)

with col1:
    if st.button("Export as CSV"):
        sleep_df.to_csv("sleep_report.csv", index=False)
        st.success("📁 Exported to sleep_report.csv")

with col2:
    if st.button("Export as PDF"):
        try:
            html = sleep_df.to_html(index=False)
            with open("report.html", "w") as f:
                f.write(html)
            pdfkit.from_file("report.html", "sleep_report.pdf")
            st.success("📄 Exported to sleep_report.pdf")
        except Exception as e:
            st.error(f"PDF export failed: {e}")
