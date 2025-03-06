import streamlit as st
import datetime

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)
st.write('선택한 날짜:', d)

st.sidebar.title("Sidebar Title")
sidebar_option = st.sidebar.selectbox('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
st.sidebar.write('You selected:', sidebar_option)
