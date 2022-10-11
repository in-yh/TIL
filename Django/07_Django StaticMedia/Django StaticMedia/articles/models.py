from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail # 이건 다른 라이브러리에서 가져옴, 문서 찾아보면서 작업해야함
from imagekit.models import ProcessedImageField, ImageSpecField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'
# instance는 이미지 파일, FileField가 정의된 모델의 인스턴스 (pk값은 None, save가 되기 전이라서 사용하기 어려움)


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    # Create 1. models.py 2. create.html 3. view.py
    # image = models.ImageField(blank=True) # MEDIA_ROOT 폴더에 '경로'가 저장
    # 이미지는 반드시 있어야 하는게 아니니깐 빈값도 허용이 되어야 함(NULL이 아니라 빈 문자열 허용)
    # blank
    #   기본값 : False
    #   True인 경우 필드를 비워 둘 수 있음
    #   유효성 검사에서 사용 됨
    # null
    #   기본값 : False
    #   True인 경우 빈 값을 NULL로 저장
    # 문자열필드(CharField, TextField와 같은)는 빈값을 ''로 해야하고, 문자열아닌필드는 빈값을 NULL로 해야함
    # ImageField를 사용하려면 Pillow 라이브러리가 필요(pip install Pillow)
    # migrations
    # freeze

    # 'upload_to' argument 
    # 사용자 지정 업로드 경로와 파일 이름 설정하기
    # 1. 문자열로 지정
    # image = models.ImageField(blank=True, upload_to='images/') # MEDIA_ROOT/images 폴더에 저장 (migration 해줘야함)
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/') # 날짜 폴더에 저장
    # 2. 함수 호출 방법
    # image = models.ImageField(blank=True, upload_to=articles_image_path) # 호출쓰지 말고 이 함수의 이름을 씀 / upload_to가 호출될 때 함수 호출
    
    # 썸네일 만들기
    # 1. 원본 이미지 저장 X
    # image = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[Thumbnail(200,300)], # 가로, 세로
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    # 2. 원본 이미지 저장 O
    image = models.ImageField(blank=True)
    image_thumnail = ImageSpecField( # 이 이름으로 필드가 생성되는 건 아님
        source='image',
        processors=[Thumbnail(200,300)], # 가로, 세로
        format='JPEG',
        options={'quality': 80},
    )
    # 출력이 될 때 생성이 된다! (templates에서 사용할 때)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content