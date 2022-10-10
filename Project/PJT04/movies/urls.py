from django.urls import path
from . import views 

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'), # 각각의 영화마다 페이지가 필요하므로 뒤에 pk값을 붙임
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
