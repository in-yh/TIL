from django.urls import path
from . import views # from . 은 현재 위치를 의미

app_name = 'articles' # index가 같아버리면 안 되니 app_name 지정
urlpatterns = [
    path('', views.index, name='index'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('catchword/<name>/', views.catchword, name='catchword'), # 마치 상담일지 같은.. 같은 포맷에 이름만 다르게 할 때
]

# 2가지 지원
# 1. string (default)
#            <str:str1>
# 2. integer <int:num1>