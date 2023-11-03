import streamlit as st

st.set_page_config(
    page_title="Global Environmental Data",
    page_icon="🌐",
)

st.header("Global Environmental Data")

st.sidebar.success("Select a data model above")

st.markdown(
    """
    Data pulled from the following source: https://data.giss.nasa.gov/gistemp/
    """
)
