import streamlit as st


st.title("Page4")

st.header("Example of object notation")

form = st.form("my_form_2")
selected_val = form.slider("Select a value")
form.form_submit_button("Submit")

st.write("Selected value: ", selected_val)
