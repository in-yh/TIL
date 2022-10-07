from django.db import models
from django.conf import settings # 추가!

# Create your models here.
class Article(models.Model):
    # 장고에서 User 모델을 참조하는 방법
    # 1. settings.AUTH_USER_MODEL : 문자열로 리턴, models.py에서만 사용, models.py는 user를 창조하는 곳이기에..
    # 2. get_user_model() : 객체를 줌, models.py 외 모든 곳에서 사용
    # migrations 해주기
    # 기존에 있던 데이터들에게는 비어있으니.. 여기서 넣어줄거니, 밖에서 넣어줄거니? / 어떤 것을 넣어줄거니?(넣어주면 '그 사용자'가 이전 게시물을 모두 작성했다 라는 의미가 됨)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


# ctrl + shift + P -> python interpreter -> 가상환경 설정
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 위치 상관 없음(어차피 DB에 마지막에 추가됨) / ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(article)으로 작성 권장 / 데이터베이스 컬럼에 article_id로 만들어짐
    # related_name='comments' => migrate 다시 해야함 , 이거 사용하면 역참조시 comment_set 대신에 comments로 대체됨
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


# Django Relationship fields 종류
# 1. 1:1 : OneToOneField()
# 2. N:1 : ForeignKey(to, on_delete, **options) : FK를 만들어주는 역할
#   to : 어디를 참조할 것인가, 참조하는 model class
#   on_delete : 외래 키가 참조하는 객체가 사라졌을 때(게시글이 없어졌어), 외래 키를 가진 객체를 어떻게 처리할 지를 정의(댓글 어떻게 처리할지..) => 데이터 무결성(부모에 무조건 있어야 됨) 원칙이 있기 때문에 매우 중요!
#     CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
#     PROTECT : 댓글이 있으면 게시글 삭제 불가
#     SET_NULL : 게시글이 지워지면 댓글을 NULL로 바꿈
#     SET_DEFAULT : 댓글을 어떤 디폴트 값으로 바꿔줌
#     cf) 데이터 무결성 : 데이터 정확성과 일관성을 유지하고 보증하는 것, 데이터베이스나 RDBMS의 중요한 기능, 참조 무결성 중요!
# 3. M:N : ManyToManyField()

# makemigrations, migrate 해주고
# DJANGO - (쿼리셋,쿼리) - ORM - (SQL) - DATABASE 
# python manage.py sqlmigrate articles 0002 : 이 설계도가 이런 SQL로 만들어졌구나 확인

# python manage.py shell_plus : Comment가 자동으로 import 됨 (shell_plus의 장점)
# comment = Comment() # Comment 클래스의 인스턴스 comment 생성
# comment.content = 'first comment' # 인스턴스 변수 저장
# comment.save() # DB에 댓글 저장
# NOT NULL constraint failed: articles_comment.article_id 에러 발생(articles_comment 테이블의 ForeignKeyField, article_id 값이 저장시 누락되었기 때문)

# article = Article.objects.create(title='title', content='content') # 게시글 작성
# article.pk # 1(게시글 확인)
# 외래 키 데이터 입력 / 다음과 같이 article 객체 자체를 넣을 수 있음
# comment.article = article # 객체를 그대로 집어넣으면 알아서 이 객체의 번호값을 추출해서 저장함
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에 넣어줄 수도 있지만 권장하지 않음
# comment.save() 
# comment.pk # 1
# comment.content # 'first comment'
# comment.article # <Article: title>, 해당 참조하는 게시물 객체를 조회할 수 있음
# comment.article_id # 1, comment의 컬럼 값을 가져옴(article_pk는 존재하지 않기에 안됨)
# comment.article.pk # 1, article table에 있는 pk값을 가져옴(1번 댓글이 작성된 게시물의 pk 조회) 
# comment.article.content # 'content' , 1번 댓글이 작성된 게시물의 content 조회

# 두번째 댓글 작성해보기
# comment = Comment(content='second comment', article=article)
# comment.save()
# comment.pk # 2

# 관계 모델 참조
# N에서 1은 참조 가능하나, 1에서 N은? 이것을 역참조라고 함. related manager를 이용하여..(옛날에 objects..)
# 역참조
#   나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
#   즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
#   N:1 관계에서는 1이 N을 참조하는 상황(외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조)
# article.comment_set.method() # _set은 안바뀜
# 컬럼에는 아무런 변화가 없으나 참조는 해야할 거 아녀, 그래서 manager를 이용해 역참조를 함
# article.comment 형식으로는 댓글 객체를 참조할 수 없음(실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음)
# 반면 참조상황에서는 comment.article 형태로 작성 가능

# 1번 게시글 조회하기
# article = Article.objects.get(pk=1)
# dir(article) # 이 객체가 사용할 수 있는 모든 메서드 조회
# article.comment_set.all() # 1번 게시글에 작성된 모든 댓글 조회(역참조), 디테일 페이지에서..
# 1번 게시글에 작성된 모든 댓글 출력하기
# comments = article.comment_set.all()
# for comment in comments:
#   print(comment.content)

