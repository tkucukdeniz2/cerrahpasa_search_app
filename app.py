import streamlit as st
import pandas as pd

# Custom CSS to inject corporate-style into the app.
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Function to search affiliations for a given term.
def search_affiliations(df, search_term):
    result = df[df['Affiliations'].str.contains(search_term, case=False, na=False)]
    result = result[['Authors', 'Affiliations', 'Title', 'Link']]
    return result

# Function to find unique titles between two dataframes.
def find_unique_titles(df1, df2):
    unique_titles = df1[~df1['Title'].isin(df2['Title'])]
    return unique_titles

# Load custom CSS
local_css("style.css")

# Display the logo and title in a more corporate style.
col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed for your layout

with col1:
    st.image("FileHandler.jpg", width=200)

with col2:
    st.markdown("""
    <h1 style='text-align: left; color: black;'>
        Istanbul University-Cerrahpaşa<br>Office of Corporate Data Management
    </h1>
    """, unsafe_allow_html=True)


# Instructions
st.markdown("""
    <div style="background-color:#f1f1f1; padding:10px; border-radius:5px; margin:10px 0;">
    <h2>Instructions</h2>
    <p>Upload the CSV files to compare the records based on the affiliations containing the term "cerrah". The first file is the primary dataset, and the second file is the reference to find unique records.</p>
    </div>
""", unsafe_allow_html=True)

# File upload section
with st.container():
    uploaded_file = st.file_uploader("Choose the first CSV file", type="csv", key="file1")
    uploaded_file_2 = st.file_uploader("Choose the second CSV file", type="csv", key="file2")

# Process files
if uploaded_file and uploaded_file_2:
    data_1 = pd.read_csv(uploaded_file)
    data_2 = pd.read_csv(uploaded_file_2)

    if 'Affiliations' in data_1.columns:
        results = search_affiliations(data_1, 'cerrah')
        if not results.empty:
            unique_titles = find_unique_titles(results, data_2)
            if not unique_titles.empty:
                for _, row in unique_titles.iterrows():
                    st.subheader(row['Title'])
                    st.write(f"**Authors:** {row['Authors']}")
                    st.write(f"**Affiliations:** {row['Affiliations']}")
                    st.markdown(f"[**Link to Document**]({row['Link']})", unsafe_allow_html=True)
                    st.markdown("---")
            else:
                st.info("All entries with 'cerrah' in the 'Affiliations' column of the first CSV are also present in the second CSV.")
        else:
            st.warning("No entries found with 'cerrah' in the 'Affiliations' column of the first CSV.")
    else:
        st.error("'Affiliations' column not found in the first CSV.")
