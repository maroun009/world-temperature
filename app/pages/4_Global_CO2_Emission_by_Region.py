import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

st.set_page_config(
    page_title="Global CO2 Emission by Region",
    page_icon="🌐",
)

st.markdown("# Global CO2 & Greenhouse Gas Emissions (Region)")
st.sidebar.header("Global CO2 & Greenhouse Gas Emissions (Region)")
st.write(
    """The following data displays the global annual temperatures by 
    latitudinal zones and hemispherical regions."""
)

df_co2 = pd.read_csv("data/owid-co2-data.csv")
df_co2.head()

df_co2["country"].unique()

selected_region = st.multiselect('Which region do you want?', ["North America", "Asia", "Europe", "World"])
if selected_region:
    df_co2_n = df_co2[df_co2["country"].isin(selected_region)]

    col1, space1, col2, space2, col3 = st.columns([1, 0.1, 1, 0.1, 1])
    col4, space3, col5, space4, col6 = st.columns([1, 0.1, 1, 0.1, 1])

    with col1:
        table = st.button("Table of CO2 Emissions by Region")

    with col2:
        share_contribution = st.button("Share Contribution to Global Warming")

    with col3:
        temp_increase = st.button("Contribution to Temperature Increase")

    with col4:
        annual_emission = st.button("Annual Total Carbon Dioxide Emission")

    with col5:
        emission_capita = st.button("Annual Total CO2 Emission Per Capita")

    with col6:
        temp_gdp = st.button("Temperature Change versus GDP")

    if table:
        st.dataframe(df_co2_n)

    if share_contribution:
        plt.figure(figsize = (10,7))
        df_co2_n_plot1 = sns.relplot(x = "year", y = "share_of_temperature_change_from_ghg", kind = "line", hue = "country", data = df_co2_n)
        plt.xlabel("Year")
        plt.ylabel("Contribution (%)")
        plt.title("Share of contribution to global warming")
        plt.show();

        st.pyplot(df_co2_n_plot1)

    if temp_increase:
        plt.figure(figsize = (10,7))
        df_co2_n_plot2 = sns.relplot(x = "year", y = "temperature_change_from_co2", kind = "line", hue = "country", data = df_co2_n)
        plt.xlabel("Year")
        plt.ylabel("Temperature change (ºC)")
        plt.title("Contribution to temperature increase due to CO2");

        st.pyplot(df_co2_n_plot2)

    if annual_emission:
        plt.figure(figsize = (12,8))
        df_co2_n_plot3 = sns.relplot(x = "year", y = "co2", kind = "line", hue = "country", data = df_co2_n)
        plt.xlabel("Year")
        plt.ylabel("CO2 (million tonnes)")
        plt.title("Annual total emissions of CO2");

        st.pyplot(df_co2_n_plot3)

    if emission_capita:
        plt.figure(figsize = (12,8))
        df_co2_n_plot4 =    sns.relplot(x = "year", y = "co2_per_capita", kind = "line", hue = "country", data = df_co2_n)
        plt.xlabel("Year")
        plt.ylabel("CO2 (million tonnes per person)")
        plt.title("Annual emissions of CO2 per capita");

        st.pyplot(df_co2_n_plot4)


    df_co2_n["gdp"] = df_co2_n['co2']/df_co2_n["co2_per_gdp"]

    if temp_gdp:
        if selected_region:
            # Here I obtained the GDP values from the other 2 variables as "gdp" column is empty for whole continents (but "co2" and "co2_per_gdp" not)
            g = sns.FacetGrid(df_co2_n, col = "country", hue = "country", height = 4)
            g.map(sns.scatterplot, "gdp", "temperature_change_from_co2")
            g.set_axis_labels("GDP", "Temperature change (ºC)")
            g.set_titles(col_template="Temperature change vs GDP")

            g.add_legend();

            st.pyplot(g)
else:
    st.write("Please select region!")
