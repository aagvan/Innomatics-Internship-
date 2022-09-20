import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("Data/pub.csv")

st.title("🥂WELCOME to the Pub house!🥂")

st.header("Details of the pubs in United Kingdom are mentioned below:-")
total_pubs = "Total number of Pubs in United Kingdoms are: \n" + str(len(df['fsa_id'].unique()))
st.subheader(total_pubs)

total_local_authority = "Total number of Local Authorities in United Kingdoms are: \n" + str(len(df['local_authority'].unique()))
st.subheader(total_local_authority)

postal_codes = "Total number of postal codes in UK are: \n" + str(len(df['postcode'].unique()))
st.subheader(postal_codes)

st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: x-large;
    color:White
}
</style>
""",
    unsafe_allow_html=True,
)
with st.expander(label="Glimpse of dataset:-",expanded=False):
    st.dataframe(df.head(20))
page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.pixabay.com/photo/2014/07/12/12/57/fremont-391190_1280.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
