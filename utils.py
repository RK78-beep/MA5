import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import fitz  # PyMuPDF

def process_file(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith((".xlsx", ".xls")):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        text = ""
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
        # Placeholder: extract financials from text using regex or table parser
        raise ValueError("PDF extraction needs advanced parsing logic.")
    else:
        raise ValueError("Unsupported file format.")
    return df

def generate_charts(df):
    try:
        fig, ax = plt.subplots()
        df["Deal Value"].plot(kind="hist", ax=ax, title="Deal Value Distribution")
        st.pyplot(fig)
    except:
        st.warning("Charts could not be generated.")

def recommend_deal(df):
    # Placeholder recommendation logic
    avg_value = df["Deal Value"].mean()
    if avg_value > 500:
        return "Recommend proceeding with due diligence. High deal value observed."
    else:
        return "Consider re-evaluating target; financials appear modest."
