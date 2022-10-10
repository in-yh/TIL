from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    # 위젯 설정
    # 장르
    A = 'comedy'
    B = 'horror'
    C = 'romance'
    GENRE_CHOICES = [
        (A, '코미디'),
        (B, '공포'),
        (C, '로맨스'),
    ]
    genre = forms.ChoiceField(choices=GENRE_CHOICES)

    # 스코어
    score = forms.FloatField( # django/forms/fields에서 있는지 확인
        widget=forms.NumberInput( # django/forms/widget에서 있는지 확인
            attrs={
                'step' : 0.5,
                'min' : 0,
                'max' : 5,
            }
        )
    )

    # 개봉일
    release_date = forms.DateField( 
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
            }
        )
    )
    
    class Meta:
        model = Movie
        fields = '__all__'