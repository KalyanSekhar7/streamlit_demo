import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
data = {
    "num": [x for x in range(1, 10)],
    "twice": [x * x for x in range(1, 10)],
    "thrice": [x * x * x for x in range(1, 10)]
}
df = pd.DataFrame(data=data)

st.sidebar.selectbox("Select a number", [1, 2, 3, 4, 5])
df_column = st.sidebar.selectbox("Select a column", df.columns)
navigation_button = st.sidebar.radio("Navigation", ["Home", "About US"])

if navigation_button == "Home":
    figure1, ax = plt.subplots()
    ax.plot(df["num"], df[df_column])

    st.pyplot(figure1)

    multiselect_column = st.sidebar.multiselect("Select columns to display", df.columns)
    figure2, ax = plt.subplots()
    plt.legend()
    ax.plot(df["num"], df[multiselect_column])

    st.pyplot(figure2)
