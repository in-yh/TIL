from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comment

# 일단 로그인 안해도 index는 볼 수 있게 함
@require_safe
def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # 두번째 인자는 이미지 파일
        if form.is_valid():
            post = form.save(commit=False) # models.py에서 user 만들고 해줘야 함!
            post.user = request.user
            post.save()
        return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

# GET 방식을 처리할 수 있을 때만 @login_required 사용 가능? 이 상태에서는 그냥 되네? 'redirect 과정에서 POST 요청 데이터의 손실'만 되는 것인가.. 아니면 주소를 정해주지 않아서?
@require_POST
def delete(request, pk):
    if request.user.is_authenticated: 
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect('posts:index') # 비로그인 상태도 delete 누르면 인덱스로 돌려보내줌

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # 인스턴스가 뒷쪽으로(비밀번호 변경할 때와 serializer 때와 다름)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/form.html', context)

@require_POST
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:index') # if절 해당 안 될 때도 고려 위해 

@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:index')
    
@require_POST
def like(request, post_pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=post_pk)
        if request.user in post.like_users.all():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('posts:index')
    return redirect('accounts:login')
        