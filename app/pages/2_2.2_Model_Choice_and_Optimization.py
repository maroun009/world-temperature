import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

st.markdown("## Model Choice and Optimization ")

st.markdown("### Exploring Regression Models")

st.markdown("""
Our regression task, aimed at predicting temperature changes, involved a thorough exploration of different machine learning algorithms. Ultimately, we selected three distinct regression models for evaluation: Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
""")

st.markdown("### Linear Regression")

st.markdown("""
Linear Regression is one of the simplest yet fundamental regression models. It operates under the assumption of a linear relationship between the independent variables (features) and the dependent variable (target). In our case, it assumed a linear association between various environmental and emissions-related features and the continuous target variable, "Temp_change." \n
Linear Regression is easy to understand and interpret. It provides coefficients for each feature, which quantifies their impact on the target variable. We employed it as a baseline model to establish a benchmark for prediction performance.
""")

st.markdown("### Decision Tree Regressor")

st.markdown("""
Decision Tree Regressor is a non-linear model that partitions the dataset into subsets based on the feature values, creating a tree-like structure to make predictions. It is well-suited for capturing non-linear relationships in the data.\n
Decision trees are capable of modelling complex interactions between features and the target variable. However, they are prone to overfitting. The Decision Tree Regressor was included to investigate its performance and check whether it could capture intricate patterns in the temperature change data.
""")

st.markdown("### Random Forest Regressor")

st.markdown("""
Random Forest is an ensemble learning method that extends Decision Trees by aggregating multiple trees to improve predictive accuracy and reduce overfitting. It is particularly powerful in handling noisy and complex datasets. Furthermore, Random Forest can capture both linear and non-linear relationships, making it a versatile choice. Due to its robustness and ability to handle high-dimensional data, we included it as one of the primary models to predict temperature changes.
After initial evaluation, Random Forest outperformed other models on the test set, emphasising its potential to deliver accurate predictions.
""")

st.markdown("### Model Selection")

st.markdown("""
Three regression models are chosen for evaluation: Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
""")

st.markdown("### Model Evaluation")

st.markdown("""
Model performance is assessed using the coefficient of determination (R-squared) on both the training and testing datasets. Additional metrics, such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), are calculated to assess model performance.
""")

greenhouse_gas = Image.open("app/img/ModelEvaluation.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ModelEvaluation1.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Hyperparameter Optimization")

st.markdown("""
Linear Regression: Betsi performed hyperparameter tuning to fine-tune the Linear Regression model using GridSearchCV, and the best hyperparameters and R-squared scores for the models are reported.
""")

