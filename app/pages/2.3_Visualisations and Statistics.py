import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

# Introduction - Identification of relationships between variables
st.markdown("## Identification of relationships between variables")

st.markdown(
    """In our analysis, we identified several key relationships between variables, with a primary focus on understanding the connections between temperature anomalies and CO2 emissions. Using Python's Seaborn and Plotly libraries, we created various types of plots and visualisations to explore these relationships. For instance, scatter plots were instrumental in examining how changes in CO2 emissions correlated with temperature anomalies over time. We also generated heatmaps to illustrate the intensity of these relationships and their spatial variations, helping us identify regions where temperature anomalies were most affected by CO2 emissions. Time series plots allowed us to analyse how these relationships evolved over time, particularly over the past century. These visualisation techniques allowed us to identify trends and outliers, enabling a comprehensive understanding of climate data patterns and relationships, contributing to a deeper insight into the climate trends under investigation. """)

# Introduction - Description of data distribution, outliers, etc.
st.markdown("### Description of data distribution, outliers, etc.")


# Introduction - Data Distribution for Temperature Anomalies:
st.markdown("## Data Distribution for Temperature Anomalies:")
st.write("""
The dataset under consideration is NASA's temperature anomaly data, specifically the "GLB.Ts+dSST.csv" file. This dataset records temperature anomalies from 1880 to 2023.
Here are the summary statistics for temperature anomalies: \n\n
●**Mean:** The mean temperature anomaly is approximately 0.06.\n
●**Median:** The median temperature anomaly is -0.06, indicating that the data is slightly left-skewed.\n
●**Mode:** The mode of the temperature anomalies is -0.11.\n
●**Standard Deviation:** The standard deviation is 0.37, suggesting that the data has moderate variability.\n
●**Range:** The range of temperature anomalies spans from -0.49 to 1.02, with a total range of 1.51.\n
●**Interquartile Range (IQR):** The IQR, which represents the middle 50% of the data, is approximately 0.47. The data's lower quartile (25th percentile) is -0.20, and the upper quartile (75th percentile) is 0.27.\n\n
These statistics provide an overview of the distribution of temperature anomalies, showing a range of values with a slight left-skew in the data, suggesting that the majority of anomalies are below zero.\n\n
""")
# Introduction - Outliers
st.markdown("### Outliers")
st.write("""
Statistical Analyses Supporting Visual Findings
The dataset, "GLB.Ts+dSST.csv," contains some potential outliers in the temperature anomaly data. To identify outliers, we can use the Interquartile Range (IQR) method. Here's a summary of the findings:\n\n
**Identified Outliers:** The potential outliers in the dataset are temperature anomalies that fall outside the bounds defined by the IQR. These anomalies are mostly extreme positive values, signifying unusually warm periods. For instance, there are anomalies that go as high as 1.02 and 1.17, which are well beyond the IQR boundaries.\n\n
**Potential Reasons for Outliers:**\n\n
  ● **Extreme Events:** Some of the outliers may be attributed to extreme climatic events, such as record-breaking heat waves or El Niño events.\n
  ● **Data Anomalies:** A few outliers could be due to data entry errors or inaccuracies in the recording process. It's essential to scrutinise the data collection methodology to ensure data integrity.\n\n
These outliers can significantly affect the analysis. Extreme positive anomalies may lead to skewed results when calculating summary statistics or trends over time. They could distort our perception of long-term climate patterns if not addressed.
Depending on the goals of our analysis, outliers will be kept in the dataset as they may be essential for studying extreme climatic events and their impacts on global temperatures.
""")

# Introduction - Statistical Analyses Supporting Visual Findings
st.markdown("### Statistical Analyses Supporting Visual Findings")
st.write("""

In this section, we performed statistical tests to further validate our visual findings and understand the relationships between key variables. We applied Pearson correlation tests with a significance level (alpha) of 0.05 to assess whether variables are correlated. The null hypothesis (H0) assumes that variables are not correlated, while the alternative hypothesis (H1) suggests a correlation between the variables. We conducted the following tests:\n\n
1  Pearson Correlation between Population and Temperature Change:\n
* **Null Hypothesis (H0):** Population and temperature change are not correlated.\n
* **Alternative Hypothesis (H1):** Population and temperature change are correlated.\n
* **Result:** The Pearson correlation test yielded a statistically significant correlation between population and temperature change.\n
2 Pearson Correlation between GDP and Temperature Change:\n
* **Null Hypothesis (H0):** GDP and temperature change are not correlated.\n
* **Alternative Hypothesis (H1):** GDP and temperature change are correlated.\n
* **Result:** The Pearson correlation test showed a statistically significant correlation between GDP and temperature change.\n
3 Pearson Correlation between CO2 Emissions and Temperature Change:\n
* **Null Hypothesis (H0):** CO2 emissions and temperature change are not correlated.\n
* **Alternative Hypothesis (H1):** CO2 emissions and temperature change are correlated.\n
* **Result:** The Pearson correlation test showed a statistically significant correlation between CO2 emissions and temperature change.\n

""")


