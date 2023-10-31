
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

import os
print(os.listdir())
#Check which datasets we have uploaded in our colab session

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
sns.set()


df_Zon = pd.read_csv("ZonAnn.Ts+dSST.csv")
df_Zon.head()


plt.figure(figsize = (10,7))
sns.lineplot(x = "Year", y = "Glob", data = df_Zon, label = "Global")
sns.lineplot(x = "Year", y = "NHem", data = df_Zon, label = "Northern Hemisphere")
sns.lineplot(x = "Year", y = "SHem", data = df_Zon, label = "Southern Hemisphere")
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies")
plt.legend();

plt.figure(figsize = (10,7))
sns.lineplot(x = "Year", y = "Glob", data = df_Zon[df_Zon["Year"]>=1990], label = "Global")
sns.lineplot(x = "Year", y = "NHem", data = df_Zon[df_Zon["Year"]>=1990], label = "Northern Hemisphere")
sns.lineplot(x = "Year", y = "SHem", data = df_Zon[df_Zon["Year"]>=1990], label = "Southern Hemisphere")
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies")
plt.legend();

df_co2 = pd.read_csv("owid-co2-data.csv")
df_co2.head()

df_co2["country"].unique()

df_co2_n = df_co2[df_co2["country"].isin(["North America", "Asia", "Europe", "World"])]

df_co2_n.head()

plt.figure(figsize = (10,7))
sns.relplot(x = "year", y = "share_of_temperature_change_from_ghg", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("Contribution (%)")
plt.title("Share of contribution to global warming");

plt.figure(figsize = (10,7))
sns.relplot(x = "year", y = "temperature_change_from_co2", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("Temperature change (ºC)")
plt.title("Contribution to temperature increase due to CO2");

plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes)")
plt.title("Annual total emissions of CO2");

plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2_per_capita", kind = "line", hue = "country", data = df_co2_n)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes per person)")
plt.title("Annual emissions of CO2 per capita");

df_co2_n["gdp"] = df_co2_n['co2']/df_co2_n["co2_per_gdp"]

# Here I obtained the GDP values from the other 2 variables as "gdp" column is empty for whole continents (but "co2" and "co2_per_gdp" not)

g = sns.FacetGrid(df_co2_n, col = "country", hue = "country", height = 4)
g.map(sns.scatterplot, "gdp", "temperature_change_from_co2")
g.set_axis_labels("GDP", "Temperature change (ºC)")
g.set_titles(col_template="Temperature change vs GDP")

g.add_legend();

# Since GDP and population seem to positively correlate with Co2 emissions and temperature increase, let's focus on some big and/or rich countries.
df_co2_country = df_co2[df_co2["country"].isin(["United States", "Canada", "Germany", "France", "Russia", "China", "India", "Brazil", "Australia"])]

# We will also have a separate dataset with "World" co2 data.

df_co2_world = df_co2.loc[df_co2["country"] == "World"]

# From the NASA dataset, we will work with Year, Glob, NHem and SHem variables:

df_temp = df_Zon[["Year", "Glob", "SHem", "NHem"]]

# With the first dataset (df_co2_country) we can compare trends between these countries and identify some correlations.
# For the modeling part, we can focus on global data (merging df_co2_world and df_temp datasets) to predict temperature changes in the next years.




# As seen in the previous graphs, we have more complete co2 data since about 1850.
# And in our NASA dataset we have data since 1880. Also, the nasa dataset is very complete (no missing values)
# so we decided to focus on the data since 1880.
# Choosing "Glob" as our target value, it is also important to not have any NaNs there.
# However, our NASA dataset is based on the 1951-1980 period. Since we want to compare these temperature changes with
# the target of "1.5ºC maximum increase from the pre-industrial average", we have to change the baseline to the pre-industrial period.
# Let's say that the pre-industrial period in our case is 1880-1900, we calculate the average anomalies in that period and
# subtract it from the other values, to obtain new temperature anomalies now in reference to the "pre-industrial period".

filtered = df_temp[(df_temp['Year'] >= 1880) & (df_temp['Year'] <= 1900)]

# Calculate the average temperature anomalies for the specified period
average = filtered['Glob'].mean()

print(f'Average temperature anomalies between 1880 and 1900: {average:.2f}')



df_temp["Glob_adj"] = df_temp["Glob"] - (-0.22)

df_temp.head()

