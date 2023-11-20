import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

# Introduction - Technical Context
st.markdown("## Technical Context")

st.markdown("### Utilizing Datasets")

st.markdown(
    """
    **Our project will leverage two primary datasets to investigate global warming and climate disruption over the last few centuries and decades. These datasets play crucial roles in understanding the climate trends and their relation to greenhouse gas emissions.

    1. **CO2 and Greenhouse Gas Emissions Data (Our World in Data):** This dataset provides historical (and regional) records of carbon dioxide and greenhouse gas emissions. It is essential for understanding the human impact on the environment. We plan to utilize Python to process and clean this data, ensuring its accuracy and completeness.

    2. **Global Temperature Anomalies (NASA):** NASA's dataset contains detailed temperature anomalies, which are deviations from the 1951-1980 means. It includes global, hemispheric, and zonal monthly, seasonal, and annual temperature variations. We will utilize Python to preprocess this data, addressing missing values and ensuring data quality.
    """)

greenhouse_gas = Image.open("app/img/GreenHouseGasesPollution.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Data Cleaning with Python
st.markdown("### Data Cleaning with Python")

st.write("""To ensure the reliability of our analyses, we will use Python for data cleaning. This process will involve:\n\n 
* **Handling Missing Data:** Our priority is identifying and addressing missing data points within both datasets. Missing values can significantly impact the integrity of our analyses. We will employ appropriate techniques to either fill in or amend these missing values. This step is pivotal in ensuring that our final dataset is as complete as possible.\n\n
* **Column Renaming for Clarity:** We recognize that the clarity and understandability of our dataset are paramount. In pursuit of this, we will evaluate the column names in both datasets and consider renaming them if necessary. This will make the dataset more intuitive and user-friendly for our team and any stakeholders involved in the project.\n\n
* **Data Type Verification:** Ensuring that data types align with the intended use of the dataset is vital. After merging the datasets, we will conduct a comprehensive check of column data types. This will help us identify any discrepancies and verify that the data types (integers, objects, floats) are appropriate for our analyses.\n\n
* **Data Transformations:** As we aim to assess global warming in the context of the goal to limit the increase to "1.5ºC above pre-industrial levels," data transformation may be necessary. This transformation is particularly relevant to the NASA dataset, which presents temperature anomalies concerning a different time period. Adjusting the data to match the desired reference is essential for our analysis's accuracy and relevance.\n\n
* **Data Integration:** We will merge and harmonise data from the CO2 emissions dataset and NASA's temperature anomalies dataset. This will facilitate comprehensive analyses by linking emissions data with temperature trends.\n\n
""")

# Introduction - Data Visualization Tools:
st.markdown("### Data Visualization Tools: ")
st.write("""To analyse and visualise the data, we will employ a combination of data visualisation tools, including Seaborn, Plotly, and Microsoft Power BI. These tools offer diverse visualisation options and will enable us to present our findings effectively.\n\n
    """)

greenhouse_gas = Image.open("app/img/TreeDataGraph.jpeg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Project Objectives:
st.markdown("### Project Objectives: ")

st.write("""Our primary objective is to answer the following key questions:\n\n
1.	**Global Climate Trends:** We will analyse global temperature anomalies over the past 100 years and since the year 2000, allowing us to assess long-term and recent climate changes.\n\n
2.	**Geographical Analysis:** We will perform a geographical analysis of Europe, USA and China to identify regional climate variations and their correlation with emissions data, considering both the past 100 years and since 2000.\n\n
3.	**Comparison with Historical Phases:** Our project will compare the current temperature anomalies with historical climate phases, particularly focusing on the past 100 years and since the year 2000 till present. This comparison will shed light on the extent of global warming and climate disruption and potential future outlook.\n\n
\n\n
""")
# Introduction - Technical Challenges:
st.markdown("### Technical Challenges: ")
st.write("""
1.	**Data Integration:** Combining datasets from different sources and formats, such as CO2 emissions data and temperature anomalies, can be challenging. Ensuring data consistency and accuracy during integration is crucial.\n\n
2.	**Data Quality:** Cleaning and preprocessing large datasets, especially handling missing data and outliers, can be time-consuming and may require advanced data cleaning techniques.\n\n
3.	**Data Volume:** Large volumes of historical climate and emissions data may pose challenges in terms of storage, processing, and computational requirements.\n\n
4.	**Complex Analysis:** Analysing temperature anomalies, emissions data, and their correlations across various geographical regions and timeframes can be technically complex.\n\n
5.	**Data Visualization:** Effectively visualising complex climate data and trends using tools like Seaborn, Plotly, and Microsoft Power BI requires expertise in data visualisation and interpretation.\n\n""")

# Introduction - Technical Opportunities:
st.markdown("### Technical Opportunities: ")
st.write("""
1.	**Advanced Tools:** Leveraging advanced data analysis tools, such as Python, Seaborn, and Plotly, presents an opportunity to create meaningful visualisations and insights.\n\n
2.	**Machine Learning:** We “may” explore the potential of machine learning techniques to predict climate trends, identify patterns, or optimise data preprocessing.\n\n
3.	**Big Data Solutions:** If dealing with large datasets, you can explore big data technologies and cloud computing solutions to handle data storage, processing, and analysis efficiently.\n\n
4.	**Open Data Resources:** The availability of open data resources, such as NASA's climate datasets and Our World in Data, provides a valuable opportunity for comprehensive climate analysis.\n\n
5.	**Interdisciplinary Insights:** Collaborating with experts in climate science, data science, and domain-specific fields can enrich the project with diverse insights and methodologies.\n\n
""")

greenhouse_gas = Image.open("app/img/CarbonFootprint.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Economic Context:
st.markdown("## Economic Context:  ")
st.write("""
This project, which focuses on the analysis of global climate data and greenhouse gas emissions, has several economic implications. Some of the economic benefits of this project in regards to the information that it is helping to disseminate to companies specifically within the European Union are highlighted below. There are several hypothesised advantages for corporations acting in an environmentally friendly manner:\n\n""")

# Introduction - Economic Implications
st.markdown("### Economic Implications: ")
st.write("""
1.	**Cost Savings:** By analysing data related to greenhouse gas emissions, European companies can identify opportunities to reduce energy consumption and emissions. Implementing energy-efficient practices and technologies can lead to significant cost savings in the long run. This aligns with the economic goal of reducing operational expenses.\n\n
2.	**Regulatory Compliance:** European companies are subject to stringent environmental regulations and emissions targets. This project can help companies ensure compliance with these regulations, avoiding potential fines and legal issues that may impact their financial stability.\n\n
3.	**Reputation and Branding:** Environmental responsibility is increasingly important to consumers and investors. European companies that are environmentally friendly and transparent in their sustainability efforts can enjoy a positive brand image. This can lead to increased customer loyalty and, in turn, higher revenues.\n\n
4.	**Innovation and Competitive Advantage:** Companies that invest in sustainable practices and technologies are often at the forefront of innovation. Your project may identify innovative ways to reduce emissions and resource usage, which can provide a competitive advantage in the European market.\n\n
5.	**Access to Green Markets:** European companies that prioritise sustainability can access green markets and attract environmentally conscious customers. These markets often offer premium pricing for eco-friendly products and services, potentially increasing revenue.\n\n
6.	**Reduced Supply Chain Risks:** Companies can use data-driven insights from your project to assess and reduce environmental risks in their supply chains. This can result in better risk management and cost reduction, positively impacting their financial stability.\n\n
7.	**Investor Attraction:** Many investors are looking for socially responsible and environmentally sustainable companies to invest in. Your project's findings can attract responsible investors who see long-term financial potential in green and eco-friendly businesses.\n\n""")


greenhouse_gas = Image.open("app/img/AutumLeaves.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Scientific Context:
st.markdown("## Scientific Context:  ")
st.write("""By exploring historical temperature data and examining contemporary climate trends, we aim to contribute to scientific understanding in a field with immense scientific relevance. Our findings will provide valuable insights for climate scientists and researchers working toward a more comprehensive understanding of the effects of global climate change. The scientific aspects of our project revolve around several key elements:\n\n
**Climate Science and Data Analysis:** Our project is rooted in the field of climate science. We utilise scientific principles and methodologies to analyse extensive datasets, such as NASA's Land-Ocean Temperature Index (L-OTI). These datasets contain valuable information about temperature anomalies and deviations from the 1951-1980 means. Our analysis involves statistical methods and data visualisation techniques to uncover patterns, trends, and anomalies in global climate data.\n\n
**Understanding Climate Change:** Climate change is a critical scientific topic with far-reaching implications. Our project aims to contribute to a deeper understanding of climate change by exploring historical temperature data. We examine variations over the past century and the last three decades. By doing so, we seek to identify and quantify the effects of global warming and climate disruption.\n\n
**Scientific Relevance:** Our project is highly relevant in the field of climate science and environmental studies. It aligns with ongoing scientific research to monitor and comprehend the impacts of climate change on a global scale. By analysing data from the past and recent decades, we contribute to the broader scientific knowledge base focused on global climate trends and variability.\n\n
**Data-Driven Insights:** We leverage scientific methodologies for data preprocessing and feature engineering. This involves cleaning and enhancing the datasets to ensure accuracy and reliability. We also use data visualisation techniques to present scientific findings in a comprehensible manner.\n\n
**Contribution to Scientific Knowledge:** Our project seeks to make a meaningful contribution to scientific knowledge by providing insights into global climate changes. The analysis will reveal how different geographical areas are affected and how these changes compare to previous temperature phases. These findings add to the body of evidence supporting climate science research.\n\n
""")

greenhouse_gas = Image.open("app/img/CO2.jpeg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Our Roles:\n
st.markdown("## Our Roles")


st.markdown("### Objectives")
st.write("""
**Analysis at Global Level:** Our primary objective is to analyse global temperature changes over two specific periods – the past 100 years and since the year 2000. We will investigate temperature anomalies, trends, and variations during these periods.\n\n
**Geographical Area Analysis:** In addition to a global analysis, we will focus on specific geographical areas to assess regional climate trends and variations during the same time frames.\n\n
**Comparison with Previous Phases:** We intend to compare the current temperature trends with historical climate phases, specifically examining the past 100 years and since 2000. This comparative analysis will provide insights into the changes in the Earth's climate.\n\n
""")

st.markdown("### Our team consists of members with complementary skills and expertise")

st.write("""
**Chris:**   Chris is an expert in data visualisation and storytelling using Microsoft Power BI. His role is to create visually compelling and informative reports and dashboards that effectively communicate the insights derived from the data. Chris's skills in Power BI will be instrumental in presenting the project's findings.\n\n
**Betsi:** Betsi is proficient in Python, with a focus on data querying and cleaning using Pandas. She will be responsible for acquiring, cleaning, and preprocessing the climate data. Betsi's expertise in Python, along with her knowledge of data visualisation libraries such as Seaborn and Plotly, will be valuable for the analysis and visualisation phases.\n\n
**Maroun:** Maroun specialises in data preprocessing and statistical analysis. His role is to prepare the data for analysis, including tasks like data cleaning, handling missing values, and addressing outliers. Maroun's statistical analysis skills will be crucial for deriving meaningful insights from the dataset.\n\n
Each of our team member's expertise aligns with their respective roles, ensuring a well-structured approach to the project. Our clear objectives guide the entire project, from data preprocessing to analysis and visualisation, and will help us achieve meaningful outcomes in understanding climate change trends. Effective collaboration among the team members will be essential to meet our project objectives.\n\n
""")

