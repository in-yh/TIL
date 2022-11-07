from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/like/', views.like, name='like'),
    path('<int:review_pk>/comments/<int:comment_pk>/like/', views.like_comment, name='like_comment'),
    path('<int:review_pk>/comments/<int:comment_pk>/recomments/create/', views.create_recomment, name='create_recomment'),
    path('<int:review_pk>/comments/<int:comment_pk>/recomments/<int:recomment_pk>/like/', views.like_recomment, name='like_recomment'),
]
