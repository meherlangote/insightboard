import streamlit as st
import pandas as pd
import plotly.express as px

def show_missing(df: pd.DataFrame):
    st.header("Missing Values Analysis")
    
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'Missing Count': missing_count,
        'Missing Percentage': missing_percent
    })
    missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values(by='Missing Percentage', ascending=False)
    
    if missing_df.empty:
        st.success("No missing values found in the dataset!")
    else:
        st.dataframe(missing_df)
        
        fig = px.bar(missing_df, x=missing_df.index, y='Missing Percentage',
                     labels={"x": "Columns", "Missing Percentage": "Missing %"},
                     title="Percentage of Missing Values by Column")
        fig.update_traces(marker_color='crimson', marker_line_color='black',
                          marker_line_width=1.5, opacity=0.8)
        st.plotly_chart(fig, use_container_width=True)
