from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user',) # models에서 user 추가한 후 여기서 빼줘야 함


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article', 'user',) # 1. article, user 컬럼은 보여지지 않게 함 2. view함수에서 처리해준다
        # settings.py BASE_DIR / 로 고쳐주면 새로고침 안해도 됨
