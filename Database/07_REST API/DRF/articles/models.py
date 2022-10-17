from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Django REST framework - Single Model
# 사전 준비
#   1. Postman 설치
#   2. 가상환경, 활성화 및 패키지 목록 설치
#   3. 모델 및 migration 진행
#   4. 준비된 fixtures 데이터 load (python manage.py loaddata articles.json)
#   5. DFR 설치, 등록 및 패키지 목록 업데이트 (pip install djangorestframework / 'rest_framework',)
 
# Django REST framework - N:1 Relation
# 사전 준비
#   1. 모델 추가 및 설계도(숫자), 데이터베이스 초기화
#   2. migration 진행
#   3. 준비된 fixtures 데이터 load (python manage.py loaddata articles.json comments.json)
