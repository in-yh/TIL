from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment) # 관리자 사이트에서 댓글 확인 가능
# admin site에 등록(register)한다.

# python manage.py createsuperuser