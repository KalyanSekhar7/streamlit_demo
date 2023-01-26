import streamlit as st

st.title("Registration form")

first, second = st.columns(2)

first_name = first.text_input("First Name")
last_name = second.text_input("Last Name")

first1, second1 = st.columns([3, 1])  # first will be 3 times that of second one
email = first1.text_input("Email ID")
mob = second1.text_input("Mob number")

user, pw, pw2 = st.columns(3)

username = user.text_input("Username")
password = pw.text_input("Password", type="password")
password2 = pw2.text_input("Retype Password", type="password")

final_1, final_2, final_3 = st.columns(3)
checkbox = final_1.checkbox("I agree")

if checkbox:
    submit = final_3.button("Submit")
