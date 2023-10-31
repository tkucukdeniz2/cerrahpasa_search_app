import streamlit as st
import pandas as pd

def search_affiliations(df):
    # Filter rows where 'Affiliations' column contains the string 'cerrah'
    result = df[df['Affiliations'].str.contains('cerrah', case=False, na=False)]
    return result

st.title('Search CSV for Affiliations')

# Upload the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)
    
    # Check if 'Affiliations' column exists in the CSV
    if 'Affiliations' in data.columns:
        # Search for the string 'cerrah' in the 'Affiliations' column
        results = search_affiliations(data)
        
        # Display the results
        if not results.empty:
            st.write(results)
        else:
            st.write("No entries found with 'cerrah' in the 'Affiliations' column.")
    else:
        st.write("'Affiliations' column not found in the CSV.")
