from django.db import models
from django.conf import settings


# M:N (Article-User) : 좋아요 기능
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # Article:User(N:1)
    # article.user
    # user.article_set

    # Article:User(M:N)
    # article.like_users
    # user.article_set 여기서 충돌 => like_articles로 바꾸자!
    
    # article.user : 게시글을 작성한 유저 N:1
    # user.article_set : 유저가 작성한 게시글들(역참조) N:1
    # article.like_users : 게시글을 좋아요한 유저 M:N
    # user.like_articles : 유저가 좋아요한 게시글(역참조) M:N
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

    # M:N (User-User) : 팔로우 기능
    # 프로필 먼저 작성

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


# fixtures : 초기 데이터를 가져올 때
# 생성
#   dumpdata : 데이터를 다 뜨는 것임
#       python manage.py dumpdata --indent 4 articles.article > articles.json 인덴트 옵션 넣은 거임
#       python manage.py dumpdata --indent 4 articles.comment > comments.json
#       python manage.py dumpdata --indent 4 accounts.user > users.json     
#       fixtures 폴더 만들어서 넣어줌
# 로드
#   loaddata : 데이터 로드
#       마이그레이션 하고
#       python manage.py loaddata articles.json comments.json users.json
