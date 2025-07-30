import streamlit as st
import pandas as pd
import pickle
import os
from utils import process_file, generate_charts, recommend_deal

st.set_page_config(page_title="M&A Deal Analyzer", layout="wide")
st.title("🤖 M&A Deal Success Predictor & Analyzer")

uploaded_file = st.file_uploader("Upload Financial Document (CSV, Excel, or PDF)", type=["csv", "xlsx", "xls", "pdf"])

if uploaded_file:
    try:
        df = process_file(uploaded_file)
        st.subheader("📊 Uploaded & Processed Data")
        st.dataframe(df)

        with open("model.pkl", "rb") as f:
            model = pickle.load(f)

        # Prediction
        prediction = model.predict(df.select_dtypes(include=["number"]))
        df["Predicted Success"] = prediction

        st.subheader("✅ Prediction Results")
        st.dataframe(df)

        st.subheader("📈 Visual Insights")
        generate_charts(df)

        st.subheader("💡 Strategic Recommendations")
        st.markdown(recommend_deal(df))

    except Exception as e:
        st.error(f"Something went wrong: {e}")
