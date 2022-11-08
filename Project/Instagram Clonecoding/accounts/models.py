from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # User는 settings.AUTH_USER_MODEL로 받기 
    nickname = models.CharField(max_length=40, blank=True) # 값이 없어도 되고
    introduction = models.TextField(blank=True)
    image_file = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField( # 사이즈는 (300,300), quality는 90, format은 jpeg
        source='image_file',
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality':80},
    )
# 데이터베이스, 마이그레이션 파일 삭제 후 다시 마이그레이션 