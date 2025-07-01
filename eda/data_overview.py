import streamlit as st
import pandas as pd

def show_overview(df: pd.DataFrame):
    st.header("Data Overview")
    
    st.write("**First 5 rows:**")
    st.dataframe(df.head())
    
    st.write("**Dataset Shape:**")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    st.write("**Column Data Types:**")
    dtype_df = pd.DataFrame(df.dtypes, columns=["Data Type"]).reset_index()
    dtype_df.columns = ["Column", "Data Type"]
    st.table(dtype_df)
    
    st.write("**Basic Statistics:**")
    st.dataframe(df.describe(include='all').T)
