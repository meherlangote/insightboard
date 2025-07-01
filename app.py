import streamlit as st
import pandas as pd
from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection
from utils.color_scheme import primary_color, secondary_color
from eda import data_summary

st.set_page_config(
    page_title="InsightBoard - AI Powered EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("assets/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown(f"""
    <h1 style="color:{primary_color}; font-weight:700; text-align:center; margin-bottom:0;">
        InsightBoard: AI-Powered Exploratory Data Analysis
    </h1>
    <p style="text-align:center; color:{secondary_color}; margin-top:5px;">
        Upload your dataset to get automated insights & interactive visualizations
    </p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(('xlsx', 'xls')):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        st.success(f"Dataset loaded successfully! Shape: {df.shape}")

        st.markdown("---")

        section = st.sidebar.radio("Select EDA Section", 
                           ["Data Overview", "Data Summary", "Missing Values", "Univariate Analysis", 
                            "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])


        # section = st.sidebar.radio("Select EDA Section", 
        #                            ["Data Overview", "Missing Values", "Univariate Analysis", 
        #                             "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])

        # Wrap EDA functions with try-except for user-friendly error messages
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
else:
    st.info("Please upload a dataset to get started.")





























# import streamlit as st
# import pandas as pd
# from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection
# from utils.color_scheme import primary_color, secondary_color, background_color, hover_color
# import streamlit.components.v1 as components

# # Page config
# st.set_page_config(
#     page_title="InsightBoard - AI Powered EDA",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Inject custom CSS for hover effects and styling
# with open("assets/styles.css") as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # Title
# st.markdown(f"""
#     <h1 style="color:{primary_color}; font-weight:700; text-align:center; margin-bottom:0;">
#         InsightBoard: AI-Powered Exploratory Data Analysis
#     </h1>
#     <p style="text-align:center; color:{secondary_color}; margin-top:5px;">
#         Upload your dataset to get automated insights & interactive visualizations
#     </p>
# """, unsafe_allow_html=True)

# # File uploader
# uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])

# if uploaded_file:
#     # Read data
#     try:
#         if uploaded_file.name.endswith(('xlsx', 'xls')):
#             df = pd.read_excel(uploaded_file)
#         else:
#             df = pd.read_csv(uploaded_file)
        
#         st.success(f"Dataset loaded successfully! Shape: {df.shape}")
        
#         st.markdown("---")
        
#         # Sidebar navigation for EDA sections
#         section = st.sidebar.radio("Select EDA Section", 
#                                    ["Data Overview", "Missing Values", "Univariate Analysis", 
#                                     "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])
        
#         # Run selected section
#         if section == "Data Overview":
#             data_overview.show_overview(df)
#         elif section == "Missing Values":
#             missing_values.show_missing(df)
#         elif section == "Univariate Analysis":
#             univariate.show_univariate(df)
#         elif section == "Bivariate Analysis":
#             bivariate.show_bivariate(df)
#         elif section == "Multivariate Analysis":
#             multivariate.show_multivariate(df)
#         elif section == "Outlier Detection":
#             outlier_detection.show_outliers(df)
        
#     except Exception as e:
#         st.error(f"Error loading file: {e}")
# else:
#     st.info("Please upload a dataset to get started.")
