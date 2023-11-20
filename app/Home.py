import streamlit as st
from PIL import Image
from PresentationPage import presentation_breakdown_page

st.set_page_config(
    page_title="Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections",
    page_icon="🌐",
)

# Sidebar navigation
page_options = ["Home", "Project Breakdown"]
selected_page = st.sidebar.selectbox("Navigate to", page_options)

# Main content based on selected page
if selected_page == "Home":
    st.markdown("# Climate Insights: A Comprehensive Analysis of Global Temperature Trends and Future Projections")

    # Display the image
    greenhouse_gas = Image.open("app/img/GreenHouseGasesPollution.jpg")
    st.image(greenhouse_gas, use_column_width=True)

    # Additional content goes here

elif selected_page == "Project Breakdown":
    presentation_breakdown_page()
