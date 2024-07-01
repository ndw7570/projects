# import streamlit as st

# st.title('Hello, Streamlit!')
# st.write('This is a simple Streamlit app running in a Docker container.')


import streamlit as st
import pandas as pd
from app import load_page
import streamlit as st

# 페이지 로드 함수
def load_page(page_name):
    st.session_state.current_page = page_name

def show():
    st.title("shipping")
    st.write("여기는 선적 페이지입니다.")

# 제목과 설명
st.title("기본 웹페이지 구현 예제")
st.write("이 애플리케이션은 사용자 입력을 받고, 데이터를 데이터프레임 형태로 표시합니다.")

# 텍스트 입력 받기
user_input = st.text_input("텍스트를 입력하세요:")

# 입력된 내용을 출력
if user_input:
    st.write(f"입력된 내용: {user_input}")

# 데이터프레임 생성
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)

import streamlit as st

# if 'page' not in st.session_state:
#     st.session_state.page = 'home'

st.sidebar.button("홈", on_click=load_page, args=('home',))
st.sidebar.button("선적", on_click=load_page, args=('shipping',))
st.sidebar.button("문의", on_click=load_page, args=('contact',))


# 사이드바 메뉴
menu = ["홈", "페이지 1", "페이지 2"]
choice2 = st.selectbox("메뉴", menu)
choice = st.sidebar.selectbox("메뉴", menu)

# 페이지 별 내용 설정
if choice == "홈":
    st.title("홈 페이지")
    st.write("여기는 홈 페이지입니다.")
elif choice == "페이지 1":
    st.title("페이지 1")
    st.write("여기는 페이지 1입니다.")
elif choice == "페이지 2":
    st.title("페이지 2")
    st.write("여기는 페이지 2입니다.")

st.sidebar.button("선적")
st.sidebar.button("통계")
st.sidebar.button("국세청")


# 데이터프레임 표시
st.write("데이터프레임 예시:")
st.dataframe(df)

# 파일 업로드
# uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
uploaded_file = st.file_uploader("EXCEL 파일 업로드", type=["xlsx"])

if uploaded_file:
    # 업로드된 CSV 파일을 데이터프레임으로 읽기
    # uploaded_df = pd.read_csv(uploaded_file)
    uploaded_df = pd.read_excel(uploaded_file)
    st.write("업로드된 데이터프레임:")
    st.dataframe(uploaded_df)

    # 데이터프레임을 CSV 파일로 저장
    uploaded_df.to_csv("uploaded_file.csv", index=False)
    st.write("업로드된 데이터를 'uploaded_file.csv' 파일로 저장했습니다.")
