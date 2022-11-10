<h1>PJT08</h1>

- **TIL**
  - 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web Application 제작 방법 학습
  - AJAX를 통한 비동기적 작동 활용 (Following, Follow 수행 시)
  - N:1 관계를 통해 게시물 작성, 코멘트 작성 등의 구현
  - M:N 관계를 통해 '좋아요', '팔로잉' 등의 기술 구현

<hr><h4>A. 유저 팔로우 기능</h4><hr>

```html
{% extends 'base.html' %}

{% comment %} profile.html {% endcomment %}

{% block content %}
<h1>{{ person.username }}의 프로필 페이지</h1>
{% with followings=person.followings.all followers=person.followers.all %}
<div>
  <div>팔로잉 : <span id="followings-count">{{ followings|length }}</span> / 
    팔로워 : <span id="followers-count">{{ followers|length }}</span></div>
    {% comment %} 프로필 페이지에서 팔로잉과 팔로워의 숫자를 length 필터를 사용해서 구해준다. {% endcomment %}
  {% if user != person %}
  {% comment %} 만일 login유저와 조회하고 있는 프로필의 유저가 다를 경우 {% endcomment %}
  <div>
    <form id="follow-form" data-user-id="{{ person.pk }}">
      {% comment %} <script>태그에서 person.pk 값을 사용할 수 있게 하기 위해서 data-user-id 기술 {% endcomment %}
      {% csrf_token %} 
      {% if user in followers %}
      {% comment %} 만약에 이미 로그인 유저가 조회하고 있는 프로필 유저를 팔로우하고 있을 경우 {% endcomment %}
      {% comment %} 팔로우의 상태에 따라 다른 버튼을 보여준다. {% endcomment %}
      <button id="followBtn">언팔로우</button>
      {% else %}
      <button id="followBtn">팔로우</button>
      {% endif %}
    </form>
  </div>
  {% endif %}
</div>
{% endwith %} 
{% endblock content %} 

{% block script %}
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
{% comment %} 비동기 작동을 위한 라이브러리 불러오기 {% endcomment %}
<script>
  const form = document.querySelector("#follow-form")
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  form.addEventListener("submit", function (event) {
    event.preventDefault()

    const userId = event.target.dataset.userId
    // person.pk 값을 userId에 담아준다.

    axios({
      method: "post",
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken}
    })
      .then((response) => {
        const followBtn = document.querySelector('#followBtn')
        if (response.data.is_followed===false) {
          // 응답 받은 is_followed정보가 false일 경우, 즉 팔로우를 하고 있지 않을 경우
          followBtn.innerText = '팔로우'
        } else {
          followBtn.innerText = '언팔로우'
        }

        // 태그 선택하기
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')
         
        // context로 넣은 데이터는 response에 담긴다.
        const followingsCount = response.data.followings_count
        const followersCount = response.data.followers_count
    
        followingsCountTag.innerText = followingsCount
        followersCountTag.innerText = followersCount
      })
      
      .catch((error) => {
        console.log(error.response)
      })

  })
</script>
{% endblock script %}
```

```python
# views.py

@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # 유저 정보를 person에 담아준다.
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                # 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            context = {
                'is_followed' : is_followed,
                'followings_count' : person.followings.count(),
                'followers_count' : person.followers.count()
            }
            return JsonResponse(context)
    return redirect('accounts:profile', person.username)

```

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

- `    person = get_object_or_404(get_user_model(), username=username)`을 통해서 `profile.html`에 보여줄 유저 정보를 가져온다.
- `request`를 보내는 요청자와 조회하고 있는 `profile`의 정보가 다를 경우만 `follow`기능을 가능하게 해줘야한다.
- `context`에 `is_followed`, `followings_count`, `followers_count` 정보를 담아서 `JsonResponse`로 보낸다.
  - 해당 정보를 보낼 경우, `profile.html`의 `<script> block`내에서 `response.data.`을 통해 정보에 접근할 수 있다.
- `models.py`에서 `ManyToManyField`의 `related_name`속성을 `followers`로 정의해 뒀기 때문에, 역참조시 `.followers`를 사용해야 한다.

<hr><h4>B. 리뷰 좋아요 기능</h4><hr>

```python
from django.db import models
from django.conf import settings

class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Community</h1>
  <hr>
  {% for review in reviews %}
  {% comment %} review를 복수의 갯수로 가져와야하기 때문에 for문을 통해서 뽑아준다. {% endcomment %}
    <p>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></p>
    <p>글 번호: {{ review.pk }}</p>
    <p>글 제목: {{ review.title }}</p>
    <p>글 내용: {{ review.content }}</p>
    <form id="like-forms" data-review-id="{{ review.pk }}">
      {% comment %} <script>블록 내에서 review.pk 값을 가져오기 위해 data-review-id 정의 {% endcomment %}
      {% csrf_token %}
      {% if user in review.like_users.all %}
        {% comment %} 한 페이지에 버튼 등 여러 개 있다면 pk로 구분해줘야 함 {% endcomment %}
        <button id="like-{{ review.pk }}">좋아요 취소</button>
      {% else %}
        <button id="like-{{ review.pk }}">좋아요</button>
      {% endif %}
    </form>
    <p>
      {% comment %} review.pk를 통해서 어떤 review인지 분류해줘야 한다. {% endcomment %}
      <span id="likes-count-{{ review.pk }}">{{ review.like_users.all|length }}</span> 명이 이 글을 좋아합니다.
    </p>
    <a href="{% url 'community:detail' review.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    {% comment %} 리뷰마다 좋아요 기능 붙여줘야 하므로 forEach와 querySelectorAll 사용 {% endcomment %}
    const likeForms = document.querySelectorAll('#like-forms')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    // foreach를 통해서 for문을 수행한다.
    likeForms.forEach((likeForm) => {
      likeForm.addEventListener('submit', function (event) {
        event.preventDefault()
        const reviewId = event.target.dataset.reviewId
  
        axios({
          method: 'post',
          url: `${reviewId}/like/`,
          headers: {'X-CSRFToken': csrftoken},
        })
          .then((response) => {
            const likeButton = document.querySelector(`#like-${reviewId}`)
            if (response.data.is_liked===true) {
              // 좋아요 취소 버튼 출력
              likeButton.innerText = '좋아요 취소'
            } else {
              // 좋아요 버튼 출력
              likeButton.innerText = '좋아요'
            }
            // 좋아요 개수 
            const likesCountTag = document.querySelector(`#likes-count-${reviewId}`)
            const likesCount = response.data.likes_count
            likesCountTag.innerText = likesCount
          })
          .catch((error) => {
            console.log(error.response)
          })
      })
    })
  </script>
{% endblock script %}
```

```python
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)

