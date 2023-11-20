# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Temperature': [25, 28, 22]}
df = pd.DataFrame(data)

def main():
    st.title("ClimateTemp App")
    
    # Display sample data
    st.write("Sample Temperature Data:")
    st.dataframe(df)

    # Plot temperature over time
    st.line_chart(df.set_index('Date')['Temperature'])

if __name__ == "__main__":
    main()
