import streamlit as st
import pandas as pd

def search_affiliations(df):
    # Filter rows where 'Affiliations' column contains the string 'cerrah'
    result = df[df['Affiliations'].str.contains('cerrah', case=False, na=False)]
    
    # Select only the specified columns
    result = result[['Authors', 'Affiliations', 'Title', 'Link']]
    
    return result

st.title('Search Scopus Export Data for Affiliations')

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
            for _, row in results.iterrows():
                st.write(f"**Authors:** {row['Authors']}")
                st.write(f"**Affiliations:** {row['Affiliations']}")
                st.write(f"**Title:** {row['Title']}")
                # Create a hyperlink that opens in a new tab
                st.markdown(f"**Link:** <a href='{row['Link']}' target='_blank'>{row['Link']}</a>", unsafe_allow_html=True)
                st.write("---")  # Add a separator line
        else:
            st.write("No entries found with 'cerrah' in the 'Affiliations' column.")
    else:
        st.write("'Affiliations' column not found in the CSV.")
