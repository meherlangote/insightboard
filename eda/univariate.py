import streamlit as st
import pandas as pd
import plotly.express as px

def show_univariate(df: pd.DataFrame):
    st.header("Univariate Analysis")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    col = st.selectbox("Select column for univariate analysis", options=numeric_cols + categorical_cols)
    
    if col in numeric_cols:
        fig = px.histogram(df, x=col, nbins=30, title=f"Histogram of {col}")
        fig.update_layout(bargap=0.1)
        st.plotly_chart(fig, use_container_width=True)
        
        fig_box = px.box(df, y=col, title=f"Box Plot of {col}")
        st.plotly_chart(fig_box, use_container_width=True)
        
    elif col in categorical_cols:
        counts = df[col].value_counts().reset_index()
        counts.columns = [col, 'Count']
        fig = px.bar(counts, x=col, y='Count', title=f"Bar Plot of {col}")
        st.plotly_chart(fig, use_container_width=True)
