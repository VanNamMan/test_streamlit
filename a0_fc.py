import pandas as pd
import numpy as np
import time
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "A0 FC Data",
    ("Image,Video","Goal")
)

st.image("a0.jpg","A0 FC 2019")
st.header("Welcome to A0 Football Club")
st.button("Upload...")