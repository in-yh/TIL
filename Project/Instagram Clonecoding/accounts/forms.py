from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields 
        # 상속받은 거 그대로 가져옴
        # password는 저장하지 않음. 그냥 인증수단


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능함.
        # 다 보여주지 않기 위해 여기서 정의해줘야 함.
        fields = ('username', 'email', 'first_name', 'last_name',)


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',) # user 필드는 안보이게 하기