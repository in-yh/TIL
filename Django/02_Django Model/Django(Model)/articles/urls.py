from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), # new/임.. # 갑을 입력할 곳
    path('create/', views.create, name='create'), # 값을 저장
    path('<int:pk>/', views.detail, name='detail'), # 모든 게시글마다 뷰함수와 템플릿파일을 만들 수 없고 글의 번호(pk)를 이용하여 구현해보자! articles/2/ -> 결과물 조회
    path('<int:pk>/delete', views.delete, name='delete'), # 특정 글 삭제할 거니깐
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
]
