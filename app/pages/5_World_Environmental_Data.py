import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set()

st.set_page_config(
    page_title="World Environmental Data",
    page_icon="🌐",
)

st.markdown("# World Environmental Data")
st.sidebar.header("World Environmental Data")
st.write(
    """The following displays the count of the world data by category."""
)

df_Zon = pd.read_csv("data/ZonAnn.Ts+dSST.csv")
df_co2 = pd.read_csv("data/owid-co2-data.csv")

# We will also have a separate dataset with "World" co2 data.

df_co2_world = df_co2.loc[df_co2["country"] == "World"]

# From the NASA dataset, we will work with Year, Glob, NHem and SHem variables:

df_temp = df_Zon[["Year", "Glob", "SHem", "NHem"]]

# Merging NASA dataset with world co2 data ("inner" join to only have data from 1880 and avoid getting more NaNs)
df_temp = df_temp.rename({"Year": "year"}, axis=1)

df_temp["Glob_adj"] = df_temp["Glob"] - (-0.22)
df_temp["NHem_adj"] = df_temp["NHem"] - (-0.30)
df_temp["SHem_adj"] = df_temp["SHem"] - (-0.14)

merged_global = df_temp.merge(right=df_co2_world, on="year", how="inner")

st.write(merged_global.head())

# We already knew that the "raw data" has a broad range of values for gdp and population.

# Analysis of the "merged_global" data (i.e. global temperatures already merged with "World" co2 data)
# I didn't include here "gdp" or "co2_per_gdp" because info showed too many NaNs.

cols2 = ["Glob_adj", "NHem_adj", "SHem_adj", "population", "co2", "co2_per_capita", "temperature_change_from_co2"]

category = st.selectbox("Select graph data by category: ", cols2)

plt.figure(figsize=(10, 7))
displayPlot = sns.displot(merged_global[category], kde=True)
plt.xlabel(category)
plt.ylabel("Count")
plt.title("Count of " + category)
plt.legend();

st.pyplot(displayPlot)

boxPlot = plt.figure(figsize=(10, 7))
sns.boxplot(data=merged_global[category])
plt.title(f'Boxplot for {category}')
plt.xlabel(category)
plt.ylabel("Count")
plt.show()

st.pyplot(boxPlot)

plot3 = plt.figure(figsize=(7, 7))

sns.heatmap(merged_global[cols2].corr(), annot=True, cmap='viridis');

# A high correlation between many of the variables chosen can be seen.

sns.pairplot(merged_global[cols2], diag_kind="kde")

st.pyplot(plot3)
