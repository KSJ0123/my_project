import streamlit as st

st.sidebar.header("메뉴")
menu= st.sidebar.selectbox('Menu',["자기소개",'학교소개','로그인'])

def 자기소개():
    st.header('자기소개 페이지')
def 학교소개():
    st.header('학교소개 페이지')
def 로그인():
    st.header('로그인')
    c1 , c2 = st.columns(2)
    id=c1.text_input('아이디',placeholder='아이디를 입력하세요')
    pw=c1.text_input('비번',placeholder='비밀번호를 입력하세요',type='password')
    btn=st.button('로그인')
    if btn:
        if id=='abc' and pw =='123':
            st.write('환영합니다')
        else:
            st.write('로그인 실패')

if menu=='자기소개':
    자기소개()
elif menu=='학교소개':
    학교소개()
elif menu=='로그인':
    로그인()