import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os
import base64
import plotly.io as pio
import streamlit as st

# Helper: Save Plotly fig as base64 PNG string for embedding
def fig_to_base64(fig):
    img_bytes = pio.to_image(fig, format='png')
    encoded = base64.b64encode(img_bytes).decode()
    return f'<img src="data:image/png;base64,{encoded}" alt="plot" />'

def generate_report(df, eda_results):
    """
    eda_results: dict containing HTML snippets for each section.
    """
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    html_content = template.render(
        dataset_overview=eda_results.get('data_overview', 'No overview data'),
        missing_values=eda_results.get('missing_values', 'No missing data'),
        univariate_analysis=eda_results.get('univariate', 'No univariate analysis'),
        bivariate_analysis=eda_results.get('bivariate', 'No bivariate analysis'),
        multivariate_analysis=eda_results.get('multivariate', 'No multivariate analysis'),
        outlier_detection=eda_results.get('outliers', 'No outlier analysis'),
    )
    return html_content

def get_download_link(html_content, filename="InsightBoard_EDA_Report.html"):
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">📥 Download EDA Report (HTML)</a>'
    return href
