# forms.py를 만듦
from django import forms
from .models import Article

# class ArticleForm(forms.Form): # forms 모듈 안에 Form 클래스를 받음
#     # 사용자로부터 어떠한 데이터를 받을거냐
#     title = forms.CharField(max_length=10) # form에서는 필수값 아님, 제한만 걸뿐
#     content = forms.CharField(widget=forms.Textarea) # form에서는 textfield 존재하지 않음, 이렇게 하려면 widget 사용!
#     # migrate 먼저 해 주고
#     # widget은 출력만 바꿔줌!

#     # DROPDOWN 만들기
#     NATION_A = 'kr' # value값들 , 장고의 스타일가이드 권장사항
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'), # 쉼표! , 사용자에게 보여지는 것
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
#     # 라디오 버튼으로 만들어볼까? widget 검색!
#     # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
    

class ArticleForm(forms.ModelForm):
    # widget 활용(위에 작성하는 것을 권장, formfield 안에 넣어야 함)
    title = forms.CharField(
        label='제목', # label 태그의 내용이 '제목'으로 바뀜
        widget=forms.TextInput(
            attrs={ # 속성 딕셔너리로 넣음
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the title',
                'maxlength' : 10, # 유효성 검사에 영향을 줄까? 안준다! 그냥 입력할 때 입력 안되게 해줌.
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content form-control', # 부트스트랩 form-control 이용 
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required' : 'Please enter your content', # 공백 넣었을 때 에러 표출
        }
    )

    class Meta: # ModelForm의 정보를 작성(model / fields 바꾸면 안됨!)
        model = Article # 어떤 모델을 기반으로 할지, 호출하지 않는다 (괄호를 사용해 인스턴스로 사용하는 게 아님), 반환값이 아닌 참조값이 들어감, 다른 함수에서 "필요한 시점"에 호출하는 경우(예시 views.index)
        fields = '__all__' # 어떤 모델 필드 중 어떤 것을 출력할지, created_at과 updated_at은 출력하진 않았음.
        # textarea로 알아서? models.py TextField()를 textarea로 보여줌 (그냥 form에서는 위젯으로 바꿔줬는데)
        # exclude = ('title',) # 별도로 데이터를 넣을 때, fields와 exclude는 함께 작성해도 되나 권장하지 않음
        # cf) meta data : 데이터를 표현하기 위한 데이터 ex) 사진파일 + 촬영시각,렌즈(사진 데이터에 대한 데이터==사진의 meta data)
