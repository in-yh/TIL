from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # 외래키 데이터는 어디서 받아와야 할까?
    # detail 페이지의 url을 살펴보면 <int:pk>값이 사용되고 있음
    # 댓글의 외래키 데이터에 필요한 정보가 바로 게시글의 pk값
    # 이전에 학습했던 url을 통해 변수를 넘기는 variable routing을 사용
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete'), # 댓글 번호만 필요
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'), # 애초에 두 개 다 받아버린다면
]
