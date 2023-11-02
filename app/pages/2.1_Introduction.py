import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

# Introduction - Technical Context
st.markdown("## Technical Context")

st.markdown(
    """
    __**Utilizing Datasets:**__ Our project will leverage two primary datasets to investigate global warming and climate disruption over the last few centuries and decades. These datasets play crucial roles in understanding the climate trends and their relation to greenhouse gas emissions.

    1. **CO2 and Greenhouse Gas Emissions Data (Our World in Data):** This dataset provides historical (and regional) records of carbon dioxide and greenhouse gas emissions. It is essential for understanding the human impact on the environment. We plan to utilize Python to process and clean this data, ensuring its accuracy and completeness.

    2. **Global Temperature Anomalies (NASA):** NASA's dataset contains detailed temperature anomalies, which are deviations from the 1951-1980 means. It includes global, hemispheric, and zonal monthly, seasonal, and annual temperature variations. We will utilize Python to preprocess this data, addressing missing values and ensuring data quality.
    """)

# Introduction - Data Cleaning with Python
st.markdown("### Data Cleaning with Python")

st.write(
    """To ensure the reliability of our analyses, we will use Python for data cleaning. This process will involve:\n\n 
**Handling Missing Data:** Our priority is identifying and addressing missing data points within both datasets. Missing values can significantly impact the integrity of our analyses. We will employ appropriate techniques to either fill in or amend these missing values. This step is pivotal in ensuring that our final dataset is as complete as possible.\n\n
**Column Renaming for Clarity:** We recognize that the clarity and understandability of our dataset are paramount. In pursuit of this, we will evaluate the column names in both datasets and consider renaming them if necessary. This will make the dataset more intuitive and user-friendly for our team and any stakeholders involved in the project.\n\n
**Data Type Verification:** Ensuring that data types align with the intended use of the dataset is vital. After merging the datasets, we will conduct a comprehensive check of column data types. This will help us identify any discrepancies and verify that the data types (integers, objects, floats) are appropriate for our analyses.\n\n
**Data Transformations:** As we aim to assess global warming in the context of the goal to limit the increase to "1.5ºC above pre-industrial levels," data transformation may be necessary. This transformation is particularly relevant to the NASA dataset, which presents temperature anomalies concerning a different time period. Adjusting the data to match the desired reference is essential for our analysis's accuracy and relevance.\n\n
**Data Integration:** We will merge and harmonise data from the CO2 emissions dataset and NASA's temperature anomalies dataset. This will facilitate comprehensive analyses by linking emissions data with temperature trends.\n\n

    """)