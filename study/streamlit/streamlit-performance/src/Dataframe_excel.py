import streamlit as st
import pandas as pd
from io import BytesIO

# import shipping  # 가정: shipping.py가 적절히 구성되어 있음

# 페이지 로드 함수
def load_page(page_name):
    st.session_state.current_page = page_name
st.set_page_config(layout="wide")
# 초기 세션 상태 설정
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# 사이드바 메뉴 설정
st.sidebar.title("Navigation")
st.sidebar.button("홈", on_click=load_page, args=('home',))
st.sidebar.button("선적", on_click=load_page, args=('shipping',))
st.sidebar.button("문의!", on_click=load_page, args=('contact',))

# 페이지 별 내용 렌더링
if st.session_state.current_page == 'home':
    st.title("Home Page")
    st.write("Welcome to the home page!")
elif st.session_state.current_page == 'shipping':
    st.title("shipping")
    st.write("Welcome to the shipping page!")
    # shipping.show()  # shipping.py의 show 함수 실행
elif st.session_state.current_page == 'contact':
    st.title("Contact Page")
    st.write("This is the contact page.")



# 제목과 설명
st.title("기본 웹페이지 구현 예제")
st.write("이 애플리케이션은 사용자 입력을 받고, 데이터를 데이터프레임 형태로 표시합니다.")

# 초기 세션 상태 설정
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# 사용자 입력 받기
user_input = st.text_input("텍스트를 입력하세요:")
if user_input:
    st.write(f"입력된 내용: {user_input}")

# 데이터프레임 생성 및 표시
data = {'Column 1': [1, 2, 3, 4], 'Column 2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)
st.write("데이터프레임 예시:")
st.dataframe(df)

# 파일 업로드
uploaded_file = st.file_uploader("EXCEL 파일 업로드", type=["xlsx"])
if uploaded_file:
    uploaded_df = pd.read_excel(uploaded_file)
    # st.write("업로드된 데이터프레임:")
    # st.dataframe(uploaded_df)
   
    edited_df = st.data_editor(uploaded_df, num_rows="dynamic")
    st.write("수정된 데이터프레임:")
    st.dataframe(edited_df)

    save_button = st.button("수정된 데이터 저장")
    if save_button:
        edited_df.to_excel("edited_data.xlsx", index=False)
        st.write("수정된 데이터를 'edited_data.xlsx' 파일로 저장했습니다.")

    # 데이터프레임을 EXCEL 파일로 저장
    uploaded_df.to_excel("uploaded_file.xlsx", index=False)
    st.success("업로드된 데이터를 'uploaded_file.xlsx' 파일로 저장했습니다.")

    # 데이터프레임을 CSV 파일로 저장
    # uploaded_df.to_csv("uploaded_file.csv", index=False)
    # st.success("업로드된 데이터를 'uploaded_file.csv' 파일로 저장했습니다.")

# Excel 파일로 저장하는 함수
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        # writer.save()
    processed_data = output.getvalue()
    return processed_data

# 다운로드 버튼
if st.button('Download Excel File'):
    val = to_excel(uploaded_df)
    st.download_button(label='Real?',
                       data=val,
                       file_name='data.xlsx',
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
import streamlit as st
import time

# 프로그레스 바 초기화
progress_bar = st.progress(0)
sidebar_progress_bar = st.sidebar.progress(0)

steps = 10
rate = 1 / steps
# 100 단계의 작업을 시뮬레이션
for i in range(steps):
    # 프로그레스 바 업데이트
    # progress_bar.progress(i + 1)
    progress_bar.progress(i*rate + rate)
    sidebar_progress_bar.progress(i*rate + rate)
    time.sleep(0.1)  # 진행 상황을 느리게 보여주기 위해 시간 지연

st.write("작업 완료!")

# # 페이지 로드 함수
# def load_page(page_name):
#     st.session_state.current_page = page_name

# # 사이드바 메뉴 설정
# st.sidebar.title("Navigation")
# st.sidebar.button("홈", on_click=load_page, args=('home',))
# st.sidebar.button("선적", on_click=load_page, args=('shipping',))
# st.sidebar.button("문의", on_click=load_page, args=('contact',))

# # 페이지 별 내용 렌더링
# if st.session_state.current_page == 'home':
#     st.title("Home Page")
#     st.write("Welcome to the home page!")
# elif st.session_state.current_page == 'shipping':
#     st.title("shipping")
#     st.write("Welcome to the shipping page!")
#     # shipping.show()  # shipping.py의 show 함수 실행
# elif st.session_state.current_page == 'contact':
#     st.title("Contact Page")
#     st.write("This is the contact page.")


