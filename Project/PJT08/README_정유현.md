# PJT 08

### 이번 pjt 를 통해 배운 내용

- AJAX 통신과 JSON 구조에 대한 이해
- Database N:1/M:N에 대한 이해
- 영화 추천 알고리즘 설계



## A. 유저 팔로우 기능

- 요구 사항 :

  * 팔로우 버튼을 클릭하는 경우, AJAX 통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성
  * 프로필 페이지에 해당 사용자를 팔로우할 수 있는 버튼 표시
  * 프로필 페이지에 팔로워 수와 팔로잉 수 표시

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * views.py에서 데이터를 JSON 형태로 보내주기
    * profile.html에서 AJAX 활용
      * axios 라이브러리를 이용하여 요청을 보낼 때, url과 csrftoken 처리
      * axios 요청 후 응답데이터 출력하기(태그 선택 -> response 데이터 가져오기 -> 태그 안에 데이터 넣기)
  
  ```python
  # accounts/views.py
  @require_POST
  def follow(request, user_pk):
      if request.user.is_authenticated:
          person = get_object_or_404(get_user_model(), pk=user_pk)
          user = request.user
          if person != user:
              if person.followers.filter(pk=user.pk).exists():
                  person.followers.remove(user)
                  # 팔로우 여부를 확인하기 위한 is_followed 변수 작성
                  is_followed = False
              else:
                  person.followers.add(user)
                  is_followed = True
              # context에 담아서 JSON으로 응답
              context = {
                  'is_followed' : is_followed,
                  'followings_count' : person.followings.count(),
                  'followers_count' : person.followers.count()
              }
              return JsonResponse(context)
      return redirect('accounts:profile', person.username)
  ```
  
  ```html
  <!-- base.html -->
  	{% block script %} 
  	{% endblock script %}
  	<!-- base에 block태그 넣어주기!! 넣어주지 않으면 실행 안 됨 -->
  </body>
  
  <!-- accounts/profile.html -->
  {% extends 'base.html' %} 
  {% block content %}
  <h1>{{ person.username }}의 프로필 페이지</h1>
  {% with followings=person.followings.all followers=person.followers.all %}
  <div>
    <div>팔로잉 : <span id="followings-count">{{ followings|length }}</span> / 팔로워 : <span id="followers-count">{{ followers|length }}</span></div>
    {% if user != person %}
    <div>
      <form id="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %} 
        {% if user in followers %}
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
  
  <!-- block 태그 추가 -->
  {% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> // axios CDN
  <script>
    const form = document.querySelector("#follow-form")
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
    form.addEventListener("submit", function (event) {
      event.preventDefault() // form 태그의 submit 실행 막기
  
      const userId = event.target.dataset.userId
  	
      // 1. url
      // 2. csrf
      axios({
        method: "post",
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken}
      })
        .then((response) => {
          // 버튼 출력 바꿔주기(버튼 태그 선택 -> response 데이터(views.py에서 context로 담긴 데이터)에 따라 -> 태그 안에 데이터 넣기)
          const followBtn = document.querySelector('#followBtn')
          if (response.data.is_followed===false) {
            followBtn.innerText = '팔로우'
          } else {
            followBtn.innerText = '언팔로우'
          }
  
          // 태그 선택하기
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCountTag = document.querySelector('#followers-count')
           
          // response 데이터 가져오기
          const followingsCount = response.data.followings_count
          const followersCount = response.data.followers_count
      
          // 태그 안에 데이터 넣기
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
  
  - 이 문제에서 어려웠던 점
    * base.html에 block태그 잊기 쉬운데 태그 넣어주지 않으면 실행조차 안 되기에 주의하기!
  - 내가 생각하는 이 문제의 포인트
    * AJAX 활용하여 비동기 웹 통신 구현(axios 라이브러리 이용)

------

 

## B. 리뷰 좋아요 기능

- 요구 사항 :

  * 좋아요 버튼을 클릭하는 경우, AJAX 통신을 이용하여 서버에서 JSON 데이터를 받아와 상황에 맞게 HTML 화면을 구성
  * 전체 리뷰 목록 조회 페이지에 좋아요 버튼과 좋아요 개수를 표시
  * 이미 좋아요 버튼을 누른 경우 좋아요 취소 버튼 표시

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 한 페이지에 여러 개 리뷰를 보여준다.
      * 리뷰마다 form이 있어서 forms를 선택할 때 여러 개 선택할 수 있는 querySelectorAll 사용
      * forms를 for문 순회한다.
      * 모든 태그들을 review.pk로 구분해주고 script에서는 reviewId로 구분하여 선택한다.
  
  ```python
  # community/views.py
  @require_POST
  def like(request, review_pk):
      if request.user.is_authenticated:
          review = get_object_or_404(Review, pk=review_pk)
          user = request.user
  
          if review.like_users.filter(pk=user.pk).exists():
              review.like_users.remove(user)
              # 좋아요 여부를 확인하기 위한 is_liked 변수 작성
              is_liked = False
          else:
              review.like_users.add(user)
              is_liked = True
          # context에 담아서 데이터 전송
          context = {
              'is_liked': is_liked,
              'likes_count': review.like_users.count()
          }
          return JsonResponse(context)
      return redirect('accounts:login')
  ```
  
  ```html
  <!-- community/index.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Community</h1>
    <hr>
    {% for review in reviews %}
      <p>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></p>
      <p>글 번호: {{ review.pk }}</p>
      <p>글 제목: {{ review.title }}</p>
      <p>글 내용: {{ review.content }}</p>
      <form id="like-forms" data-review-id="{{ review.pk }}">
        {% csrf_token %}
        {% if user in review.like_users.all %}
          {% comment %} 한 페이지에 버튼 등 여러 개 있다면 review.pk로 구분해줘야 함 {% endcomment %}
          <button id="like-{{ review.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-{{ review.pk }}">좋아요</button>
        {% endif %}
      </form>
      <p>
        <span id="likes-count-{{ review.pk }}">{{ review.like_users.all|length }}</span> 명이 이 글을 좋아합니다.
      </p>
      <a href="{% url 'community:detail' review.pk %}">[detail]</a>
      <hr>
    {% endfor %}
  {% endblock %}
  
  {% block script %}
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
      // 리뷰마다 좋아요 기능 붙여줘야 하므로 forEach와 querySelectorAll 사용
      const likeForms = document.querySelectorAll('#like-forms')
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      
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
  
  - 이 문제에서 어려웠던 점
    * 선택하려고 했던 태그들을 review.pk로 구분해주고 script에서는 reviewId로 선택한다.
    
  - 내가 생각하는 이 문제의 포인트 
  
    * form이 하나 있는게 아니라 review마다 form이 하나씩 있는 것 즉, form이 여러 개이기 때문에 form마다의 구분이 필요

