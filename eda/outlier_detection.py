import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def show_outliers(df: pd.DataFrame):
    st.header("Outlier Detection")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    col = st.selectbox("Select numeric column to check outliers", numeric_cols)
    
    if col:
        # Calculate IQR for outlier detection
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
        
        st.write(f"Number of outliers detected in **{col}**: {outliers.shape[0]}")
        
        fig = px.box(df, y=col, points="all", title=f"Box Plot with Outliers for {col}")
        st.plotly_chart(fig, use_container_width=True)
