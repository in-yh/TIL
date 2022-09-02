from django.contrib import admin
from .models import Article

admin.site.register(Article)

# 장고의 가장 강력한 기능 중 하나! 관리자 페이지!
# 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지
# 레코드 생성 여부 확인에 유용하며 직접 레코드 삽입도 가능

# python manage.py createsuperuser
# username, password 설정 + y
# runserver 후 /admin 추가
# admin.py에 모델 클래스 등록 필요
# admin 페이지에서 데이터 추가해보기