plt.figure(figsize = (10,7))
sns.lineplot(x = "Year", y = "Glob_adj", data = df_temp)
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies (pre-industrial levels)");

# We can do the same with Northern and Sothern Hemispheres out of curiosity...
average_n = filtered['NHem'].mean()
print(f'NHem-Average temperature anomalies between 1880 and 1900: {average_n:.2f}')
average_s = filtered['SHem'].mean()
print(f'SHem-Average temperature anomalies between 1880 and 1900: {average_s:.2f}')

df_temp["NHem_adj"] = df_temp["NHem"] - (-0.30)
df_temp["SHem_adj"] = df_temp["SHem"] - (-0.14)

df_temp.head()

plt.figure(figsize = (10,7))
sns.lineplot(x = "Year", y = "Glob_adj", data = df_temp, label = "Global")
sns.lineplot(x = "Year", y = "NHem_adj", data = df_temp, label = "Northern Hemisphere")
sns.lineplot(x = "Year", y = "SHem_adj", data = df_temp, label = "Southern Hemisphere")
plt.xlabel("Year")
plt.ylabel("Temperature (ºC change)")
plt.title("Temperature anomalies (pre-industrial levels)")
plt.legend();

# We can see that the Northern Hemisphere has surpased the 1.5ºC "limit" a couple of times. It's also interesting to see a seasonality in the data...

# Some graphs for the country dataset:

plt.figure(figsize = (10,7))
sns.relplot(x = "year", y = "temperature_change_from_co2", kind = "line", hue = "country", data = df_co2_country)
plt.xlabel("Year")
plt.ylabel("Temperature change (ºC)")
plt.title("Contribution to temperature increase due to CO2");

# United States is a big contributor to temperature increase due to CO2 emissions!



plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2", kind = "line", hue = "country", data = df_co2_country)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes)")
plt.title("Annual total emissions of CO2");

plt.figure(figsize = (12,8))
sns.relplot(x = "year", y = "co2_per_capita", kind = "line", hue = "country", data = df_co2_country)
plt.xlabel("Year")
plt.ylabel("CO2 (million tonnes per person)")
plt.title("Annual emissions of CO2 per capita");

# In the last few decades, China has been leading in total Co2 emissions, although on a per capita basis,
# the United States was the leader throughout the last century.

plt.figure(figsize = (10,7))
sns.relplot(x = "gdp", y = "temperature_change_from_co2", hue = "country", data = df_co2_country)
plt.xlabel("GDP")
plt.ylabel("Temperature change (ºC)")
plt.title("Temperature change due to CO2");

# Picking only variables of interest (let me know if you want to add another):

co2_country = df_co2_country[["country", "year", "population", "gdp", "co2", "co2_per_capita", "co2_per_gdp", "temperature_change_from_co2"]]

co2_country.info()


# Handling missing values (I chose median because it's more robust to extreme values):

cols = ['population', 'gdp', 'co2', 'co2_per_capita', 'co2_per_gdp', 'temperature_change_from_co2']

for i in cols:
    co2_country[i] = co2_country[i].fillna(co2_country[i].median())

# Some statistical tests:
# H0: variables are not correlated
# H1: variables are correlated
# alpha = 0.05

from scipy.stats import pearsonr

pearsonr(x = co2_country.population, y = co2_country.temperature_change_from_co2)

# Population and temperature change due to CO2 are statistically correlated.

pearsonr(x = co2_country.gdp, y = co2_country.temperature_change_from_co2)

# GDP and temperature change due to CO2 are statistically correlated.


# Merging NASA dataset with world co2 data ("inner" join to only have data from 1880 and avoid getting more NaNs)
df_temp = df_temp.rename({"Year" : "year"}, axis=1)

merged_global = df_temp.merge(right = df_co2_world, on = "year", how = "inner")

merged_global.head()

# Picking only variables of interest (let me know if you want to add another):

merged_global = merged_global[["year", "Glob_adj", "NHem_adj", "SHem_adj", "country", "population", "gdp", "co2", "co2_per_capita", "co2_per_gdp", "temperature_change_from_co2"]]

merged_global.info()

# I would suggest to remove gdp and co2_per_gdp in this case (too many NaNs)


# Some statistical tests:
# H0: variables are not correlated
# H1: variables are correlated
# alpha = 0.05

from scipy.stats import pearsonr

