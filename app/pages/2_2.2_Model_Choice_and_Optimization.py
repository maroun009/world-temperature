import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

st.markdown("## Model Choice and Optimization ")

st.markdown("### Exploring Regression Models")



st.markdown("### Linear Regression")



st.markdown("### Decision Tree Regressor")


st.markdown("### Random Forest Regressor")



st.markdown("### Model Selection")


st.markdown("### Model Evaluation")



greenhouse_gas = Image.open("app/img/ModelEvaluation.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ModelEvaluation1.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Hyperparameter Optimization")


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



greenhouse_gas = Image.open("app/img/ModelImprovement.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ModelImprovementGraph.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Predicting Temperature Changes for Future Years")



greenhouse_gas = Image.open("app/img/PredictingTempChange.png")
st.image(greenhouse_gas)
st.markdown("")



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

