from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('catchword/<name>/', views.catchword, name='catchword'), # 마치 상담일지 같은.. 같은 포맷에 이름만 다르게 할 때
]
