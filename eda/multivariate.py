import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

def show_multivariate(df: pd.DataFrame):
    st.header("Multivariate Analysis")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    if len(numeric_cols) < 2:
        st.info("At least two numeric columns required for multivariate analysis.")
        return
    
    corr = df[numeric_cols].corr()
    
    fig = px.imshow(corr,
                    text_auto=True,
                    color_continuous_scale='RdBu_r',
                    title="Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("Pairplot (scatterplot matrix):")
    fig2 = px.scatter_matrix(df[numeric_cols], dimensions=numeric_cols[:5], color=None)
    st.plotly_chart(fig2, use_container_width=True)
