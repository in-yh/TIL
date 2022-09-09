from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required # 로그인되어 있는지 확인하고 밑에 보여줌. 로그인 안 된 상태로 접근하려면 로그인창으로 돌려줌 오.. 1. 장고는 우리 로그인 주소를 어떻게 알았을까 : 모름 @login_required가 보내는 곳이 accounts/login인데 우리가 accounts로 쓰고 있어서 딱 맞았지 2. url에 뭔가 붙어 있음(next parameter) : login이 성공하면 직전 주소로 보내주기 위해 남겨줌, 근데 안가, login에서 주소를 바꿔줘야 해
# /articles/create/ 로 강제 접속 시도하면
# 로그인 페이지(login.html)로 리다이렉트 후 /accounts/login/?next=/articles/create/ url이 뜸
# 인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨
# ex) ?next=/articles/create/
# "next" query string parameter
# 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect하기 위해 장고가 제공해주는 쿼리 스트링 파라미터
# 해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게 됨
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


## 두 데코레이터로 인해 발생하는 구조적 문제
# 먼저 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
# delete view함수의 @login_required로 인해 로그인 페이지로 리다이렉트, url은 /accounts/login/?next=/articles/1/delete/
# 로그인 하면 (지워져야 하는데..)
# @require_POST에 막혀 405에러
# 이유 : 로그인 성공 이후 GET방식으로 next 파라미터 주소에 리다이렉트 되기 때문
## 두 가지 문제
# redirect 과정에서 POST 요청 데이터의 손실
# redirect로 인한 요청은 GET 요청 메서드로만 요청됨
# 해결방안 : @login_required는 GET request method를 처리할 수 있는 view 함수에서만 사용해야함
# @login_required
@require_POST
def delete(request, pk):
    if request.user.is_authenticated: # 그래서 안에 넣음 / 비로그인상태에서 delete 누르면 index페이지로 감
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
