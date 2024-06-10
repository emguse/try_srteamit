import pandas as pd
import streamlit as st


st.title("Page 1")

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

# latex
st.header("st.latex")
st.latex(
    r"""
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     """
)

# secrets
st.header("st.secrets")
st.text(
    """
    .streamlit/secrets.toml

    OpenAI_key = "your OpenAI key"
    whitelist = ["sally", "bob", "joe"]

    [database]
    user = "!!!USERNAME!!!"
    password = "!!!PASSWORD!!!"
    """
)
st.write(st.secrets["whitelist"])
st.write(st.secrets["database"]["user"])
st.write(st.secrets.database.password)


# file_uploader(Max:200MB)
st.header("st.file_uploader")

st.subheader("Input CSV")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("DataFrame")
    st.write(df)
    st.subheader("Descriptive Statistics")
    st.write(df.describe())
else:
    st.info("☝️ Upload a CSV file")
