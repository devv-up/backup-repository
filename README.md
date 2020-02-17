# devv-up-backend

## 목적
devv-up 어플리케이션에 필요한 HTTP API 작성, DB관리, 배포

## 사용법
- 설정은 서버를 구동하는 명령어의 뒤에 인자로 넣어준다.
	- ex) python manage.py runserver --settings=mysettings.local
	- ex) python manage.py runserver --settings=mysettings.product
- 배포시 설정파일에는 프로젝트의 Root 경로에 secrets.json 파일 필요. 아래와 같은 설정을 해줘야함
	- "SECRET_KEY":"임의의 긴 비밀번호"
	- 추후 추가 예정

## 기술 스택
- Docker + Docker Compose
- Jenkins
- AWS
- Python
- Django + Django Rest Framework
- Nginx
- MySQL
