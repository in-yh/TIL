"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 장고 공식문서 참조(django managing static files 구글링)
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기
#   사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고나서,
#   실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
#       업로드 된 파일의 URL == settings.MEDIA_URL
#       위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
