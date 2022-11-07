from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment, Recomment
from .forms import ReviewForm, CommentForm, RecommentForm
from django.http import JsonResponse


@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    recomment_form = RecommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'recomment_form': recomment_form,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likes_count': review.like_users.count()
        }
        return JsonResponse(context)
        # return redirect('community:index') # 이건 지우기
    return redirect('accounts:login')


@require_POST
def like_comment(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk) # 특정 댓글
        # request.user가 댓글을 좋아한 유저 목록 안에 있다면 remove
        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')


@require_POST
def create_recomment(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        recomment_form = RecommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.user = request.user
            recomment.save()
            return redirect('community:detail', review_pk)
        context = {
            'recomment_form': recomment_form,
        }
        return render(request, 'community/detail.html', context)
    return redirect('accounts:login')


@require_POST
def like_recomment(request, review_pk, comment_pk, recomment_pk):
    if request.user.is_authenticated:
        recomment = get_object_or_404(Recomment, pk=recomment_pk)
        if request.user in recomment.like_users.all():
            recomment.like_users.remove(request.user)
        else:
            recomment.like_users.add(request.user)
        return redirect('community:detail', review_pk)
    return redirect('accounts:login')