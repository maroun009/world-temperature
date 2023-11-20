import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections",
    page_icon="🌐",
)

greenhouse_gas = Image.open("app/img/GreenHouseGasesPollution.jpg")
st.image(greenhouse_gas, caption="Greenhouse Gases Pollution", use_column_width=True)

# Additional content goes here


