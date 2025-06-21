import streamlit as st
import os

# Set up the app
st.set_page_config(page_title="📈 Stock Forecasting Dashboard", layout="wide")
st.title("📊 Stock Forecasting Dashboard – ARIMA | SARIMA | LSTM")

# Sidebar navigation
section = st.sidebar.radio("📁 Select Section", [
    "EDA",
    "ARIMA",
    "SARIMA",
    "LSTM",
    "Dashboards (HTML)"
])

# Display Python script content
def display_script(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        st.code(code, language="python")
    except FileNotFoundError:
        st.error(f"❌ File not found: {file_path}")
    except Exception as e:
        st.error(f"⚠ Error loading {file_path}: {e}")

# Display HTML dashboard
def display_dashboard(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
        st.components.v1.html(html, height=800, scrolling=True)
    except FileNotFoundError:
        st.error(f"❌ Dashboard file not found: {file_path}")
    except Exception as e:
        st.error(f"⚠ Error displaying dashboard: {e}")

# Section logic
if section == "EDA":
    st.subheader("📌 Exploratory Data Analysis")
    display_script("eda.py")

elif section == "ARIMA":
    st.subheader("🔮 ARIMA Forecast Model")
    display_script("arima.py")

elif section == "SARIMA":
    st.subheader("📆 SARIMA Forecast Model")
    display_script("sarima.py")

elif section == "LSTM":
    st.subheader("🧠 LSTM Deep Learning Forecast")
    display_script("lstm_model.py")

elif section == "Dashboards (HTML)":
    st.subheader("🌐 Interactive Dashboards")
    dashboard_file = st.selectbox("Choose a dashboard file", [
        "eda_dashboard.html",
        "simple_dashboard.html",
        "sarima_dashboard.html",
        "lstm_dashboard.html"
    ])
    display_dashboard(dashboard_file)
