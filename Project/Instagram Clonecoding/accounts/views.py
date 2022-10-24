from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileUpdateForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # request를 기본인자로 받는다.
        if form.is_valid():
            auth_login(request, form.get_user()) # 유저정보 받을 때는 get_user() 메서드 이용
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def signup(request):
    # 이미 로그인 된 사용자가 접근하면 메인 화면으로 이동
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            # 회원가입이 완료되면 로그인이 된 상태로 메인 화면으로 이동
            auth_login(request, user) # 위 user를 여기에 씀
            profile = profile_form.save(commit=False) # user_id 여기서 정의
            profile.user = request.user
            profile.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
        profile_form = ProfileUpdateForm()
    context = {
        'form': form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required # GET방식이 있으므로 가능? ?next=/accounts/delete/로 돌려주려면 그만한 처리가 필요했던 것 같음
def delete(request):
    # if request.user.is_authenticated: # 로그인 안하면 돌려보냄
        # 회원탈퇴를 위한 한 번 더 확인받는 과정
        if request.method == 'POST':
            request.user.delete() # 삭제는 그냥 delete..
            auth_logout(request) # 로그아웃 인자는 request 하나뿐
            return redirect('posts:index')
        else:
            return render(request, 'accounts/delete.html') 
    # return redirect('accounts:login')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) # 인스턴스가 뒤에
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST) # 인스턴스를 앞에
        if form.is_valid():
            form.save()
            # 비밀번호 변경해도 로그인 풀리지 않게 함
            # 비밀번호 변경하면서 기존 세션을 업데이트 해주는 과정이 필요
            update_session_auth_hash(request, form.user) # 현재 요청과 새 세션 데이터가 파생될 업데이트된 사용자 객체를 가져오고, 세션 데이터 적절하게 업데이트해줌
            return redirect('posts:index')
    else:
        form = PasswordChangeForm(request.user) # 유저정보 적는거 필수! PasswordChangeForm은 SetPasswordForm를 상속받는데 저기서 필수인자로 해놔서..
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username) # username이 요청받은 username과 같은 거 뽑기
    profiles = person.profile_set.all() # User 객체인 person(1)에서 여러 profile들(N)을 역참조로 모두 가져오기
    context = {
        'person': person,
        'profiles': profiles,
    }
    return render(request, 'accounts/profile.html', context)

def profile_update(request, profile_pk):
    profile = Profile.objects.get(pk=profile_pk) # profile 가져오기
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile) # 이전 정보로 profile 넣어주기
        if form.is_valid():
            form.save() # user정보는 이미 고정이기에 다시 저장해줄 필요 없음
            return redirect('accounts:profile', profile.user.username) # profile 보낼 때는 username을 인자로 보내야하므로 username은 User필드에 있음
    else:
        form = ProfileUpdateForm(instance=profile)
    context = {
        'form': form,
        'profile': profile, # render로 보낼 때 인자가 필요하다면 context에 명시해준다고 생각해야 함
    }
    return render(request, 'accounts/profile_update.html', context)

# 문제점1 : profile 수정할 때 정보가 없으면 에러 발생 => 회원가입 시, 프로필 생성할 수 있도록 form 같이 넣어줌!
# 문제점2 : user 1개당 profile 1개만 생성되게 함(여러개면 이상해서..)