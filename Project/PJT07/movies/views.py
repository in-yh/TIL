from rest_framework.response import Response # response에서 가져오는거
from rest_framework.decorators import api_view # api는 무조건 api_view가 있어야 함!!
from rest_framework import status
from .models import Actor, Movie, Review
from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, ActorSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(actor) # 하나면 그냥 객체만 넣어줌
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data) # 인스턴스가 앞쪽으로 들어감
        if serializer.is_valid(raise_exception=True): # 유효성 검증 통과하지 못하면 400에러 뜨게 함
            serializer.save()
            return Response(serializer.data) # 200이라서 별도 뭐 없음

    elif request.method == 'DELETE':
        review.delete() # 삭제는 그냥 삭제, serializer 할 것도 없지
        return Response({ 
            "delete" : f'review {review_pk} is deleted'
        }, status = status.HTTP_204_NO_CONTENT)
        # delete 화면 만들어주기


@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data) # 내가 넣은 데이터를 가져오고(그냥 조회만 한다면 조회할 객체를 넣어주면 돼)
    if serializer.is_valid(raise_exception=True): # 그 데이터가 유효하다면
        serializer.save(movie=movie) # 저장하는데, movie 정보는 읽기 전용 필드이므로 여기서 넣어줘
        return Response(serializer.data, status=status.HTTP_201_CREATED)