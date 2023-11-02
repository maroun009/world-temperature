import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

st.set_page_config(
    page_title="Global Temperature by Zone",
    page_icon="🌐",
)

st.markdown("# Global Annual Temperature by Zone")
st.sidebar.header("Global Annual Temperature by Zone")
st.write(
    """The following data displays the global annual temperatures by 
    latitudinal zones and hemispherical regions."""
)

df_Zon = pd.read_csv("data/ZonAnn.Ts+dSST.csv")

col1, left, col2, right, col3 = st.columns([1, 0.1, 1, 0.1, 1])

with col1:
    table = st.button("Table of All Tempeature Data")

with col2:
    all_years = st.button("Temperature Anomalies (All Years)")

with col3:
    graph_after_1990 = st.button("Temperature Anomalies (Starting 1990)")

if table:
    st.write(df_Zon.head())

    df_temp = df_Zon[["Year", "Glob", "SHem", "NHem"]]

    filtered = df_temp[(df_temp['Year'] >= 1880) & (df_temp['Year'] <= 1900)]

    # Calculate the average temperature anomalies for the specified period
    average = filtered['Glob'].mean()

    # We can do the same with Northern and Sothern Hemispheres out of curiosity...
    st.text(f'Average temperature anomalies between 1880 and 1900: {average:.2f}')
    average_n = filtered['NHem'].mean()
    st.text(f'NHem-Average temperature anomalies between 1880 and 1900: {average_n:.2f}')
    average_s = filtered['SHem'].mean()
    st.text(f'SHem-Average temperature anomalies between 1880 and 1900: {average_s:.2f}')

if all_years:
    df_Zon_plot1 = plt.figure(figsize=(10, 7))
    sns.lineplot(x="Year", y="Glob", data=df_Zon, label="Global")
    sns.lineplot(x="Year", y="NHem", data=df_Zon, label="Northern Hemisphere")
    sns.lineplot(x="Year", y="SHem", data=df_Zon, label="Southern Hemisphere")
    plt.xlabel("Year")
    plt.ylabel("Temperature (ºC change)")
    plt.title("Temperature anomalies")
    plt.legend();

    st.pyplot(df_Zon_plot1)

if graph_after_1990:
    df_Zon_plot2 = plt.figure(figsize=(10, 7))
    sns.lineplot(x="Year", y="Glob", data=df_Zon[df_Zon["Year"] >= 1990], label="Global")
    sns.lineplot(x="Year", y="NHem", data=df_Zon[df_Zon["Year"] >= 1990], label="Northern Hemisphere")
    sns.lineplot(x="Year", y="SHem", data=df_Zon[df_Zon["Year"] >= 1990], label="Southern Hemisphere")
    plt.xlabel("Year")
    plt.ylabel("Temperature (ºC change)")
    plt.title("Temperature anomalies")
    plt.legend();

    st.pyplot(df_Zon_plot2)
