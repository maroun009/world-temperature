import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

# Introduction "Technical Context"
st.markdown("## Technical Context")

st.write(
    """ 1. Utilising Datasets: Our project will leverage two primary datasets to investigate the global warming and climate disruption over the last few centuries and decades.
     These datasets play crucial roles in understanding the climate trends and their relation to greenhouse gas emissions. \n\n
2. CO2 and Greenhouse Gas Emissions Data (Our World in Data): This dataset provides historical (and regional) records of carbon dioxide and greenhouse gas emissions. It is essential for understanding the human impact on the environment. We plan to utilize Python to process and clean this data, ensuring its accuracy and completeness.\n\n
    """)

# Introduction "**Data Cleaning with Python**"
st.markdown("### Data Cleaning with Python")

st.write(
    """To ensure the reliability of our analyses, we will use Python for data cleaning. This process will involve:\n\n
- Global Temperature Anomalies (NASA): NASA's dataset contains detailed temperature anomalies, which are deviations from the 1951-1980 means. It includes global, hemispheric, and zonal monthly, seasonal, and annual temperature variations. We will utilize Python to preprocess this data, addressing missing values and ensuring data quality.\n\n
    """)