@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likes_count': review.like_users.count()
        }
        return JsonResponse(context)
        # return redirect('community:index') # 이건 지우기
    return redirect('accounts:login')
```

- `review`에 대한 `like`기능 같은 경우, `follow`와 비슷한 기능을 가지지만, `index.html`에 각각의 `review`마다 다수의 `button`을 생성해야 하기 때문에 `for`문을 사용한다.
  - `for`문 내에 `button`의 `id`값에 `review.pk`값을 같이 넣어줘서, 각각의 버튼이 각각의 `review`와 연결되게 작성한다.
- `views.py`에서 `like`함수를 구현할 때,`is_liked`값 변경을 통해서 `index.html`의 `button`값을 변경해준다.
  - `is_liekd`와 `likes_count`정보를 `context`에 담아서 `JsonResponse`를 실행해준다.
- 전체적으로 `follow`기능과 비슷하지만, 여러가지의 `review`를 동시에 보여줘야 하기 때문에 `querySelectorAll`을 사용하고, `for`문 내에서 `review.pk`값을 같이 가지고 가 줘야 한다는 차이가 있다.
- `request.user.is_authenticated`조건을 추가해서 인증 된 사용자만 `like`를 할 수 있도록 해준다.

<hr><h4>C. Movies 앱 기능</h4><hr>

**`index.html`**

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Movies</h1>
  <a href="{% url 'movies:recommended' %}"><button>추천영화</button></a>
  {% for movie in movies %}
    <h3>{{ movie.title }}</h3>
    <p>
      {% for genre in movie.genres.all %}
        <span>{{ genre.name }}</span>
      {% endfor %}
    </p>
    {% if movie.overview %}
      <p>{{ movie.overview|truncatechars:60 }}</p>
    {% else %}
      <p>줄거리 없음</p>
    {% endif %}
    <a href="{% url 'movies:detail' movie.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- `for`문을 통해서 모든 영화 정보를 보여준다.

**`detail.html`**

```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ movie.title }}</h1>
  <p>
    genre : 
    {% for genre in movie.genres.all %}
    <span>{{ genre.name }}</span>
    {% endfor %}
  </p>
  <p>popularity : {{ movie.popularity }}</p>
  <p>vote average : {{ movie.vote_average }}</p>
  <p>overview : {{ movie.overview }}</p>
  <img src="{{ movie.poster_path }}" alt="">
{% endblock %}
```

-  `movie`세부 정보를 보여주고 `img`태그를 활용해서 포스터를 보여준다.

**`recommended.html`**

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Recommended Movies</h1>
  <a href=""><button>재추천</button></a>
  {% for movie in recommended_movies %}
    <h3>{{ movie.title }}</h3>
    <p>
      {% for genre in movie.genres.all %}
        <span>{{ genre.name }}</span>
      {% endfor %}
    </p>
    {% if movie.overview %}
      <p>{{ movie.overview|truncatechars:60 }}</p>
    {% else %}
      <p>줄거리 없음</p>
    {% endif %}
    <a href="{% url 'movies:detail' movie.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- `views.py`에서 `recommendde`함수를 통해서 10개의 랜덤 영화 목록을 받는다.
- 받은 영화 목록을 `for`문을 통해서 넣어준다.

**`views.py`**

```python
import random
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie


@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    # movie = get_object_or_404(Movie.objects.prefetch_related('genres'), pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

@require_safe
def recommended(request):
    movies = Movie.objects.all()
    recommended_movies = random.sample(list(movies), 10)  # 랜덤 영화 10개 추천
    context = {
        'recommended_movies': recommended_movies,
    }
    return render(request, 'movies/recommended.html', context)
```

- `random.sample(sequence, k)`함수를 통해서 `random`으로 정보를 불러온다.

**`models.py`**

```python
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
```

- `genre`하나에도 여러개의 `movie`가 연결 될 수 있고, `movie`하나에도 여러개의 `genre`가 연결될 수 있기 때문에 `ManyToManyField`를 사용해줘야 한다.

<hr><h4>후기</h4><hr>

- 동기적 처리를 AJAX를 통해서 비동기로 처리하는 방법을 학습했다.
- model간의 관계 설정을 통해 참조하는 방법을 학습했다.