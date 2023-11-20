import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

st.markdown("## Interpretation of Results")

st.markdown("### Analysis of Regression Model Errors")

st.markdown("""
The analysis of errors in our regression models played a pivotal role in understanding the limitations and areas of improvement for each model. By delving into the errors, we gained valuable insights into the models' performance and identified opportunities for refinement. Our error analysis consisted of the following key components:
""")

st.markdown("### Residual Analysis")

st.markdown("""
We began by examining the residuals, which are the differences between the actual temperature changes and the predictions made by our models. This analysis allowed us to identify patterns and trends in the errors. It was essential to scrutinise whether the residuals exhibited any systematic bias, such as consistently overestimating or underestimating temperature changes.
""")

greenhouse_gas = Image.open("app/img/ResidualAnalysis.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Outlier Detection")

st.markdown("""
We utilised various outlier detection techniques to identify observations that significantly contributed to high error rates. Isolating and understanding the outliers were essential for addressing extreme cases and ensuring that the models were not unduly influenced by a small number of unusual data points.
""")

greenhouse_gas = Image.open("app/img/OutliarDetection.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Model Refinements")

st.markdown("""
The insights gained from the analysis of errors played a pivotal role in making necessary refinements to our regression models. For example, if the errors demonstrated a systematic pattern, such as consistently underestimating temperature changes during certain periods, we could adjust the model to account for this bias. Addressing outlier data points and conducting feature engineering were also integral to our error-driven model improvements.\n
By systematically identifying, analysing, and addressing errors, we aimed to enhance the accuracy and reliability of our regression models for predicting temperature changes. This iterative process of error analysis and model refinement was crucial in ensuring that our models could make more precise and meaningful climate-related predictions.
""")

st.markdown("### Challenges in Predicting Climate-Related Variables")

st.markdown("""
We found the need to explain why some of our predictions fell flat or did not do a good enough job in application. Predicting climate-related variables such as temperature changes, CO2 levels, and other environmental factors is a complex and challenging task. A number of factors contribute to the inherent difficulty in making accurate predictions in the field of climate science and environmental modelling:\n
Complexity of Climate Systems: \n
Earth's climate systems are incredibly complex and dynamic, characterised by countless interrelated components. Climate patterns are influenced by factors such as solar radiation, atmospheric circulation, ocean currents, land surface properties, and greenhouse gas concentrations. These intricate interactions make it challenging to model and predict climate changes accurately.\n
Feedback Mechanisms: \n
Climate systems include feedback mechanisms, where changes in one component can trigger a cascade of effects throughout the system. For example, an increase in global temperatures can lead to the melting of polar ice caps, which, in turn, influences sea levels, ocean currents, and weather patterns. Understanding and modelling these feedback loops accurately is a formidable challenge.\n
Long-Term Projections: \n
Climate change involves making long-term projections, often spanning decades or centuries. Predicting how various factors will evolve over extended time frames is inherently uncertain, as it requires making assumptions about future developments in technology, policy, and human behaviour.\n
Inherent Variability: \n
Natural climate variability, such as El Niño and La Niña events, volcanic eruptions, and solar cycles, can introduce short-term fluctuations in climate patterns. Distinguishing between natural variability and long-term climate change signals is a complex task.\n
""")

st.markdown("### Algorithm Selection")

