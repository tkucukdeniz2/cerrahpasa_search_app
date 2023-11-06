import streamlit as st
import pandas as pd

def search_affiliations(df, search_term):
    # Filter rows where 'Affiliations' column contains the search term
    result = df[df['Affiliations'].str.contains(search_term, case=False, na=False)]
    # Select only the specified columns
    result = result[['Authors', 'Affiliations', 'Title', 'Link']]
    return result

def find_unique_titles(df1, df2):
    # Find titles in df1 that are not in df2
    unique_titles = df1[~df1['Title'].isin(df2['Title'])]
    return unique_titles

# Display the logo at the top of the app
st.image("FileHandler.jpg")
st.title('Search Scopus Export Data for Affiliations')

# Upload the first CSV file
uploaded_file = st.file_uploader("Choose the first CSV file", type="csv", key="file1")

# Upload the second CSV file
uploaded_file_2 = st.file_uploader("Choose the second CSV file", type="csv", key="file2")

if uploaded_file is not None and uploaded_file_2 is not None:
    # Read the first CSV file
    data_1 = pd.read_csv(uploaded_file)
    
    # Read the second CSV file
    data_2 = pd.read_csv(uploaded_file_2)
    
    # Check if 'Affiliations' column exists in the first CSV
    if 'Affiliations' in data_1.columns:
        # Search for the string 'cerrah' in the 'Affiliations' column of the first CSV
        results = search_affiliations(data_1, 'cerrah')
        
        # If there are results, check if any title is not in the second CSV
        if not results.empty:
            unique_titles = find_unique_titles(results, data_2)
            
            # Display the results
            if not unique_titles.empty:
                for _, row in unique_titles.iterrows():
                    st.write(f"**Authors:** {row['Authors']}")
                    st.write(f"**Affiliations:** {row['Affiliations']}")
                    st.write(f"**Title:** {row['Title']}")
                    # Create a hyperlink that opens in a new tab
                    st.markdown(f"**Link:** <a href='{row['Link']}' target='_blank'>{row['Link']}</a>", unsafe_allow_html=True)
                    st.write("---")  # Add a separator line
            else:
                st.write("All entries with 'cerrah' in the 'Affiliations' column of the first CSV are also present in the second CSV.")
        else:
            st.write("No entries found with 'cerrah' in the 'Affiliations' column of the first CSV.")
    else:
        st.write("'Affiliations' column not found in the first CSV.")
