# streamlit_app.py
import streamlit as st
from pages.home import home_page  # Importing the home page function

def main():
    st.set_page_config(
        page_title="ClimateTemp Dashboard",
        page_icon=":partly_sunny:",
        layout="wide"
    )

    st.title("ClimateTemp Dashboard")

    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": home_page,
        # Add more pages here as your app grows
    }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()
