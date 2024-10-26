import streamlit as st

#별점 = st.feedback('stars')
#st.write(별점)
st.write('점심메뉴를 선택하세요')
짜장면= st.checkbox('짜장면')
짬뽕 = st.checkbox('짬뽕')
탕수육 = st.checkbox('탕수육')
sum=0

pri=0
if 짜장면:
    st.write('짜장면을 선택하셨습니다')
    pri=+6000
if 짬뽕:
    st.write('짬뽕을 선택하셨습니다')
    pri=+7000
if 탕수육:
    st.write('탕수육을 선택하셨습니다')
    pri=+12000

st.write(pri,'원 입니다')

라디오버튼=st.radio('내가 가장 좋아하는 색상은?',[":red[빨강]",":blue[파랑]",":green['녹색']"])

if 라디오버튼 ==":red[빨강]":
    st.write('빨강을 선택하셨습니다')

#selectbox
menu = st.selectbox("과목을 선택하세요",['확률과 통계','미적분','기하'])
st.write(menu ,'과목을 선택 하셨습니다')
문자열=''
#multselect
list1=[]
menu2=st.multiselect('과목을 선택하세요',['물리학1','생명과학1','화학1','지구과학1'])
#st.write(menu2+'과목을 선택하셨습니다')
for a in menu2:
    #st.write(a+'과목을 선택하셨습니다')
    문자열 += a+' '

st.write(문자열+'과목을 선택하셨습니다')

id = st.text_input('아이디를 입력하세요',placeholder='아이디 입력')
pw = st.text_input('비밀번호를 입력하세요',type='password')
로그인 = st.button('로그인')

if id == 'abc' and pw == '123':
    st.write('환영합니다')
else:
    st.write('다시 입력해주세요')

#이미지
st.image('./img/40%.png')
#동영상
st.video('https://www.youtube.com/watch?v=ViBlMIhglWs&list=RDViBlMIhglWs&start_radio=1')