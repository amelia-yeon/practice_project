# python:3.7.9의 이미지로 부터 가져옴!
FROM python:3.7.9

#image가 올라갔을 때 수행되는 명령어들
# 필자의 경우, app이라는 폴더를 만들고 -> 해당 디렉토리에 있는 app 항목을 '/app'로 복사
# 해당 디펜던시도 '/app' 아래로 복사
# 작업 디렉토리를 '/app' 으로 지정 -> cd 명령어와 동일함 
RUN mkdir /app 
COPY /app /app
COPY pyproject.toml /app 
COPY poetry.lock /app 
WORKDIR /app


# source 복사한 뒤로
# poetry 설치 및 실행 명령어 적어주기
# pip3를 이용하여 poetry 설치


RUN pip3 install poetry
RUN pip3 install -U python-dotenv
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root
# poetry로 pyproject.toml에 추가되어 있는 패키지를 설치할 때 사용 하는 명령어는 poetry install 이다.
# poetry install 할 때 주의 할 점 -> poetry install --no-root를 붙여야 빌드 오류가 나지 않는다
# 이유 : --no-root를 붙여줘야 의존성만 설치를 해주기 때문에! 


# expose는 Dockefrile의 빌드로 생성된 이미지에서 열어줄 포트를 의미, 호스트 머신과 컨테이너 포트 매핑시 사용됨!
# 컨테이너를 생성 할 때 실행되며 -> 보통 컨테이너 내부에서 항상 돌아가는 서버를 띄울 때 사용한다.
EXPOSE 8001
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8001"]

