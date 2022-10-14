from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('<str:username>/', views.profile, name='profile'), # 이렇게 하면 위에 주소들(str)과 겹쳐서 안 쓰는게 좋음, 위에 쓰면 더더욱 안됨 
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]

