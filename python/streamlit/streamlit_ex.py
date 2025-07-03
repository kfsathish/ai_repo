import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Data Analysis App", layout="wide")

st.title("📊 CSV Upload and Data Analysis App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    st.write(f"✅ **Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
    st.write("✅ **Columns:**", list(df.columns))

    # Data types
    st.subheader("Column Data Types")
    st.write(df.dtypes)

    # Descriptive Statistics
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Select column for histogram
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.subheader("Histogram Visualization")
        col_to_plot = st.selectbox("Select a numeric column to plot its histogram:", numeric_cols)

        fig, ax = plt.subplots()
        df[col_to_plot].hist(bins=30, ax=ax)
        ax.set_title(f"Histogram of {col_to_plot}")
        ax.set_xlabel(col_to_plot)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        st.warning("No numeric columns available for histogram plotting.")

else:
    st.info("👈 Please upload a CSV file to begin analysis.")

st.sidebar.title("About")
st.sidebar.info("""
This app allows you to upload a CSV file and perform basic exploratory data analysis:
- View first few rows
- Check data shape, columns, and data types
- See descriptive statistics
- Check missing values
- Visualize numeric columns with histograms
""")