------

 

## C. Movies 앱 기능

* 요구 사항: 
  * 전체 영화 목록 조회(index)
  * 단일 영화 상세 조회(detail)
  * 영화 추천 기능(사용자가 인증되어 있다면, 적절한 알고리즘을 활용하여 10개의 영화를 추천 및 제공)

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 랜덤 영화 10개를 추천해주는 기능 추가
  
  ```python
  # movies/views.py
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
  
  ```html
  <!-- movies/index.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Movies</h1>
    <a href="{% url 'movies:recommended' %}"><button>추천영화</button></a>
    {% for movie in movies %}
      <h3>{{ movie.title }}</h3>
      <p>
        {% comment %} 특정 movie의 모든 장르 번호 뽑기 {% endcomment %}
        {% for genre in movie.genres.all %} 
          {% comment %} 장르의 번호를 이름으로 바꾸기  {% endcomment %}
          <span>{{ genre.name }}</span>
        {% endfor %}
      </p>
      {% if movie.overview %}
  	  {% comment %} 문자열이 지정된 인수보다 길면 자른다. 잘린문자열을 ...로 표현 {% endcomment %}
        <p>{{ movie.overview|truncatechars:60 }}</p>
      {% else %}
        <p>줄거리 없음</p>
      {% endif %}
      <a href="{% url 'movies:detail' movie.pk %}">[detail]</a>
      <hr>
    {% endfor %}
  {% endblock %}
  
  
  <!-- movies/detail.html -->
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
    {% comment %} .url로 안해도 되는 이유는? {% endcomment %}
    <img src="{{ movie.poster_path }}" alt="">
  {% endblock %}
  
  
  <!-- movies/recommended.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>Recommended Movies</h1>
    {% comment %} 링크를 비우면 같은 페이지로 불러옴(즉, {% url 'movies:recommended'로 실행 %}) {% endcomment %}
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
  
  - 이 문제에서 어려웠던 점
    * `random.sample(list(movies), 10)` random 모듈을 이용해 sample 메서드를 이용하는 것(구글링하여 사용법 이해 필요했음)
    * 재추천할 때 하이퍼링크를 비워두면 현재 url 실행
  - 내가 생각하는 이 문제의 포인트 
    * 랜덤 추천 위한 메서드!(도 가능하지만 평점순으로 추천하는 방법도 구현해봐야겠다!)

