import streamlit as st
import pandas as pd
import plotly.express as px

def show_bivariate(df: pd.DataFrame):
    st.header("Bivariate Analysis")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    x_col = st.selectbox("Select X-axis column", options=numeric_cols + categorical_cols, index=0)
    y_col = st.selectbox("Select Y-axis column", options=numeric_cols, index=1)
    
    if x_col in categorical_cols:
        fig = px.box(df, x=x_col, y=y_col, title=f"Box Plot of {y_col} by {x_col}")
    else:
        fig = px.scatter(df, x=x_col, y=y_col, trendline="ols", title=f"Scatter Plot of {y_col} vs {x_col}")
    
    st.plotly_chart(fig, use_container_width=True)
