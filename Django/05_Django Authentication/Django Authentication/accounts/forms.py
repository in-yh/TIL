from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta): # UserCreationForm의 Meta 부분을 상속
        model = get_user_model() # User 참조할 때 직접적으로 참조하는 것을 권장하지 않음. 간접참조(현재프로젝트에서 활성화된 사용자유저모델을 반환해주는 함수 : get_user_model())
        fields = UserCreationForm.Meta.fields + ('email',) # username말고 더 받고 싶을 때 (존재하지 않는 필드를 하면 에러) 공식문서 참조하면 optional
        # password는 저장하지 않음, 그냥 인증수단


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # admin 인터페이스에서 사용되는 ModelForm이기 때문에 일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능함.
        # 다 보여주지 않기 위해 여기서 정의해줘야 함.
        fields = ('username', 'first_name', 'last_name',) 
        # 비밀번호 수정은 따로 해줘야함