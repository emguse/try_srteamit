import streamlit as st


st.set_page_config(layout="wide")

st.title("Page 2")

with st.expander("about"):
    st.write("this is test")
    st.image("./data/dst/sample_wave.png")

st.sidebar.header("input")
user_name = st.sidebar.text_input("user name ")
user_face = st.sidebar.selectbox("choose ", ["", "🥶", "😶‍🌫️", "😱", "🪦"])

col1, col2, col3 = st.columns(3)
with col1:
    if user_name != "":
        st.write(f"Hello {user_name}!")
    else:
        st.write("<== Please enter")
with col2:
    if user_face != "":
        st.write(f"{user_face} <- 🦈")
with col3:
    st.image("./data/dst/sample_wave.png")
