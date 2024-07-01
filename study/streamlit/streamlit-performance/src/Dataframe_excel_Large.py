import streamlit as st
import pandas as pd
# import shipping  # 가정: shipping.py가 적절히 구성되어 있음

st.set_page_config(layout="wide")

# 제목과 설명
st.title("기본 웹페이지 구현 예제")
st.write("이 애플리케이션은 사용자 입력을 받고, 데이터를 데이터프레임 형태로 표시합니다.")

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
    st.table(edited_df) # 별로 안좋아..

    save_button = st.button("수정된 데이터 저장")
    if save_button:
        edited_df.to_csv("edited_data.csv", index=False)
        st.write("수정된 데이터를 'edited_data.csv' 파일로 저장했습니다.")

    # 데이터프레임을 CSV 파일로 저장
    uploaded_df.to_csv("uploaded_file.csv", index=False)
    st.success("업로드된 데이터를 'uploaded_file.csv' 파일로 저장했습니다.")
