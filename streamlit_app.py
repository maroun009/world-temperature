# streamlit_app.py
import streamlit as st
from pages import home, contents, introduction, data_manipulation, visualization, \
    classification, model_optimization, results_interpretation, third_section, \
    global_temperature, global_co2_by_region, global_co2_by_country, co2_and_temperature, environmental_data, project_breakdown

# Create a dictionary to map page names to their corresponding functions
pages = {
    "Home": home.home_page,
    "Contents": contents.contents_page,
    "Introduction": introduction.introduction_page,
    "Understanding and Manipulation of Data": data_manipulation.data_manipulation_page,
    "Pre-Processing and Feature Engineering": data_manipulation.feature_engineering_page,
    "Visualizations and Statistics": visualization.visualization_page,
    "Classification of Problem": classification.classification_page,
    "Model Choice and Optimization": model_optimization.model_optimization_page,
    "Interpretation of Results": results_interpretation.results_interpretation_page,
    "Third Section Contents": third_section.third_section_page,
    "Global Annual Temperature Zone": global_temperature.global_temperature_page,
    "Global CO2 Emission by Region": global_co2_by_region.global_co2_by_region_page,
    "Global CO2 Emission by Country": global_co2_by_country.global_co2_by_country_page,
    "CO2 Emissions & Temperature Anomalies": co2_and_temperature.co2_and_temperature_page,
    "World Environmental Data": environmental_data.environmental_data_page,
    "Project Breakdown": project_breakdown.project_breakdown_page,  # Added this line
}

# Streamlit app
def main():
    st.sidebar.title("Navigation")
    page_selection = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page
    pages[page_selection]()

if __name__ == "__main__":
    main()


