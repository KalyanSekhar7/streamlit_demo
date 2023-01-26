import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(100, 3), columns=["first", "second", "third"])

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

figure1, ax = plt.subplots()
ax.scatter(data["first"], data["second"])
ax.legend()
plt.title("Scatter plot")
plt.xlabel("first")
plt.ylabel("Second")
st.pyplot(figure1)

