from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.articles_list), # 템플릿 없기 때문에 name 안해도 됨
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
