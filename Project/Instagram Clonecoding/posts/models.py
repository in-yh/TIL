from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Post와 User 연결하고자
    content = models.TextField()
    image = models.ImageField(blank=True)
    image_thumnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':80},
    )
    # 1. 이미지 파일에 대한 필드 추가(마이그레이션)
    # 2. templates 수정
    # 3. views 수정
    # 4. 출력하기(post.image.url)

    # 이미지 리사이징
    # django-imagekit 모듈 설치 및 등록
    #   pip install django-imagekit
    #   pip freeze > requirements.txt
    #   'imagekit',
    # 원본 이미지 저장 방법 사용
    #   ImageSpecField, Thumbnail 이용


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()