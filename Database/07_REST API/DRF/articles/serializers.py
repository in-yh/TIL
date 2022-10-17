from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer): # 목록을 serializer 해야하기에 리스트

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',) # serialize 톱니바퀴 역할을 한 거임

# ModelSerializer
# ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
# 1. Model 정보에 맞춰 자동으로 필드 생성
# 2. serializer에 대한 유효성 검사기를 자동으로 생성(is_valid())

# python manage.py shell_plus
# from articles.serializers import ArticleListSerializer
# serializer = ArticleListSerializer()
# article = Article.objects.get(pk=1)
# serializer = ArticleListSerializer(article)
# serializer.data # 데이터를 만듦
# 여기까지 단일

# 이제부터 쿼리셋
# articles = Article.objects.all()
# serializer = ArticleListSerializer(articles)
# serializer.data # 오류, many옵션을 True로 해줘야 함(쿼리셋일때!!)
# serializer = ArticleListSerializer(articles, many=True)
# serializer.data

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer): # detail 작성 위해 단일로 다시 작성
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comment_set이 N이라 쿼리셋을 참조(없어도 빈 리스트)
    comment_set = CommentSerializer(many=True, read_only=True)
    # pk뿐만 아니라 모든 정보를 보여줌
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # article.comment_set.count() / 보여지긴 해야하나 유효성검사는 통과해야하니(원래 필드가 아니라서 밑에 쓰면 작동 안 함)

    class Meta:
        model = Article
        fields = '__all__'

