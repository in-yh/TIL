from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseForbidden

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user # 사용자로부터 받는게 아니라.. request에서 받음..
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk) # 특정 게시글은 있어
    comment_form = CommentForm()
    comments = article.comment_set.all() # 역참조, 이 게시물이 가진 모든 댓글을 가지고 옴
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user: # 삭제를 요청한 사람과 작성한 사람이 같다면, 삭제
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated: # 인증되지 않을 경우(401)
#         if request.user == article.user: # 인증은 되었으나 삭제할 권한이 없어(403)
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden() # 403 보여줌
#     return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user: # 수정하려는 사람과 작성한 사람이 같다면
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else: # 수정하려는 사람과 작성한 사람이 다르다면
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST # 그 화면에서 하는 것이기 때문에 POST (GET이 필요가 없는데..)
def comments_create(request, pk): 
    if request.uesr.is_authenticated: # 인증된 사용자인지 확인
        article = Article.objects.get(pk=pk) # 밑에 article이 나오므로 여기서 정의해줘야 함, 그리고 외래키 데이터 입력에 필요한 객체 준비
        comment_form = CommentForm(request.POST) 
        if comment_form.is_valid(): # forms.py에서 article은 exclude 되어있기 때문에 content만 넣어도 통과
            # article.pk는 넣어지지 않아서 에러 발생
            # save 메서드의 commit 옵션값이 있는데 기본적으로 True지만 False로 바꿔주면 저장하지 않고 (save 되었을 때 결과물)을 하나 줌
            comment = comment_form.save(commit=False) # 인스턴스 필요
            comment.article = article # 객체 그대로 집어넣어
            comment.user = request.user # 요청객체를 넣어줌, user는 request 객체에서 가져옴
            comment.save() # article, content 모두 있으므로 저장
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login') # 인증된 사용자가 아니면, login으로 보내주면 오..


# def comments_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk # 1. comment에서 article.pk를 조회할 수 있으니..
#     comment.delete()
#     return redirect('articles:detail', article_pk)  


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user: # 삭제되기 전 확인
            comment.delete()
    return redirect('articles:detail', article_pk)

# 댓글 수정은 그 페이지에서 수정 가능(다른 페이지로 가는게 아니라) -> 지금은 불가, 자바스크립트가 구현

