from pathlib import Path
from datetime import time, datetime

import pandas as pd
import streamlit as st


# read csv
p_sample_wave = Path("data/dst/sample_wave.csv")
df = pd.read_csv(p_sample_wave, index_col=0)


st.header("main.py")

# button
st.subheader("st.button")
if st.button("hello"):
    st.write("Pressed")
else:
    st.write("Ignored")

# Select box
st.header("st.selectbox")
option = st.selectbox("Select", ("foo", "bar"))
st.write(option)

# Multi select
st.header("st.multiselect")
element = st.multiselect(
    "Select Elements", ["sin_wave", "cos_wave"], ["sin_wave", "cos_wave"]
)

# Chart, Dataframe
st.subheader("st.line_chart, Dataframe")
st.line_chart(df, y=element)

df

# Slider
st.subheader("st.slider")
n = st.slider("Choose Number", 0, 100, 42)
st.write("Number: ", n)

# Range slider
st.subheader("Range slider")
values = st.slider("Select a range of values", 0.0, 200.0, (42.0, 137.0))
st.write("Values:", values)

# Range time slider
st.subheader("Range time slider")
selected_time_range = st.slider(
    "Select time range: ", value=(time(8, 30), time(17, 00))
)
st.write("You're selected: ", selected_time_range)

# Datetime slider
st.subheader("Datetime slider")
start_time = st.slider(
    "Select datetime:",
    value=datetime(2024, 4, 1, 9, 00),
    format="YYYY/MM/DD - hh:mm",
)
st.write("You're selected: ", start_time)

# Map
st.map()

# check box
st.header("st.checkbox")
st.write("choose")
ice = st.checkbox("Ice cream")
cof = st.checkbox("Coffee")
sof = st.checkbox("juice")
if ice:
    st.write("🍨")
if cof:
    st.write("☕️")
if sof:
    st.write("🧃")

st.header("st.latex")
st.latex(
    r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     """
)
