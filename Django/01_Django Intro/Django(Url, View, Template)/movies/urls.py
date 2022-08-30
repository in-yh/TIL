from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('home/', views.home, name='home') 
    # 'home/' 으로 넣으면 주소창에 movies/home 추가해야함.
    # ''이면 주소창에 movies만 추가
    # 즉, 실행되는 주소창 이름이 달라지는 것임!
]
