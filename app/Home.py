import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections",
    page_icon="🌐",
)

st.markdown("# Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections")

# Specify the correct path to the image
image_path = "app/img/GreenHouseGasesPollution.jpg"
greenhouse_gas = Image.open(image_path)
st.image(greenhouse_gas, use_column_width=True)
# Additional content goes here



