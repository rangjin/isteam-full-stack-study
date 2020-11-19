# isteam-full-stack-study

### 터미널 명령어

- #### 가상환경 생성
python -m venv "가상환경 이름"

- #### 가상환경 실행
"프로젝트 폴더"/"가상환경 이름"/Scripts 폴더로 이동 후 activate

- #### 가상환경 종료
deactivate

- #### Django 설치
pip install django

- #### Django 프로젝트 생성
django-admin startproject "프로젝트 이름" "프로젝트 생성 위치"

- #### 서버 실행
python manage.py runserver

- #### Django 앱 생성
django-admin startapp "앱 이름" "앱 생성 위치"

- #### Model 마이그레이션
  1. Model 변경
  2. python manage.py makemigrations
  3. python manage.py migrate

- #### 슈퍼유저 생성
python manage.py createsuperuser
