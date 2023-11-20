import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

# Introduction - Data Cleaning and Processing Steps
st.markdown("## Understanding and Manipulation of Data")

st.markdown("### Description of the Dataset(s) Used and Their Availability")

st.markdown("""
Our project is driven by specific objectives aimed at understanding global climate trends, performing geographical analyses, and comparing current climate anomalies with historical phases. To achieve these objectives, we rely on two primary datasets:
""")

st.markdown("""
*	Data on CO2 and Greenhouse Gas Emissions by Our World in Data: This dataset provides invaluable historical records of carbon dioxide (CO2) and greenhouse gas emissions on a global scale. It covers emissions from various sectors and is freely accessible, sourced from Our World in Data.
*	NASA Tables of Global and Hemispheric Means and Zonal Annual Means: This dataset presents temperature anomalies, representing deviations from the 1951-1980 baseline. It includes global, Northern Hemisphere, and Southern Hemisphere temperature data, with records dating back to 1880. This dataset is openly available to the public, provided by NASA.
""")

greenhouse_gas = Image.open("app/img/LeafLightbulb.jpeg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Ownership of Data")

st.markdown("""
Both of these datasets are accessible to the public without any ownership concerns or restrictions. They are offered by reputable sources, ensuring the quality and authenticity of the data.
""")

st.markdown("### Volume of the Dataset and Its Relevance to the Objectives")

st.markdown("""
*	Data on CO2 and Greenhouse Gas Emissions: This dataset, with its extensive historical coverage, empowers us to investigate the environmental impact of emissions. It spans various sectors and offers ample data, aligning perfectly with our objectives. It's particularly relevant for our geographical analysis of Europe, the USA, and China.
*	NASA Temperature Anomalies Dataset: Boasting long-term temperature records from 1880 to the present, this dataset plays a crucial role in our exploration of global climate trends over the past century and from the year 2000 onward. The substantial volume of data is essential for our comparison of current climate anomalies with historical phases, thereby addressing our project's core objectives.
""")