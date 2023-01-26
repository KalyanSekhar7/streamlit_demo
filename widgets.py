import streamlit as st

st.title("Widgets")

welcome_button = st.button("Welcome")

if welcome_button:
    st.write("Thank you for clicking this")

text_input = st.text_input(label="Input your text")

st.write(text_input)

address = st.text_area("Address")

st.write(address)

date_input = st.date_input("Enter a date")
time_input = st.time_input("Enter the time")

Checkbox1 = st.checkbox("Accept terms and condition", value=True)
if Checkbox1:
    st.write("Thank you , you may proceed")

radio_button = st.radio("Colours", ["red", "Green", "Blue"], index=0)

select_box = st.selectbox("Colours", ["red", "Green", "Blue"], index=0)

multi_select = st.multiselect("Colours", ["red", "Green", "Blue"])

slider = st.slider("Select an Age",min_value=18,max_value=150,step = 5)

numbers = st.number_input("Enter the number",min_value=18.0,max_value=150.0,step = 5.0)


file_uploader = st.file_uploader("Upload an imaqe")

st.image(file_uploader)