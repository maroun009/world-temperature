import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

st.set_page_config(
    page_title="CO2 Emissions & Temperature Anomalies",
    page_icon="🌐",
)

st.markdown("# CO2 Emissions & Temperature Anomalies")
st.sidebar.header("CO2 Emissions & Temperature Anomalies")
st.write(
    """The following compares carbon dioxide emissions with temperature
    anomalies."""
)

# Load the CO2 emissions data (owid-co2-data.csv)
co2_data = pd.read_csv('data/owid-co2-data.csv')

# Load the temperature data (GLB.Ts+dSST.csv)
temperature_data = pd.read_csv('data/GLB.Ts+dSST.csv', skiprows=1)  # Skip the first row

# Data Distribution Analysis for CO2 Emissions
co2_description = co2_data.describe()
co2_mean = co2_data['co2'].mean()
co2_median = co2_data['co2'].median()
co2_mode = co2_data['co2'].mode().values[0]
co2_std = co2_data['co2'].std()
co2_range = co2_data['co2'].max() - co2_data['co2'].min()
co2_iqr = co2_data['co2'].quantile(0.75) - co2_data['co2'].quantile(0.25)

# Data Distribution Analysis for Temperature Anomalies
temperature_description = temperature_data.describe()
temperature_mean = temperature_data['J-D'].mean()
temperature_median = temperature_data['J-D'].median()
temperature_mode = temperature_data['J-D'].mode().values[0]
temperature_std = temperature_data['J-D'].std()
temperature_range = temperature_data['J-D'].max() - temperature_data['J-D'].min()
temperature_iqr = temperature_data['J-D'].quantile(0.75) - temperature_data['J-D'].quantile(0.25)

col1, space1, col2, space2, col3 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    graph = st.button("CO2 Emission & Temp Anomalies Graph")

with col2:
    co2_emission = st.button("Carbon Dioxide Emission Statistics")

with col3:
    temp_anomalies = st.button("Temperature Anomalies Statistics")

if graph:
    # Data Visualization
    plot1 = plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.yscale("log")
    sns.histplot(data=co2_data, x='co2', kde=True)
    plt.title("CO2 Emissions Distribution (log scale)")

    plt.subplot(1, 2, 2)
    sns.histplot(data=temperature_data, x='J-D', kde=True)
    plt.title("Temperature Anomalies Distribution")

    plt.show()

    st.pyplot(plot1)

# Print Data Distribution Summary
if co2_emission:
    st.write("Summary Statistics for CO2 Emissions:")
    st.write(co2_description)
    st.write(f"Mean: {co2_mean:.2f}, Median: {co2_median:.2f}, Mode: {co2_mode:.2f}")
    st.write(f"Standard Deviation: {co2_std:.2f}, Range: {co2_range:.2f}, IQR: {co2_iqr:.2f}")

if temp_anomalies:
    st.write("\nSummary Statistics for Temperature Anomalies:")
    st.write(temperature_description)
    st.write(f"Mean: {temperature_mean:.2f}, Median: {temperature_median:.2f}, Mode: {temperature_mode:.2f}")
    st.write(f"Standard Deviation: {temperature_std:.2f}, Range: {temperature_range:.2f}, IQR: {temperature_iqr:.2f}")

st.divider()

st.write("This section provides graphs of each category and their corresponding count")

cols = ["population", "gdp", "co2", "co2_per_capita", "co2_per_gdp"]

category = st.selectbox("Select graph data by category: ", cols)

plt.figure(figsize=(10, 7))
cat = sns.displot(co2_data[category], kde=True)
plt.xlabel(category)
plt.ylabel("Count")
plt.title("Count of " + category)
plt.legend();

st.pyplot(cat)

co2_data.boxplot(cols)
plt.show();
