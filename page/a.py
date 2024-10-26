import streamlit as st

st.title("A")

btn = st.button("D 페이지로 이동")

if btn:
    st.switch_page("./page/d.py")