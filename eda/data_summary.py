import streamlit as st
import pandas as pd
import numpy as np

def show_data_summary(df: pd.DataFrame):
    st.header("Data Summary & Insights")

    total_rows = df.shape[0]

    missing_counts = df.isnull().sum()
    missing_percent = (missing_counts / total_rows) * 100

    for col in df.columns:
        st.markdown(f"### Column: `{col}`")
        dtype = df[col].dtype
        st.write(f"Data type: {dtype}")

        missing = missing_counts[col]
        miss_pct = missing_percent[col]

        if missing > 0:
            st.warning(f"Missing values: {missing} ({miss_pct:.2f}%)")
        else:
            st.success("No missing values")

        if pd.api.types.is_numeric_dtype(df[col]):
            st.write(f"Mean: {df[col].mean():.3f}")
            st.write(f"Median: {df[col].median():.3f}")
            st.write(f"Standard Deviation: {df[col].std():.3f}")

            skewness = df[col].skew()
            st.write(f"Skewness: {skewness:.3f}")

            if abs(skewness) > 1:
                st.info("Note: Highly skewed distribution")

        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            st.write(f"Date Range: {df[col].min()} to {df[col].max()}")

        elif pd.api.types.is_object_dtype(df[col]):
            top_values = df[col].value_counts().head(3)
            st.write(f"Top categories:\n{top_values.to_frame()}")

        st.markdown("---")
