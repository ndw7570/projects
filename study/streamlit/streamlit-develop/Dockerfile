# 베이스 이미지로 python을 사용합니다.
FROM python:3.9

# 작업 디렉터리를 생성하고 설정합니다.
WORKDIR /app

# 로컬의 모든 파일을 도커 이미지로 복사합니다.
COPY . .

# 필요 패키지들을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit 애플리케이션이 사용하는 포트를 노출합니다.
EXPOSE 8501

# Streamlit 애플리케이션을 실행합니다.
CMD ["streamlit", "hello"]
