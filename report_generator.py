import base64
from jinja2 import Environment, FileSystemLoader

def generate_report(df, eda_results):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    html_content = template.render(
        dataset_overview=eda_results.get('data_overview', ''),
        missing_values=eda_results.get('missing_values', ''),
        univariate_analysis=eda_results.get('univariate', ''),
        bivariate_analysis=eda_results.get('bivariate', ''),
        multivariate_analysis=eda_results.get('multivariate', ''),
        outlier_detection=eda_results.get('outliers', ''),
    )
    return html_content

def get_download_link(html_content, filename="InsightBoard_Report.html"):
    b64 = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">📥 Download EDA Report (HTML)</a>'
    return href
