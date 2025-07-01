# import streamlit as st
# import pandas as pd
# from eda import data_overview, missing_values, univariate, bivariate, multivariate, outlier_detection
# from utils.color_scheme import primary_color, secondary_color
# import streamlit.components.v1 as components

# # Same page config and CSS loading as before...

# uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx", "xls"])

# if uploaded_file:
#     try:
#         if uploaded_file.name.endswith(('xlsx', 'xls')):
#             df = pd.read_excel(uploaded_file)
#         else:
#             df = pd.read_csv(uploaded_file)
#         st.success(f"Dataset loaded successfully! Shape: {df.shape}")

#         st.markdown("---")

#         # Create placeholders to collect HTML snippets for report
#         eda_html_snippets = {}

#         # Prepare overview HTML snippet
#         with st.expander("Data Overview", expanded=True):
#             try:
#                 data_overview.show_overview(df)
#                 # Capture dataframe as HTML
#                 eda_html_snippets['data_overview'] = df.head().to_html() + df.describe(include='all').to_html()
#             except Exception as e:
#                 st.error(f"Error in Data Overview: {e}")
#                 eda_html_snippets['data_overview'] = f"<p>Error generating overview: {e}</p>"

#         with st.expander("Missing Values", expanded=False):
#             try:
#                 missing_values.show_missing(df)
#                 missing_df = df.isnull().sum()
#                 missing_df = pd.DataFrame({'Missing Count': missing_df, 'Missing %': (missing_df / len(df) * 100)})
#                 eda_html_snippets['missing_values'] = missing_df[missing_df['Missing Count'] > 0].to_html()
#             except Exception as e:
#                 st.error(f"Error in Missing Values: {e}")
#                 eda_html_snippets['missing_values'] = f"<p>Error generating missing values: {e}</p>"

#         with st.expander("Univariate Analysis", expanded=False):
#             try:
#                 univariate.show_univariate(df)
#                 # For simplicity, just save column names analyzed
#                 eda_html_snippets['univariate'] = "<p>Univariate plots generated in app.</p>"
#             except Exception as e:
#                 st.error(f"Error in Univariate Analysis: {e}")
#                 eda_html_snippets['univariate'] = f"<p>Error: {e}</p>"

#         with st.expander("Bivariate Analysis", expanded=False):
#             try:
#                 bivariate.show_bivariate(df)
#                 eda_html_snippets['bivariate'] = "<p>Bivariate plots generated in app.</p>"
#             except Exception as e:
#                 st.error(f"Error in Bivariate Analysis: {e}")
#                 eda_html_snippets['bivariate'] = f"<p>Error: {e}</p>"

#         with st.expander("Multivariate Analysis", expanded=False):
#             try:
#                 multivariate.show_multivariate(df)
#                 eda_html_snippets['multivariate'] = "<p>Multivariate plots generated in app.</p>"
#             except Exception as e:
#                 st.error(f"Error in Multivariate Analysis: {e}")
#                 eda_html_snippets['multivariate'] = f"<p>Error: {e}</p>"

#         with st.expander("Outlier Detection", expanded=False):
#             try:
#                 outlier_detection.show_outliers(df)
#                 eda_html_snippets['outliers'] = "<p>Outlier detection plots generated in app.</p>"
#             except Exception as e:
#                 st.error(f"Error in Outlier Detection: {e}")
#                 eda_html_snippets['outliers'] = f"<p>Error: {e}</p>"

#         # Button to generate and download report
#         if st.button("Generate & Download EDA Report"):
#             report_html = generate_report(df, eda_html_snippets)
#             st.markdown(get_download_link(report_html), unsafe_allow_html=True)
            

#     except Exception as e:
#         st.error(f"Error loading file: {e}")
# else:
#     st.info("Please upload a dataset to get started.")



























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
