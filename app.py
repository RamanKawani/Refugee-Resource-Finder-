import streamlit as st
import pandas as pd
import json

# Load resources data from JSON
def load_resources():
    with open('resources.json', 'r') as f:
        resources = json.load(f)
    return pd.DataFrame(resources)

# Main Streamlit app
def main():
    st.title("Refugee Resource Finder in KRG")
    st.write("Find the available resources for refugees in the Kurdistan Region of Iraq.")

    # Load data
    df = load_resources()

    # Sidebar: Filters for resource type, location, or service
    st.sidebar.header("Filter Resources")
    resource_type = st.sidebar.selectbox("Resource Type", df['type'].unique())
    location = st.sidebar.selectbox("Location", df['location'].unique())

    filtered_df = df[(df['type'] == resource_type) & (df['location'] == location)]

    if filtered_df.empty:
        st.write("No resources found based on the filters applied.")
    else:
        st.write(f"### Available Resources in {location} ({resource_type})")
        st.write(filtered_df[['name', 'contact', 'services']])

    # Option to display all resources
    if st.sidebar.button("Show All Resources"):
        st.write("### All Resources")
        st.write(df[['name', 'type', 'location', 'contact', 'services']])

if __name__ == "__main__":
    main()
