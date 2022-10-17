from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status # 201, 404 등등

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

# 목록 조회생성
@api_view(['GET', 'POST']) # DRF에서는 필수로 해줘야함, 기본은 GET(GET 아니면 405 응답)
def articles_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all() 
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data) # serializer된 데이터!(재구성할 수 있는 데이터)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data) # 출력되는 필드만 다름
        if serializer.is_valid(raise_exception=True): # raise_exception 쓰면 아래줄 안써도 됨, 유효하지 않은 데이터에 대해 예외 발생시키기, 기본적으로 400 응답
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201(잘 생성되었다.) 리턴 
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 400 리턴

# 단일 조회수정삭제
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk) # 페이지 못 찾으면 404를 줘야하기에.. get_object_or_404() # all()은 get_list_or_404()로 바꿔줌
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data) # serializer된 데이터!(재구성할 수 있는 데이터)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204 응답
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data) # 인스턴스가 앞쪽으로 들어감 (모델과 다름??)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data) # 200이라서 별도 뭐 없음

    
@api_view(['GET']) # DRF에서는 필수로 해줘야함, GET 아니면 405 응답
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data) # serializer된 데이터!(재구성할 수 있는 데이터)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204 응답
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data) # 인스턴스가 앞쪽으로 들어감 (모델과 다름??)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()
            return Response(serializer.data) # 200이라서 별도 뭐 없음

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data) # request.POST 아님
    if serializer.is_valid(raise_exception=True): # 읽기 전용 필드로 바꿔서 여기서 article 검사 하지 않게 해줘
        serializer.save(article=article) # commit=False가 아니라 save의 인자로 들어감
        return Response(serializer.data, status=status.HTTP_201_CREATED)