st.markdown("""
To thoroughly evaluate the performance of our predictive models for temperature changes and assess the potential issues related to their predictions. Our model evaluation results provided us with valuable insights into how well each model was performing, ultimately highlighting the superiority of the Random Forest model in comparison to the other two models. This conclusion was drawn based on the highest coefficient of determination (R-squared) observed on the test set, signifying a better fit to our training data.\n
Despite the Random Forest model's promising performance, a concern was raised regarding its predictions for future years. It became apparent that these predictions remained remarkably consistent and did not show any significant variation, suggesting a potential issue in how the model was handling future data points. In response to this concern, we decided to delve deeper into the model's behaviour and address this issue.\n
Upon closer examination, it became clear that the reason behind the lack of variation in future predictions was rooted in the way we had constructed our training and testing datasets. Specifically, we had inadvertently used the same dataset for both training and future predictions. In other words, the model was being tested on data that it had already been exposed to during training, making the test set not truly representative of unseen data.\n
To rectify this problem and obtain a more accurate assessment of our model's generalisation capabilities, we decided to implement a critical change. We realised that it was essential to utilise a separate dataset for making predictions about future temperature changes. By doing so, we ensured that the model was confronted with data it had never encountered before, simulating a more realistic scenario akin to forecasting real-world temperature trends.\n
This adjustment aimed to enhance the reliability and credibility of our model's predictions for future years. It allowed us to gauge the model's ability to adapt to unforeseen variations and make forecasts that would stand up to the test of time. In conclusion, by implementing this crucial modification and ensuring the use of a distinct dataset for future predictions, we aimed to address the issue of unchanging predictions and enhance the overall robustness of our temperature change forecasting model.
""")

st.markdown("### Hyperparameter Tuning for Linear Regression")

st.markdown("""
We harnessed the GridSearchCV technique to fine-tune the hyperparameters of our Linear Regression model. Specifically, we explored the 'fit_intercept' and 'copy_X' hyperparameters through a grid search. Our goal was to identify the ideal combination of these hyperparameters that would maximise the R-squared score, an indicator of how well the model fits the data.
""")


st.markdown("### Hyperparameter Tuning for Random Forest Regression")

st.markdown("""
Much like the Linear Regression process, we utilised GridSearchCV to tune hyperparameters for our Random Forest model. Our hyperparameters of interest for the Random Forest model encompassed the following:
""")

st.markdown("""
* 'n_estimators': The number of trees within the forest.
* 'max_depth': The maximum depth of each tree.
* 'min_samples_split': The minimum number of samples needed to split an internal node.
* 'min_samples_leaf': The minimum number of samples required for a leaf node.
""")

st.markdown("""
Our grid search combed through various combinations of these hyperparameters to pinpoint the set that would yield the highest R-squared score, ultimately optimising our model.
""")

st.markdown("""
Feature Selection:\n
Following the fitting of our Random Forest model, we applied a feature importance technique to select the most significant features while mitigating overfitting. This process enabled us to train a Random Forest model on a reduced set of features, enhancing the model's performance.
""")

greenhouse_gas = Image.open("app/img/FeatureSelection.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("""
Predicting Future Temperature Changes: Our project extended to forecasting future temperature changes. We crafted a dataset that included future values for CO2 emissions and deployed our Random Forest model to predict temperature changes in forthcoming years.\n
However, it's important to note that the predictions for future temperature changes generated the same value for all future years. Several factors could contribute to this outcome, including the assumption that historical trends will persist, or the possibility that our model isn't well-suited for long-term extrapolation into the future.\n
To enhance our predictions for future years, we might benefit from employing more sophisticated methods, such as time series forecasting techniques or models tailored explicitly for long-term climate predictions.
""")

st.markdown("### Exploring Time Series Analysis and Forecasting Techniques")

st.markdown("""
In the time series notebook, Betsi explored time series analysis and forecasting techniques. Initially, she focused on analysing global temperature anomalies and conducted a seasonal decomposition analysis to understand potential seasonality patterns in the data. She then performed differencing and autocorrelation analysis to assess stationarity and then attempted to fit an ARIMA(3,1,2) model, which didn't produce satisfactory results. \n
Subsequently, she investigated a SARIMA(3,1,1) model and found it more promising, particularly with the consideration of seasonality. She conducted forecasts up to 2042 and visualised the results, considering an external factor (CO2 data) for improved predictions. \n
Furthermore, she explored the use of monthly temperature data and applied the Prophet model for forecasting temperature anomalies up to 2042, presenting the results with visualizations. These techniques provided valuable insights into time series modeling and forecasting, including the importance of seasonality and exogenous factors in improving predictions. 
""")

greenhouse_gas = Image.open("app/img/ExploringTime.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ExploringTime1.png")
st.image(greenhouse_gas)
st.markdown("")