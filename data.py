import streamlit as st
import pandas as pd
import numpy as np
import time
from tqdm import tqdm

# Displaying data

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a)
nd = n.reshape(2, 4)

sample_dict = {
    "name": ["kalyan"],
    "city": ["ahmedabad"]
}

# remember that the dictionary has to be like a table containing arrays

df = pd.read_csv('references/final_dataset.csv',
                 encoding='cp1252')
st.write("# Using Dataframe")
st.dataframe(df.head())

st.dataframe(nd, width=100, height=100)
st.write("# Using table")
st.table(df.head())
st.write("# Displaying dictionary as a table")
st.table(sample_dict)
st.write("# Using json ")
st.json(sample_dict)
st.write("# Using Simple write command")
st.write(df.head())  # it automatically takes note of the type and displays it accordingly

st.write("# Using Cache memory")


@st.cache
def reference_time():
    tqdm(time.sleep(5))
    return time.time()


if st.checkbox("1"):
    st.write(reference_time())

if st.checkbox("2"):
    st.write(reference_time())
