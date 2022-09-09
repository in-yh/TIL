from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login # init 파일에 있음. view함수 login과의 충돌 방지 위해 auth_login으로 변경
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import User


# def index(request):
#     users = User.objects.all()
#     context = {
#         'users' : users,
#     }
#     return render(request, 'accounts/index.html', context)


def login(request): # 로그인 정보 입력할 함수와 인증할 함수, 총 2개 필요
    if request.user.is_authenticated: # 인증된 사람이라면 로그인 로직을 수행할 수 없도록 처리
        return redirect('articles:index') # login 접근하려해도 로그인상태라면 index로 돌려보냄

    # 페이지 GET, 인증 POST
    if request.method == "POST": # 로그인 시켜주는 코드
        form = AuthenticationForm(request, request.POST) # ModelForm일 때, request.POST였음. # 첫 번째 인자가 request!!, 두 번째가 data
        # form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 로그인은 save 아니고 session을 만듦 # 입력된 데이터 판단하여
            auth_login(request, form.get_user()) # request, 유저정보(AuthenticationForm이 제공하는 인스턴스 메서드, 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환) # 현재 세션에 데이터 입력
            # # def get_user(self):
            # #   return self.user_cache
            # return redirect('articles:index') 
            return redirect(request.GET.get('next') or 'articles:index') # 단축평가, 주소창에 next가 있으면 그 주소로 보냄 / html에서 action을 빈칸으로 둬야 잘 실행함(action을 한 곳으로 보내면 안 됨)
    else:
        # form 안 만들고 built-in form을 쓸거임.
        form = AuthenticationForm() # ModelForm이 아니라 Form임 (DB에 저장할 필요 없으니)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
    # 개발자도구에 Application 내 value값이 'django_session'의 session_key값임 (더 중요한 값은 DB에 있음)
    # 모든 쿠키 데이터를 서버에 저장하면 안 되나? 그러면 서버는 많은 요청을 처리해야해서 부하가 많이 걸림
    # 그러나 브라우저도 보안 쎔. 쉽게 value값을 바꿀 순 없음.

def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')

def signup(request): # 2개의 view함수 즉, create와 똑같음
    if request.method == 'POST':
        # UserCreationForm 모델폼에서.. Meta에 기본유저가 들어가있음. (Manager isn't available; 'auth.User' has been swapped for 'accounts.User')
        # class Meta:
        #   model = User
        form = CustomUserCreationForm(request.POST) # POST한 거 가져와야지!!
        if form.is_valid():
            user = form.save() # 공식문서 참조하면 user로 리턴
            # 회원가입 된 후 로그인 상태로 index페이지 보여주기
            auth_login(request, user) # 위 user를 여기에 씀
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request): # 회원탈퇴
    # 유저데이터 가져와야 하는데.. request
    request.user.delete()
    # 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우
    # 로그아웃 후 탈퇴하면 request.user을 불러올 수 없음.
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user) # 유저정보는 request.user에 있음
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST) # 유저정보가 먼저 들어감
        if form.is_valid():
            form.save()
            # user = form.save() # 공식문서 확인해보면 save하면 self.user를 반환하기에
            # 비밀번호 변경하면 로그아웃이 됨(기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함)
            # 비밀번호 변경하면서 기존 세션을 업데이트 해주는 과정이 필요 (update_session_auth_hash(request, user))
            update_session_auth_hash(request, form.user) # 현재 요청과 새 세션 데이터가 파생될 업데이트된 사용자 객체를 가져오고, 세션 데이터 적절하게 업데이트해줌
            # update_session_auth_hash(request, user) # 형식 : 요청, 유저정보
            return redirect('alticles:index')
    else:
        form = PasswordChangeForm(request.user) # 유저정보 적는거 필수! PasswordChangeForm은 SetPasswordForm를 상속받는데 저기서 필수인자로 해놔서..
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
