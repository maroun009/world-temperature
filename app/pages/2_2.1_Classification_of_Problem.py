import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

st.markdown("## Classification of the Problem")

st.markdown("### Machine Learning Type")

st.markdown("""
The machine learning problem in our project falls into the category of regression. Regression is a type of supervised learning where the objective is to predict a continuous numerical output. In our case, we are predicting temperature changes, which are represented as a continuous variable, "Temp_change." The goal is to model the relationship between various environmental and emissions-related features and the continuous target variable, allowing us to forecast temperature changes over time. Regression is the most suitable approach for this problem since it enables us to make quantitative predictions about temperature variations, making it a regression-based machine learning task.
""")

st.markdown("### Predicting Temperature Changes")

st.markdown("""
For this part of the project, in Predicting Temperature Changes we attempt to utilise regression machine learning with the primary objective of forecasting temperature changes, specifically the "Temp_change" variable. Our dataset, "owid-co2-data.csv," comprises a comprehensive collection of metrics meticulously maintained by Our World in Data, encompassing a wide array of CO2 and Greenhouse Gas Emissions data.
""")

st.markdown("### Data Preprocessing")

st.markdown("""
Data Separation: The dataset is separated into features (X) and the target variable ("Temp_change," y). Which is then further split into training and testing subsets using the train_test_split function.
""")

greenhouse_gas = Image.open("app/img/DataSeparation.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("""
Dealing with Missing Values: Missing values in the dataset are handled using the SimpleImputer class, which replaces missing values with the median value for each column. The Median imputation was chosen due to it’s robustness to extreme values.
""")

greenhouse_gas = Image.open("app/img/MissingValues.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("""
Feature Scaling: Feature scaling is performed using the StandardScaler to rescale numerical variables so they are comparable on a common scale. This preprocessing step ensures that features are standardised and prevents certain features from dominating others due to their scales.
""")

greenhouse_gas = Image.open("app/img/FeatureScaling.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Choice of Primary Performance Metric")

st.markdown("""
The choice of a primary performance metric is very important for us in evaluating regression models as it determines how well the model's predictions align with the actual target values. In our project, we have opted to use R-squared as we believe it possesses many attributes valuable our project question.\n
R-squared is a widely recognized and interpretable metric. It quantifies the proportion of the variance in the target variable (in this case, "Temp_change") that can be explained by the independent variables (features) included in the regression model. This explanation is expressed as a value between 0 and 1, where 1 indicates that the model perfectly explains the variance in the target variable. This makes it easy to understand and communicate the model's performance to both technical and non-technical stakeholders. \n
Furthermore, R-squared is particularly well-suited for regression tasks. In regression, the objective is to model and predict continuous numerical values. Unlike classification tasks where you assess model performance based on accuracy, precision, or recall, regression focuses on estimating and explaining the variability in the target variable. R-squared aligns perfectly with this objective by quantifying how well the model captures this variability.\n
R-squared also provides a comprehensive evaluation of how well the our models fit the data. It helps us determine whether the model's predictions are consistent with the actual values and whether it captures the underlying trends and patterns within the dataset. A high R-squared value implies that a significant portion of the variance is explained by the model, indicating a good fit, while a lower value suggests room for improvement.
""")

st.markdown("### Additional Performance Metrics for Comprehensive Model Evaluation")

st.markdown("""
We also utilised additional performance metrics alongside R-squared (coefficient of determination) to comprehensively evaluate our regression models. These additional metrics include Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). MAE measures the average absolute differences between the actual and predicted values, providing insight into the models' overall accuracy. MSE quantifies the average squared differences between actual and predicted values, emphasising the significance of larger errors. RMSE is the square root of MSE, giving a metric in the same unit as the target variable, which helps in understanding the scale of prediction errors. These supplementary metrics were employed to gain a more detailed perspective on our models' performance, offering valuable insights into different aspects of prediction accuracy and errors.
""")