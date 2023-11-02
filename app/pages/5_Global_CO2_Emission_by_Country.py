import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

st.set_page_config(
    page_title="Global CO2 Emission by Country",
    page_icon="🌐",
)

st.markdown("# Global CO2 & Greenhouse Gas Emissions (Country)")
st.sidebar.header("Global CO2 & Greenhouse Gas Emissions (Country)")
st.write(
    """The following data displays the global annual temperatures by 
    country."""
)

df_co2 = pd.read_csv("data/owid-co2-data.csv")

# Since GDP and population seem to positively correlate with Co2 emissions and temperature increase, let's focus on some big and/or rich countries.
selected_region = st.multiselect('Which country do you want?', ["United States", "Canada", "Germany", "France", "Russia", "China", "India", "Brazil", "Australia"])
if selected_region:
    df_co2_country = df_co2[df_co2["country"].isin(selected_region)]

    # We can see that the Northern Hemisphere has surpased the 1.5ºC "limit" a couple of times. It's also interesting to see a seasonality in the data...

    col1, space1, col2, space2, col3, space3, col4 = st.columns([1, 0.1, 1, 0.1, 1, 0.1, 1])

    with col1:
        temp_increase = st.button("Contribution to Temperature Increase")

    with col2:
        annual_emission = st.button("Annual Total Carbon Dioxide Emission")

    with col3:
        emission_capita = st.button("Annual Total CO2 Emission Per Capita")

    with col4:
        temp_change = st.button("Temperature Change Due to CO2")

    # Some graphs for the country dataset:

    if temp_increase:
        plt.figure(figsize=(10, 7))
        df_co2_country_plot1 = sns.relplot(x="year", y="temperature_change_from_co2", kind="line", hue="country", data=df_co2_country)
        plt.xlabel("Year")
        plt.ylabel("Temperature change (ºC)")
        plt.title("Contribution to temperature increase due to CO2");

        st.pyplot(df_co2_country_plot1)

    # United States is a big contributor to temperature increase due to CO2 emissions!

    if annual_emission:
        plt.figure(figsize=(12, 8))
        df_co2_country_plot2 = sns.relplot(x="year", y="co2", kind="line", hue="country", data=df_co2_country)
        plt.xlabel("Year")
        plt.ylabel("CO2 (million tonnes)")
        plt.title("Annual total emissions of CO2");

        st.pyplot(df_co2_country_plot2)

    if emission_capita:
        plt.figure(figsize=(12, 8))
        df_co2_country_plot3 = sns.relplot(x="year", y="co2_per_capita", kind="line", hue="country", data=df_co2_country)
        plt.xlabel("Year")
        plt.ylabel("CO2 (million tonnes per person)")
        plt.title("Annual emissions of CO2 per capita");

        st.pyplot(df_co2_country_plot3)

    # In the last few decades, China has been leading in total Co2 emissions, although on a per capita basis,
    # the United States was the leader throughout the last century.

    if temp_change:
        plt.figure(figsize=(10, 7))
        df_co2_country_plot4 = sns.relplot(x="gdp", y="temperature_change_from_co2", hue="country", data=df_co2_country)
        plt.xlabel("GDP")
        plt.ylabel("Temperature change (ºC)")
        plt.title("Temperature change due to CO2");

        st.pyplot(df_co2_country_plot4)
else:
    st.write("Please select country!")