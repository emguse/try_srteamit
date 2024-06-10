import time

import streamlit as st


st.title("Page3")

st.header("st.progress")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

st.balloons()