pearsonr(x = merged_global.population, y = merged_global.Glob_adj)

# Population and Global temperature change are statistically correlated.

pearsonr(x = merged_global.co2, y = merged_global.Glob_adj)

# CO2 emissions and Global temperature change are statistically correlated.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CO2 emissions data (owid-co2-data.csv)
co2_data = pd.read_csv('owid-co2-data.csv')

# Load the temperature data (GLB.Ts+dSST.csv)
temperature_data = pd.read_csv('GLB.Ts+dSST.csv', skiprows=1)  # Skip the first row

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

# Data Visualization
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=co2_data, x='co2', kde=True)
plt.title("CO2 Emissions Distribution")

plt.subplot(1, 2, 2)
sns.histplot(data=temperature_data, x='J-D', kde=True)
plt.title("Temperature Anomalies Distribution")

plt.show()

# Print Data Distribution Summary
print("Summary Statistics for CO2 Emissions:")
print(co2_description)
print(f"Mean: {co2_mean:.2f}, Median: {co2_median:.2f}, Mode: {co2_mode:.2f}")
print(f"Standard Deviation: {co2_std:.2f}, Range: {co2_range:.2f}, IQR: {co2_iqr:.2f}")

print("\nSummary Statistics for Temperature Anomalies:")
print(temperature_description)
print(f"Mean: {temperature_mean:.2f}, Median: {temperature_median:.2f}, Mode: {temperature_mode:.2f}")
print(f"Standard Deviation: {temperature_std:.2f}, Range: {temperature_range:.2f}, IQR: {temperature_iqr:.2f}")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CO2 emissions data (owid-co2-data.csv)
co2_data = pd.read_csv('owid-co2-data.csv')

# Load the temperature data (ZonAnn.Ts+dSST.csv)
temperature_data = pd.read_csv('ZonAnn.Ts+dSST.csv')

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
temperature_mean = temperature_data['Glob'].mean()
temperature_median = temperature_data['Glob'].median()
temperature_mode = temperature_data['Glob'].mode().values[0]
temperature_std = temperature_data['Glob'].std()
temperature_range = temperature_data['Glob'].max() - temperature_data['Glob'].min()
temperature_iqr = temperature_data['Glob'].quantile(0.75) - temperature_data['Glob'].quantile(0.25)

# Data Visualization
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=co2_data, x='co2', kde=True)
plt.title("CO2 Emissions Distribution")

plt.subplot(1, 2, 2)
sns.histplot(data=temperature_data, x='Glob', kde=True)
plt.title("Temperature Anomalies Distribution")

plt.show()

# Print Data Distribution Summary
print("Summary Statistics for CO2 Emissions:")
print(co2_description)
print(f"Mean: {co2_mean:.2f}, Median: {co2_median:.2f}, Mode: {co2_mode:.2f}")
print(f"Standard Deviation: {co2_std:.2f}, Range: {co2_range:.2f}, IQR: {co2_iqr:.2f}")

print("\nSummary Statistics for Temperature Anomalies:")
print(temperature_description)
print(f"Mean: {temperature_mean:.2f}, Median: {temperature_median:.2f}, Mode: {temperature_mode:.2f}")
print(f"Standard Deviation: {temperature_std:.2f}, Range: {temperature_range:.2f}, IQR: {temperature_iqr:.2f}")

cols = ["population", "gdp", "co2", "co2_per_capita", "co2_per_gdp"]

for i in cols:
  sns.displot(co2_data[i], kde = True)

co2_data.boxplot(cols)
plt.show();

# We already knew that the "raw data" has a broad range of values for gdp and population.

# Analysis of the "merged_global" data (i.e. global temperatures already merged with "World" co2 data)
# I didn't include here "gdp" or "co2_per_gdp" because info showed too many NaNs.

cols2 = ["Glob_adj", "NHem_adj", "SHem_adj", "population", "co2", "co2_per_capita", "temperature_change_from_co2"]
for i in cols2:
  sns.displot(merged_global[i], kde = True)

for i in cols2:
  sns.boxplot(data = merged_global[i])
  plt.title(f'Boxplot for {i}')
  plt.show()

plt.figure(figsize=(7,7))

sns.heatmap(merged_global[cols2].corr(),annot=True,cmap='viridis');

# A high correlation between many of the variables chosen can be seen.

sns.pairplot(merged_global[cols2], diag_kind = "kde")