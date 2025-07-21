import streamlit as st
import pandas as pd
from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection, data_summary
from utils.color_scheme import primary_color, secondary_color

st.set_page_config(
    page_title="AI Powered EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject global styles
with open("assets/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title and subtitle
st.markdown(f"""
    <h1 style="color:{primary_color}; font-weight:700; text-align:center; margin-bottom:0;">
        AI-Powered Exploratory Data Analysis
    </h1>
    <p style="text-align:center; color:{secondary_color}; margin-top:5px;">
        Upload your dataset to get automated insights & interactive visualizations
    </p>
""", unsafe_allow_html=True)

# Custom Upload UI
st.markdown("""
    <style>
    /* Hide default text inside the uploader */
    .stFileUploader label div:first-child {
        visibility: hidden;
        height: 0;
        margin: 0;
        padding: 0;
    }

    /* Replace it with your custom text */
    .stFileUploader label::after {
        content: "Upload File";
        color: #000000;
        font-weight: bold;
        font-size: 18px;
        display: block;
        text-align: center;
        padding: 20px 40px;
        background-color: #ffffff;
        border: 2px dashed #f57c00;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(245,124,0,0.5);
        transition: all 0.3s ease;
    }

    .stFileUploader label:hover::after {
        background-color: #fbe9e7;
        box-shadow: 0 0 20px rgba(245,124,0,0.8);
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-file-uploader">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["csv", "xlsx", "xls"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)


# Process uploaded file
if uploaded_file:
    try:
        if uploaded_file.name.endswith(('xlsx', 'xls')):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        st.success(f"Dataset loaded successfully! Shape: {df.shape}")

        st.markdown("---")

        with st.sidebar:
            st.markdown("## Select EDA Section", unsafe_allow_html=True)
            section = st.radio(
                "",
                ["Data Overview", "Data Summary", "Missing Values", "Univariate Analysis",
                "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"]
            )

        try:
            if section == "Data Overview":
                data_overview.show_overview(df)
            elif section == "Data Summary":
                data_summary.show_data_summary(df)
            elif section == "Missing Values":
                missing_values.show_missing(df)
            elif section == "Univariate Analysis":
                univariate.show_univariate(df)
            elif section == "Bivariate Analysis":
                bivariate.show_bivariate(df)
            elif section == "Multivariate Analysis":
                multivariate.show_multivariate(df)
            elif section == "Outlier Detection":
                outlier_detection.show_outliers(df)
        except Exception as e:
            st.error(f"Oops! Something went wrong while generating this section: {e}")

    except Exception as e:
        st.error(f"Error loading file: {e}")

