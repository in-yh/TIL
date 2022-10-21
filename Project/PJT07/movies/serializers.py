from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


# Movie에서 제목만 출력 
class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


# 특정 Actor가 출연한 Movie 목록 조회하기 (역참조)
class ActorSerializer(serializers.ModelSerializer):

    movies = MovieTitleSerializer(many=True, read_only=True) # 제목만 출력되게 함

    class Meta:
        model = Actor
        fields = '__all__'


# Actor에서 name만 출력하게 함 / 이렇게 하나하나 만드는게 맞나?
class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


# 특정 Movie의 정보 제공
class MovieSerializer(serializers.ModelSerializer):

    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True) # 역참조

    class Meta:
        model = Movie
        fields = '__all__'
        # 위의 actors를 정의해주기 전에는 여기서 '__all__'을 해주면 actors의 번호가 들어감
        # 그래서 exclude = ('actors',)를 해서 제거를 해주고 위에 actors를 정의해줬는데 에러발생
        # '__all__'을 해주고 위에 actors 정의해주면 번호였던 것이 알아서 내용이 들어감


class ReviewSerializer(serializers.ModelSerializer):

    movie = MovieTitleSerializer(read_only=True) # 참조, 1개를 가져오기에 many=True는 하지 않는다.

    class Meta:
        model = Review
        fields = '__all__'