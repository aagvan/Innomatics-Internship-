import streamlit as st
import numpy as np
import pandas as pd


st.title("Pubs🥂 Location In Maps🗺")

df = pd.read_csv("Data/pub.csv")

authority = st.selectbox('Select a Local Authority', list(df['local_authority'].unique()))

button_click = st.button('Search')
if button_click == True:
    auth = df[df['local_authority'] == authority]
    count = len(auth)
    st.write("Number of Pubs: ", count)
    location = auth[['latitude','longitude']]
    st.map(location)

page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.pixabay.com/photo/2014/07/12/12/57/fremont-391190_1280.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)