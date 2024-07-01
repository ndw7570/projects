# 베이스 이미지로 python을 사용합니다.
FROM python:3.9

# 작업 디렉터리를 생성하고 설정합니다.
WORKDIR /app

# requirements.txt 파일을 이미지로 복사합니다.
COPY src/requirements.txt .

# 필요 패키지들을 설치합니다.
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# 현재 디렉터리의 모든 파일을 이미지의 /app 디렉터리에 복사합니다.
COPY src/ .

EXPOSE 8501

# 스트림릿 애플리케이션을 실행합니다.
# CMD ["streamlit", "run", "app.py"]
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]
#, "--server.address=0.0.0.0"]