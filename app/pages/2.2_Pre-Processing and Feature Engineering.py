import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

# Introduction - Data Cleaning and Processing Steps
st.markdown("## Data Cleaning and Processing Steps:")

st.markdown(
    """Our project involves a comprehensive data pre-processing and feature engineering phase, executed using Python. This pivotal stage ensures that the dataset is refined and optimised for our subsequent analyses. Below are the key steps involved:\n\n
Data Cleaning\n\n\n\n
●	Handling Missing Data: We identified and addressed any missing data points in our datasets. This will be achieved by employing various techniques, such as imputation or interpolation, to maintain data integrity. Additionally, we will use the fillna method to replace missing values and various statistical methods to inform our decisions.\n\n
●	**Outlier Detection and Treatment:** Outliers can significantly impact our analyses. We made use of the IQR (Interquartile Range) to detect outliers. Data points outside a defined range beyond the upper and lower quartiles were considered outliers.\n\n
●	**Duplications:** Duplicates in the dataset can lead to inaccuracies. We will utilise the duplicated and drop_duplicates methods to identify and remove duplicate records, ensuring data consistency.\n\n
●	**Modifying Data:** We will use the replace method to modify elements of the DataFrame, potentially changing data types with the astype method. Additionally, we may rename columns to enhance readability and comprehension.\n\n
●	**Applying Functions:** The apply method, in conjunction with lambda functions, will allow us to apply specific operations to the DataFrame, further enhancing data quality.\n\n """)

# Introduction - Data Integration
st.markdown("### Data Integration")

st.write("""
●	**Merging Datasets:** Since our project involves the utilisation of data from different sources, we will merge these datasets into a unified and cohesive dataset. This step may require joining operations and concatenation to bring together relevant information from various files.\n\n
Here is an example of how we performed a standardisation process, in this case, a baseline shift.\n\n
● **Filtering the Data:**\n
Firstly, we filtered the temperature anomaly dataset (df_temp) to focus on the period between 1880 and 1900. This is the "pre-industrial" period defined.\n\n
● **Calculating the Average:**\n
After filtering, we calculated the average temperature anomalies (average) for this specified pre-industrial period.\n\n
**Shifting the Baseline:**\n
We subtracted this calculated average from all the temperature anomalies in the dataset. This shifts the baseline from the 1951-1980 period to the pre-industrial period (1880-1900). This subtraction aligns the temperature anomalies with the "pre-industrial" reference, allowing us to compare them with the target of a "1.5ºC maximum increase from the pre-industrial average."\n\n
The purpose of this baseline shift is to ensure that we’re comparing temperature anomalies consistently with the defined target. By setting the pre-industrial period as the new reference, we're aligning the analysis with the specific goal of understanding temperature changes concerning the pre-industrial era.\n\n
This is a crucial step in ensuring the relevance and accuracy of the analysis, especially when dealing with climate data that spans different reference periods. It helps to make the data more interpretable and relevant to our research objectives.\n\n
""")


# Introduction - Data Transformation:
st.markdown("### Data Transformation: ")

st.write("""
●	Temporal Alignment: Given the specific goal of assessing temperature anomalies concerning the "1.5ºC increase above pre-industrial levels," we will undertake data transformations. This will involve aligning the temporal aspect of our data to match this reference point, ensuring the relevance of our analyses.
""")



# Introduction - Consideration of dimension reduction techniques
st.markdown("### Consideration of dimension reduction techniques")

st.write("""
We initially considered utilising Principal Component Analysis as a dimension reduction technique but were not entirely confident on how to implement it in reality. However, here is our reasoning as to why it would have been effective against our datasets.
In our project, we may use PCA to reduce the dimensionality of the temperature and CO2 datasets. \n
Utilising PCA to transform a dataset with multiple variables (temperature and CO2 measurements for different locations and time points) into a new set of variables called principal components.
These new components could then have been used to identify the principal components in such a way that the first component explains the maximum variance in the data, the second component explains the second most variance, and so on. We could then have chosen to retain a subset of the principal components that capture most of the data's variance, effectively reducing the dimensionality.\n\n

We wanted to use Principal Component Analysis (PCA) because of the numerous benefits for our climate data analysis. Firstly, it enables effective dimension reduction, reducing the complexity of the dataset by retaining only the most informative principal components while eliminating less important variables. Secondly, PCA acts as a noise reduction tool, filtering out irrelevant data fluctuations and enhancing the focus on significant climate patterns and trends. Moreover, PCA aids in data visualisation, allowing analysts to uncover hidden spatial or temporal patterns not immediately evident in the raw data. Lastly, when certain principal components strongly correlate with temperature or CO2 trends, PCA facilitates feature selection, simplifying the interpretation of results and offering more clarity in climate research and analysis.\n\n
""")






