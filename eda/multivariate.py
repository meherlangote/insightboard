import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

def show_multivariate(df: pd.DataFrame):
    st.header("Multivariate Analysis")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) < 2:
        st.info("At least two numeric columns are required for multivariate analysis.")
        return

    # --- Correlation Heatmap ---
    corr = df[numeric_cols].corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        title="Correlation Heatmap"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Seaborn Pairplot (static image) ---
    st.subheader("Pairplot (static image using Seaborn)")

    try:
        selected_cols = numeric_cols[:5]  # Limit to 5 for readability
        sns_plot = sns.pairplot(df[selected_cols])
        buf = BytesIO()
        sns_plot.savefig(buf, format="png")
        st.image(buf.getvalue(), caption="Pairplot (Seaborn)", use_column_width=True)
    except Exception as e:
        st.error(f"Error generating pairplot: {e}")

    # --- 3D Scatter Plot ---
    st.subheader("3D Scatter Plot (Interactive)")

    if len(numeric_cols) >= 3:
        x_axis = st.selectbox("X-axis", numeric_cols, index=0, key="x")
        y_axis = st.selectbox("Y-axis", numeric_cols, index=1, key="y")
        z_axis = st.selectbox("Z-axis", numeric_cols, index=2, key="z")
        color_col = st.selectbox("Color by (optional)", ["None"] + numeric_cols, index=0)

        try:
            fig3d = px.scatter_3d(
                df,
                x=x_axis,
                y=y_axis,
                z=z_axis,
                color=df[color_col] if color_col != "None" else None,
                title="3D Scatter Plot",
                opacity=0.7
            )
            st.plotly_chart(fig3d, use_container_width=True)
        except Exception as e:
            st.error(f"Error generating 3D plot: {e}")
    else:
        st.info("Not enough numeric columns for 3D plot.")











# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.figure_factory as ff

# def show_multivariate(df: pd.DataFrame):
#     st.header("Multivariate Analysis")
    
#     numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
#     if len(numeric_cols) < 2:
#         st.info("At least two numeric columns required for multivariate analysis.")
#         return
    
#     corr = df[numeric_cols].corr()
    
#     fig = px.imshow(corr,
#                     text_auto=True,
#                     color_continuous_scale='RdBu_r',
#                     title="Correlation Heatmap")
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("Pairplot (scatterplot matrix):")
#     fig2 = px.scatter_matrix(df[numeric_cols], dimensions=numeric_cols[:5], color=None)
#     st.plotly_chart(fig2, use_container_width=True)
