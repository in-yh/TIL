from django import forms
from .models import Review, Comment, Recomment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user', 'like_users']


class RecommentForm(forms.ModelForm):

    class Meta:
        model = Recomment
        exclude = ['comment', 'user', 'like_users']
