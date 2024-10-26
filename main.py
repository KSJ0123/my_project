#start: streamlit run main.py
import streamlit as st

st.write('hello world!!')
st.header(':violet[제목]')
st.subheader('부제목')
st.write('매천고')
st.code("print('hello world!!')",language='python')
st.divider()
st.markdown(':red[**공동**]교육과정')

button = st.button('버튼')
if button:
    st.write('버튼클릭!')

a = st.number_input('1번 숫자를 입력하세요',step=1)
b = st.number_input('2번 숫자를 입력하세요',step=1)
btn = st.button('더하기')
if btn:
    st.write(a+b)