# streamlit_app.py
import streamlit as st
from pages import project_breakdown,

# Create a dictionary to map page names to their corresponding functions
pages = {
    
    "Project Breakdown": project_breakdown.project_breakdown_page,
}

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    page_selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[page_selection]()

if __name__ == "__main__":
    main()