greenhouse_gas = Image.open("app/img/LinearRegression.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("""
Random Forest: Similar hyperparameter optimisation is applied to the Random Forest model to identify the best hyperparameters and their impact on model performance.
""")

greenhouse_gas = Image.open("app/img/RandomForest.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Model Improvement")

st.markdown("""
The models are retrained with the best hyperparameters to assess any improvements in performance. Feature selection is introduced as a strategy to mitigate overfitting, focusing on the most important variables. The Random Forest model is retrained on this reduced dataset, resulting in notable reductions in overfitting.
""")

greenhouse_gas = Image.open("app/img/ModelImprovement.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ModelImprovementGraph.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Predicting Temperature Changes for Future Years")

st.markdown("""
A dataset for future years (2022 to 2041) is constructed, assuming that historical trends since the year 2000 will continue. The same preprocessing steps, including imputation and feature scaling, are applied to this future dataset. The Random Forest model is used to predict "Temp_change" for these future years.
""")

greenhouse_gas = Image.open("app/img/PredictingTempChange.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Combining Known and Future Data")

st.markdown("""
The known and future data are combined by concatenating the known data (X_train and X_test) for both features and the target variable. The Random Forest model is retrained on the entire known dataset, further enhancing its predictive capabilities.
""")

greenhouse_gas = Image.open("app/img/CombiningKnownData.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Future Predictions")

st.markdown("""
The retrained model is utilised to predict "Temp_change" for future years (2023 to 2042). The results are presented in a DataFrame, showcasing the temperature change predictions for the years 2023 to 2042.
""")

greenhouse_gas = Image.open("app/img/FuturePredictions.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Feature Selection")

st.markdown("""
Five important variables ("Year," "oil_co2," "coal_co2," "cement_co2," "gas_co2," and "co2") are selected for further analysis. A reduced dataset is created using these selected features for both training and testing data.\n
These selected attributes formed the foundation of a streamlined dataset, employed for both training and testing. Additionally, the preprocessing procedures, such as imputation and feature scaling, remained consistent with those applied to the original data. This process led to the training of a Random Forest Regressor model on the refined dataset. In this context, coefficients of determination (R-squared) were calculated to assess the model's performance on both training and test datasets. Subsequently, hyperparameter optimization for the Random Forest model was a pivotal focus, utilising GridSearchCV to fine-tune its parameters on the trimmed dataset.
""")

st.markdown("### Future Data and Predictions")

st.markdown("""
A forward-looking perspective was adopted to predict temperature changes in future years. A dataset spanning from 2022 to 2041 was crafted, making the assumption that historical trends observed since 2000 would persist. The same rigorous preprocessing steps, including imputation and feature scaling, were applied to this future dataset, ensuring its compatibility with the known data. Notably, the known data, comprising X_train and X_test for both features and the target variable (y_train and y_test), was seamlessly integrated with the future data. A pivotal development was the retraining of a new Random Forest Regressor model, denoted as rf3, on the comprehensive known dataset. This retrained model, rf3, was then harnessed to make predictions for temperature changes in future years, spanning from 2023 to 2042. To present these future predictions effectively, a well-structured DataFrame was constructed, encapsulating the "Year" and the corresponding projected "Temp_change" values, underscoring the project's capacity for forward-looking climate-related predictions.
""")

greenhouse_gas = Image.open("app/img/FutureDataTable.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Time Series Forecasting")

st.markdown("""
The type of machine learning problem involved in this scenario is Time Series Forecasting. Time series forecasting is the process of predicting future values based on historical time-ordered data. In this specific case, we are forecasting future temperature anomalies using historical temperature anomaly data.\n
Here's how we implemented time series forecasting using ARIMA (AutoRegressive Integrated Moving Average) in Python:\nœ
Data Loading \n
We loaded the historical temperature anomaly data from the provided CSV file, which contains two columns: 'Year' and 'J-D' (annual mean temperature anomaly).\n
Data Preprocessing
""")

st.markdown("""
* We converted the 'J-D' column to numeric data.
* Removed rows with missing values in the 'J-D' column.
""")

st.markdown("""
Model Fitting\n
We used ARIMA, a popular time series forecasting method, to fit a model to the preprocessed data. ARIMA has three main components: AutoRegressive (AR) order, Integrated (I) order, and Moving Average (MA) order. We used some initial values (p=1, d=1, q=1) for these hyperparameters.\n
Forecasting\n
We used the fitted ARIMA model to make future forecasts. We specified the number of time periods we wanted to forecast.\n
Visualisation
""")

st.markdown("""
* We created a plot to visualise the forecasted values against the years.
* We set the Y-axis to represent temperature anomalies in degrees Celsius and set Y-axis limits to make the temperature anomaly of 1.0 more visible.
* We added a legend to explain what the values on the Y-axis mean.
* Finally, we displayed the chart.
""")

st.markdown("""
The resulting chart shows the forecasted temperature anomalies for future years based on historical data. We feel that this time series forecasting is a fitting technique for making predictions in scenarios where data has a time-based structure, which is perfect for climate data.
""")

greenhouse_gas = Image.open("app/img/TemperatureAnomalyForecast.png")
st.image(greenhouse_gas)
st.markdown("")

