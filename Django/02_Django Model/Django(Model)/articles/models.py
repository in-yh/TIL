from django.db import models # django.db.models 모듈의 Model 클래스를 상속 받음

# 1. 모델 클래스 생성
#   models.Model 상속
class Article(models.Model):  # Model 클래스를 상속받음 # 하나의 테이블을 위해서는 하나의 클래스가 필요
    # 필드(컬럼)를 정의한다(게시판의 제목과 내용)
    # 클래스변수가 하나의 필드가 된다. 
    # 스키마에서 항상 따라왔던 건 어떤 타입이냐. 
    # 타입은 models에 들어있음. 데이터타입을 정의할 수 있는 여러가지 모델 필드들이 존재. 필드들이 클래스로서 존재
    title = models.CharField(max_length=10) # '필드이름 = 필드타입' 이 됨. 데이터베이스의 뼈대, 스키마를 만듦
    content = models.TextField() # CharField()는 길이 제한 있는 문자열(max_length이라는 필수 키워드 인자가 있음, 저장할 때 유효성검사를 함), TextField()는 조금 긴 문자열(max_length 있지만 유효성 검사 안함)
    # models 모듈의 Field 클래스를 통해 테이블의 필드에 저장할 데이터 유형을 정의, ex) CharField, TextField

    # 지금까지 작성한 models.py 내 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의
    # 모델 클래스 == 테이블 스키마
    # id를 우리가 쓰지 않아도 장고가 알아서 만들어줌

    # 이 클래스를 실제 데이터베이스에 어떻게 반영할 건가(지금 모델에만 써져있고 데이터베이스는 비어 있음)
    # 데이터베이스에 테이블을 생성해야함
    # 그 과정이 Migrations
    # python manage.py makemigrations
    # python manage.py migrate

    # 작성시간/수정시간을 추가하여 모델 변경
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # models.py 변경사항이 일어났을 때 새로운 설계도를 만들어야 함.
    # 바로 makemigrations 하면 반영 안 됨.
    # 데이터베이스는 기본적으로 빈값을 추가 할 수 없어, default값을 정해줘(방식 2개)
    # 1. 값이 있다면 지금(터미널 창)에 입력해
    # 2. 이 대화에서 나가서 코드에 default 값을 넣어서 다시 migrate해
    # 1번 누르고 엔터 하면 다음 화면으로 넘어감, 지금 디폴트 값 입력해, 파이썬 문법에 맞게, 그냥 엔터를 치면 timezone.now 메서드를 기본값으로 줄게(DateTimeField에 맞춰서)
    # 엔터 누르면 됨.

    # 설계도가 0002번 만들어짐.
    # 0001과 다른 점은 dependencies! 0002번은 0001번에 의존, 1번설계도에서 변경사항이 생겨 2번설계도가 생긴거니 의존성 있음.
# class Test.. # 이렇게 만들면 3번 설계도는 2번에 의존할까? NO!!

    # 번호를 쌓아나가는 이유는? 깃을 생각해보자. commit을 쌓아나가지. 변경사항을 쌓아나가. 왜 역사를 기록하기 위해. 언제 문제가 생길지 모르니. 그 과거로 돌아가야할 때도 있지.

    # 마지막에 migrate 해야해 꼭!!

    # settings 등록하고 url 연결 전에 migrations , migrate 하기!