------

 

## D. 댓글 좋아요 및 대댓글 기능

* 요구 사항: 
  * 단일 리뷰 상세 조회 페이지에 댓글 좋아요 버튼과 좋아요 개수를 표시
  * 각 댓글에 하위 댓글을 작성할 수 있는 대댓글 기능을 완성

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 댓글:좋아요(M:N) 설정
    * 대댓글:댓글(N:1) / 대댓글:유저(N:1) / 대댓글:좋아요(M:N) 설정
    * forms.py에서 필드는 필요한 것만 출력
    * 좋아요 기능은 request.user가 '댓글이나 대댓글에 좋아요한 유저 목록' 내에 있다면 remove, 없다면 add
    * 대댓글 생성하는 것은 request.POST에 담겨있지 않은 정보들을 처리해주기(commit=False 등)
  
  ```python
  # community/models.py
  class Comment(models.Model):
      content = models.TextField()
      review = models.ForeignKey(Review, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
  
  
  class Recomment(models.Model):
      content = models.TextField()
      comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_recomment')
  
      
  # community/forms.py
  class CommentForm(forms.ModelForm):
  
      class Meta:
          model = Comment
          exclude = ['review', 'user', 'like_users']
  
  
  class RecommentForm(forms.ModelForm):
  
      class Meta:
          model = Recomment
          exclude = ['comment', 'user', 'like_users']
  
          
  # community/urls.py
  urlpatterns = [ ...
      path('<int:review_pk>/comments/<int:comment_pk>/like/', views.like_comment, name='like_comment'),
      path('<int:review_pk>/comments/<int:comment_pk>/recomments/create/', views.create_recomment, name='create_recomment'),
      path('<int:review_pk>/comments/<int:comment_pk>/recomments/<int:recomment_pk>/like/', views.like_recomment, name='like_recomment'),
  ]
  
  
  # community/views.py
  @require_GET
  def detail(request, review_pk):
      review = get_object_or_404(Review, pk=review_pk)
      comments = review.comment_set.all()
      comment_form = CommentForm()
      recomment_form = RecommentForm() # 댓글 서식 출력 위함
      context = {
          'review': review,
          'comment_form': comment_form,
          'comments': comments,
          'recomment_form': recomment_form,
      }
      return render(request, 'community/detail.html', context)
  
  
  @require_POST
  def like_comment(request, review_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk) # 특정 댓글
          # request.user가 댓글을 좋아한 유저 목록 안에 있다면 remove
          if request.user in comment.like_users.all():
              comment.like_users.remove(request.user)
          else:
              comment.like_users.add(request.user)
          return redirect('community:detail', review_pk)
      return redirect('accounts:login')
  
  
  @require_POST
  def create_recomment(request, review_pk, comment_pk):
      if request.user.is_authenticated:
          comment = get_object_or_404(Comment, pk=comment_pk)
          recomment_form = RecommentForm(request.POST)
          if recomment_form.is_valid():
              recomment = recomment_form.save(commit=False)
              recomment.comment = comment
              recomment.user = request.user
              recomment.save()
              return redirect('community:detail', review_pk)
          context = {
              'recomment_form': recomment_form,
          }
          return render(request, 'community/detail.html', context)
      return redirect('accounts:login')
  
  
  @require_POST
  def like_recomment(request, review_pk, comment_pk, recomment_pk):
      if request.user.is_authenticated:
          recomment = get_object_or_404(Recomment, pk=recomment_pk)
          if request.user in recomment.like_users.all():
              recomment.like_users.remove(request.user)
          else:
              recomment.like_users.add(request.user)
          return redirect('community:detail', review_pk)
      return redirect('accounts:login')
  ```
  
  ```html
  <!-- community/detail.html -->
  {% extends 'base.html' %}
  
  {% block content %}
    <h2 class="text-center">DETAIL</h2>
    <h3>{{ review.pk }} 번째 글</h3>
    <hr>
    <p>제목: {{ review.title }}</p>
    <p>영화 제목: {{ review.movie_title }}</p>
    <p>내용: {{ review.content }}</p>
    <p>평점: {{ review.rank }}</p>
    <p>작성 시각: {{ review.created_at }}</p>
    <p>수정 시각: {{ review.updated_at }}</p>
    <hr>
    <h4>댓글 목록</h4>
    {% if comments|length %}
      <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
    {% endif %}
    {% for comment in comments %}
      <ul>
        <li>
          {{ comment.user }} - {{ comment.content }}
            <form style="display:inline;" action="{% url 'community:like_comment' review.pk comment.pk %}" method="POST">
              {% csrf_token %}
              {% if request.user in comment.like_users.all %}
                <button>좋아요 취소</button>
              {% else %}
                <button>좋아요</button>
              {% endif %}
              <span>{{ comment.like_users.count }}</span>
            </form>
  
            {% comment %} 대댓글 목록 보여주기 {% endcomment %}
            {% for recomment in comment.recomment_set.all %}
              <ul><li>
                {{ recomment.user }} - {{ recomment.content }}
                <form style="display:inline;" action="{% url 'community:like_recomment' review.pk comment.pk recomment.pk %}" method="POST">
                  {% csrf_token %}
                  {% if request.user in recomment.like_users.all %}
                    <button>좋아요 취소</button>
                  {% else %}
                    <button>좋아요</button>
                  {% endif %}
                  <span>{{ recomment.like_users.count }}</span>
                </form>
              </li></ul>
            {% endfor %}
        </li>
      </ul>
      
      <form action="{% url 'community:create_recomment' review.pk comment.pk %}" method="POST">
        {% csrf_token %}
        {{ recomment_form }}
        <button>대댓글 작성</button>
      </form>
      <hr>
    {% empty %}
      <p><b>댓글이 없어요..</b></p>
    {% endfor %}
  
    {% if user.is_authenticated %}
      <form action="{% url 'community:create_comment' review.pk %}" method="POST">
        {% csrf_token %}
        {{ comment_form }}
        <input type="submit">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">[댓글을 작성하려면 로그인하세요.]</a>
    {% endif %}
    <a href="{% url 'community:index' %}">[back]</a>
  {% endblock  %}
  ```
  
  - 이 문제에서 어려웠던 점
    * 어려운 건 없었으나, models.py -> forms.py -> urls.py -> views.py -> html 까지 여러 파일을 수정해야 하고, 생성되는 view함수도 많아서 시간이 꽤 소요됨
  - 내가 생각하는 이 문제의 포인트 
    * 모델 관계 파악만 잘 하면 구현은 가능 (효율적인지는 모르겠으나..)

------

 

# 후기

- AJAX의 충분한 연습과 감을 익힌 프로젝트였다! 응용이 가능할런지 모르겠지만..
- 대댓글 구현을 통해 N:1 M:N 모델 관계 복습 완료! 그러나 댓글 모델 안에 댓글을 Foreignkey('self')로 받는 방법이 있었다.. 내가 구현할 수 있을지는 모르겠지만 공부는 해보자!
- 첫 페어 프로젝트!