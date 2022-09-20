import streamlit as st
import numpy as np
import pandas as pd


st.title("Nearest Pubs🥂 in UK")

df = pd.read_csv("Data/pub.csv")

location = df[["latitude", "longitude"]]

latitude = st.number_input("Enter Latitude:")
st.write("The entered latitude is: ", latitude)
longitude = st.number_input("Enter Longitude:")
st.write("The entered Longitude is: ", longitude)


button = st.button("Show Nearest Pubs")

location1 = np.array([latitude, longitude])

dist = np.sqrt(np.sum((location1 - location)**2, axis = 1))
k = 5
sort_dist = dist.argsort()[:k]


if button == True:
    st.markdown("Nearest Pubs🥂 Are")
    st.map(df.iloc[sort_dist])
    st.dataframe(df.iloc[sort_dist])

page_bg_img = '''
<style>
.stApp {
background-image: url("https://cdn.pixabay.com/photo/2014/07/12/12/57/fremont-391190_1280.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
