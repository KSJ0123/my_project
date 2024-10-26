import streamlit as st

a= st.number_input('1번 숫자를 입력하세요',step=1)
b= st.number_input('2번 숫자를 입력하세요',step=1)
btn_p= st.button('더하기')
if btn_p:
    st.write(a+b)
btn_m= st.button('빼기')
if btn_m:
    st.write(a-b)
btn_d= st.button('÷')
if btn_d:
    st.write(a/b)
btn_x=st.button('X')
if btn_x:
    st.write(a*b)