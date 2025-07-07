import streamlit as st
import pandas as pd
from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection, data_summary
from utils.color_scheme import primary_color, secondary_color

st.set_page_config(
    page_title="Nik - AI Powered EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    /* Sidebar title */
    .sidebar .css-1d391kg {  /* header */
        color: #3A81C7;
        font-weight: 700;
    }

    /* Sidebar radio container */
    section[data-testid="stSidebar"] .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 10px;
    }

    /* Each option */
    section[data-testid="stSidebar"] .stRadio > div > label {
        background-color: #1E1E1E;
        border: 2px solid #3A81C7;
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 600;
        color: #ffffff;
        transition: all 0.3s ease;
        box-shadow: 0 0 6px rgba(58, 129, 199, 0.4);
    }

    /* Hover effect */
    section[data-testid="stSidebar"] .stRadio > div > label:hover {
        background-color: #2a2d34;
        transform: scale(1.02);
        box-shadow: 0 0 12px rgba(58, 129, 199, 0.8);
        cursor: pointer;
    }

    /* Selected radio */
    section[data-testid="stSidebar"] .stRadio > div > label[data-selected="true"] {
        background-color: #3A81C7 !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(58, 129, 199, 1);
    }
    </style>
""", unsafe_allow_html=True)


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
    .stFileUploader {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    .stFileUploader > div:first-child {
        border: 2px dashed #3A81C7;
        border-radius: 15px;
        background-color: #1E1E1E;
        color: white;
        padding: 20px 50px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        box-shadow: 0 0 15px rgba(58,129,199,0.6);
        transition: all 0.3s ease;
    }

    .stFileUploader > div:first-child:hover {
        box-shadow: 0 0 20px rgba(58,129,199,1);
        background-color: #2a2d34;
    }
    </style>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["csv", "xlsx", "xls"], label_visibility="collapsed")

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
else:
    # st.info("Please upload a dataset to get started.")
    pass


















# import streamlit as st
# import pandas as pd
# from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection
# from utils.color_scheme import primary_color, secondary_color
# from eda import data_summary

# st.set_page_config(
#     page_title="InsightBoard - AI Powered EDA",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# with open("assets/styles.css") as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.markdown(f"""
#     <div class="app-title">
#         <h1>InsightBoard: AI-Powered Exploratory Data Analysis</h1>
#         <p>Upload your dataset to get automated insights & interactive visualizations</p>
#     </div>
# """, unsafe_allow_html=True)

# # Custom upload box
# st.markdown("""
#     <div class="upload-box">
#         <label for="file_uploader" class="upload-label">📤 Upload File</label>
#     </div>
# """, unsafe_allow_html=True)

# def render_upload_button():
#     # Custom upload box with styled appearance
#     uploaded_file = st.file_uploader("", type=["csv", "xlsx", "xls"], label_visibility="collapsed")

#     st.markdown("""
#         <style>
#         .custom-upload {
#             display: flex;
#             justify-content: center;
#             margin-top: 20px;
#             margin-bottom: 30px;
#         }

#         .custom-upload .stFileUploader {
#             width: fit-content;
#             margin: auto;
#         }

#         .stFileUploader > div:first-child {
#             border: 2px dashed #3A81C7;
#             border-radius: 12px;
#             background-color: #1E1E1E;
#             color: white;
#             padding: 16px 40px;
#             font-weight: 600;
#             font-size: 1.1rem;
#             text-align: center;
#             box-shadow: 0 0 10px rgba(58,129,199,0.6);
#             transition: all 0.3s ease;
#         }

#         .stFileUploader > div:first-child:hover {
#             box-shadow: 0 0 15px rgba(58,129,199,1);
#             background-color: #2a2d34;
#         }
#         </style>
#         <div class="custom-upload">
#             <div class="stFileUploader">
#                 <!-- invisible Streamlit uploader still working -->
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

#     return uploaded_file
# uploaded_file = render_upload_button()


# if uploaded_file:
#     try:
#         if uploaded_file.name.endswith(('xlsx', 'xls')):
#             df = pd.read_excel(uploaded_file)
#         else:
#             df = pd.read_csv(uploaded_file)
#         st.success(f"Dataset loaded successfully! Shape: {df.shape}")

#         st.markdown("---")

#         section = st.sidebar.radio("Select EDA Section", 
#                            ["Data Overview", "Data Summary", "Missing Values", "Univariate Analysis", 
#                             "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])

#         try:
#             if section == "Data Overview":
#                 data_overview.show_overview(df)
#             elif section == "Data Summary":
#                 data_summary.show_data_summary(df)
#             elif section == "Missing Values":
#                 missing_values.show_missing(df)
#             elif section == "Univariate Analysis":
#                 univariate.show_univariate(df)
#             elif section == "Bivariate Analysis":
#                 bivariate.show_bivariate(df)
#             elif section == "Multivariate Analysis":
#                 multivariate.show_multivariate(df)
#             elif section == "Outlier Detection":
#                 outlier_detection.show_outliers(df)
#         except Exception as e:
#             st.error(f"Oops! Something went wrong while generating this section: {e}")

#     except Exception as e:
#         st.error(f"Error loading file: {e}")
# else:
#     st.info("Please upload a dataset to get started.")

























# import streamlit as st
# import pandas as pd
# from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection
# from utils.color_scheme import primary_color, secondary_color
# from eda import data_summary

# st.set_page_config(
#     page_title="InsightBoard - AI Powered EDA",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# with open("assets/styles.css") as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.markdown(f"""
#     <h1 style="color:{primary_color}; font-weight:700; text-align:center; margin-bottom:0;">
#         InsightBoard: AI-Powered Exploratory Data Analysis
#     </h1>
#     <p style="text-align:center; color:{secondary_color}; margin-top:5px;">
#         Upload your dataset to get automated insights & interactive visualizations
#     </p>
# """, unsafe_allow_html=True)

# uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])

# if uploaded_file:
#     try:
#         if uploaded_file.name.endswith(('xlsx', 'xls')):
#             df = pd.read_excel(uploaded_file)
#         else:
#             df = pd.read_csv(uploaded_file)
#         st.success(f"Dataset loaded successfully! Shape: {df.shape}")

#         st.markdown("---")

#         section = st.sidebar.radio("Select EDA Section", 
#                            ["Data Overview", "Data Summary", "Missing Values", "Univariate Analysis", 
#                             "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])


#         # section = st.sidebar.radio("Select EDA Section", 
#         #                            ["Data Overview", "Missing Values", "Univariate Analysis", 
#         #                             "Bivariate Analysis", "Multivariate Analysis", "Outlier Detection"])

#         # Wrap EDA functions with try-except for user-friendly error messages
#         try:
#             if section == "Data Overview":
#                 data_overview.show_overview(df)
#             elif section == "Data Summary":
#                 data_summary.show_data_summary(df)
#             elif section == "Missing Values":
#                 missing_values.show_missing(df)
#             elif section == "Univariate Analysis":
#                 univariate.show_univariate(df)
#             elif section == "Bivariate Analysis":
#                 bivariate.show_bivariate(df)
#             elif section == "Multivariate Analysis":
#                 multivariate.show_multivariate(df)
#             elif section == "Outlier Detection":
#                 outlier_detection.show_outliers(df)
#         except Exception as e:
#             st.error(f"Oops! Something went wrong while generating this section: {e}")

#     except Exception as e:
#         st.error(f"Error loading file: {e}")
# else:
#     st.info("Please upload a dataset to get started.")





























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
