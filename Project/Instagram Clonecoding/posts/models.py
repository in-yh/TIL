from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Post(models.Model):
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