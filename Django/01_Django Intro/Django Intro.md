#### Django Intro



가. 모든 웹 서비스는 클라이언트-서버 구조!

1. 클라이언트 -> 서버 : requests, 요청
2. 클라이언트 <- 서버 : responses, 리턴
3. 장고는 서버를 구현하는 웹 프레임워크

나. 웹 브라우저와 웹 페이지

1. 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는.. 응답을 받는 것을 렌더링이라 표현
2. 정적(static) : url 변경 없이 움직이는 것(navbar 밑으로 내려가는 것처럼) => 자바스크립트로 구현
3. 동적(dynamic) : url 변경되어 움직이는 것 => 초반에는 이 방법으로 구현!

다. 구조(MTV Design Pattern)!! : 규칙이 있다. => 관심사 분리, 직무 분리, 개발의 효율성 위해

1. M : Model(data)

2. T : Template(client)

3. V : View(server)

4. MV(View, client)C(Controller, server) 디자인 패턴을 조금 변형한 패턴

5. Model : 데이터 기록, 저장하는 공간(보내는 것에 끝내는 것이 아니라)

6. Template : client, front-end 반드시 뷰와 같이 일 해야함. 혼자서는 안 됨.

7. View : 클라이언트의 요청을 처리하여 응답을 반환

8. 0번째 : HTTP Request -> URLS(urls.py) -> View(views.py), 접근

   1번째 : Template(<filename>.html) -> View(views.py)

   2번째 : View(views.py) -> Model(models.py)

   3번째 : Model(models.py) -> View(views.py)

   4번째 : View(views.py) -> HTTP Response(HTML)

라. 시작

```bash
ctrl + shift + '~' : 터미널 열기
python -m venv venv : 가상환경 만들기(마지막은 폴더이름! 자유롭게)
source venv/Scripts/activate : 가상환경 실행 및 저장
deactivate : 가상환경 끄기
pip install django==3.2.13 : 장고 설치
pip list : 잘 설치되었는지 확인
pip freeze > requirements.txt : 어떤게 설치되어있다를 requirements.txt 파일에 보여줌, 개발 다 끝나면 requirements에 저장하고 venv 삭제
pip install -r requirements.txt : 가상환경 만들고 실행하고 이 명령어 실행시키면 설치 자동적으로 됨

장고(프로젝트)는 앱들의 모임
django-admin startproject firstpjt .: 프로젝트 폴더 생성(점 찍어줘야 함, 그러나 이름 바꾸면 안 됨 / 점 안 찍으면 폴더 안에 폴더 생김)
python manage.py runserver : 서버 키기, ctrl + https 주소 찍어서 확인

## settings.py 에서 한글로 바꿔주기
# LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Seoul/Asia'

ctrl + c : 끄기 
python manage.py createsuperuser
python manage.py startapp articles : 앱 만들기 / 이름에 하이푼, class, 함수 안 됨. 복수형으로 작성이 약속

ls -al : 경로 확인

## 앱 등록
# settings.py
# INSTALLED_APPS = [
# 	 'articles',
#
# urls.py
# include 추가
# path('articles/', include('articles.urls')),

## url view template 순서 중요!!
```

```python
ctrl + shift + p 누르고 '사용자 설정 열기(JSON)' 누른 후 아래 추가해줘야 
HTML 문서에서 ! + TAB 키 가능

"files.associations": {
        "**/*.html": "html",
            "**/templates/**/*.html": "django-html",
        "**/templates/**/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    "emmet.includeLanguages": {
    "django-html": "html"
    }
```

