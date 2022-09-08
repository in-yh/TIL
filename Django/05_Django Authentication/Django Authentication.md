* Django authentication system
* HTTP Cookies
* Authentication in Web requests
* Authentication with User
* Limiting access to logged-in users



가. Django authentication system

1. Django authentication system(인증 시스템)은  ‘인증’과 ‘권한’ 부여 함께 제공(처리)

2. 필수 구성은 settings.py에 이미 포함 INSTALLED_APPS에서 확인 가능(django.contrib.auth)

3. 개요

   가) 인증 : 신원 확인, 사용자가 자신이 누구인지 확인, 꼭 앱이름을 accounts로 만들기!! (우린 이것만 함) => 앱 생성 및 등록, url 분리 및 매핑

   나) 권한, 허가 : 권한 부여, 인증된 사용자가 수행할 수 있는 작업을 결정

4. 우리는 사실 admin이라는 user을 사용해본 적이 있음.

나. Substituting a custom User model

1. Custom User Model로 대체하기

   가) 기본 User Model이 있음에도 필수적으로 Custom User Model을 사용하길 강력하게 권장!! (회원가입 시 username 대신 email을 사용한다면 기본 User Model을 바꾸는건 매우 어렵기에 대체하자!)

   나) Custom User Model은 기본 User Model과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문(손해볼게 없다!)

   다) Django는 현재 프로젝트에서 사용할 User Model을 결정하는 AUTH_USER_MODEL 설정 값으로 Default User Model을 재정의할 수 있도록 함.

     1)AUTH_USER_MODEL

      * 프로젝트에서 User를 나타낼 때 사용하는 모델

      * 프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음 (user 모델 대체 작업은 첫 migrations 혹은 migrate 전에 해야함!!!!!!!!!!! , 프로젝트 중간일 경우 데이터베이스 초기화하고 진행)

      * 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 함

        * 즉, 첫 번째 마이그레이션 전에 확정 지어야 하는 값

          ```python
          # settings.py
          AUTH_USER_MODEL = 'auth.User' # 인증 관련된 앱인 auth 앱의 User 모델 클래스가 있다. 그게 기본값이다.
          ```

        * settings.py 내에 AUTH_USER_MODEL 같은 건 없음. 그러나 기본값은 존재. 왜 이런식? 실제로는 본체가 따로 있음. global_settings.py(django->conf)라는게 있음(밑바탕) 여기서 AUTH_USER_MODEL이 있다.

다. How to substituting a custom User model (3단계 , 외우기!!)

1. AbstractUser를 상속받는 커스텀 User 클래스 작성 (기본 User Model처럼)

2. AUTH_USER_MODEL 값을 accounts.User로 바꾸기

3. admin.py에 커스텀 User 모델을 등록 (admin에 기본계정은 떴었다. 근데 기본 안쓰니깐 우리거 등록해줘야지)

   cf) AbstractUser : 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스

   * Abstract base classes(추상 기본 클래스)
     * 클래스는 테이블을 만들지만, 그러나 abstract 클래스는 테이블 만들지 않음. 다른 클래스를 생성하기 위한 도장 역할일뿐
     * 그러나 다른 모델을 위해 완전한 기능을 가짐

   주의) 프로젝트 중간에 AUTH_USER_MODEL 변경하기

   * 모델 관계에 영향을 미치기 때문에 훨씬 더 어려운 작업이 필요 (변경사항이 자동으로 수행될 수 없기 때문에 DB스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용해야 하는 등..)
   * 결론 ⇒ 중간 변경 하지마!! 프로젝트 처음에 해!!

   그러나.. 우리는 데이터베이스 초기화 진행해야해

   * 설계도 파일 삭제
     * 마이그레이션 폴더 및 init은 삭제하지 않음
     * 번호가 붙은 파일만 삭제
   * db.sqlite3 삭제
   * makemigrations, migrate 진행

   makemigrations, migrate 하면

   * (makemigrations) accounts에도 migration 파일 생김(유저를 바꿨으니) -> 처음 생성함에도 의존성 있음(12번..) 굉장한 유기성!
   * (migrate) 이제 auth_user 테이블이 아니라 accounts_user 테이블을 사용하게 됨

라. HTTP Cookies

1. 로그인, 로그아웃 배우기 전 알아야 할 개념 : ‘쿠키’ → 데이터 정리?, 쿠키 허용하겠습니까?

2. HTTP

   가) Hyper Text Transfer Protocol

   나) HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약) , 서로 데이터를 전송하기 위한 일종의 약속

   다) 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초

   라) 클라이언트-서버 프로토콜이라고도 부름

   마) 요청(requests) : 클라이언트(브라우저)에 의해 전송되는 메시지

   ​      응답(response) : 서버에서 응답으로 전송되는 메시지

   바) HTTP 특징

     1)비연결지향

       * 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
       * 우리의 착각, 우리가 네이버를 들어가면 우리가 네이버와 연결되어 있다고 생각하지만 실상은 서버가 메인페이지 응답해주고 연결 끊음.

     2)무상태

       * 연결이 끊겼기 때문에 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
       * 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적

   사) 근데 로그인하고 연결 끊으면 웹 사이트 이용할 때 로그인 안 되어 있어야 되지 않나? 

   아) 그 상태 유지해주는게 바로 쿠키!! 서버와 클라이언트 간 지속적인 상태 유지를 위해 ‘쿠키와 세션’이 존재

마. 쿠키

1.  HTTP 쿠키는 ''상태가 있는 세션''을 만들도록 해줌(쿠키 중 상태를 유지시켜주는 세션이 있다.)

2. ‘서버’가 사용자의 웹 브라우저에 전송하는 ‘작은 데이터 조각’

3. 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 ‘사용자의 컴퓨터(브라우저)에 설치’되는 작은 기록 정보 파일

   가) 브라우저(클라이언트)는 쿠키를 로컬에 ‘키-밸류’ 데이터 형식으로 저장

   나) 이렇게 쿠키를 저장해 놓았다가, ‘동일한 서버에 “재요청” 시 저장된 쿠키를 함께 전송’(나 로그인 된 사용자야 라고 담긴 정보를 매요청마다 보냄, 서버랑 손잡고 있는게 아니라서, HTTP의 특징 비연결지향을 바꿀 수 없기 때문)

4. 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨

   가) 이를 이용해 사용자의 로그인 상태를 유지할 수 있음.

   나) 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜 주기 때문

5. 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 "같은 서버"에 재요청 시마다 요청과 함께 저장해 두었던 쿠키도 함께 전송

6. 쿠키 사용 목적(쿠키를 허용하면 맞춤 광고를 띄워주거나 맞춤 상품 권유)

   가) 세션 관리(중요!!) 상태가 있는 세션을 만들어내는 것

     1)로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, “장바구니”(매요청마다 쿠키 정보를 보내고 있다는 말임) 등의 정보 관리

     2)개발자 도구 - Application 탭 - Cookies - 마우스 우측 버튼 - Clear 후 새로고침 => 빈 장바구니로 변경

   나) 개인화

     1)사용자 선호, 테마 등의 설정

   다) 트래킹

     1)사용자 행동을 기록 및 분석

7. 세션

   가) 사이트와 특정 브라우저 사이의 상태를 유지시키는 것 (일련의 발급과정 필요)

   나) 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장

     1)클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달

     2)쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리

   다) session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장(핵심 데이터는 서버에 저장)

8. 쿠키 수명

   가) session cookie

     1)현재 세션이 종료되면 삭제됨

     2)브라우저 종료와 함께 세션이 삭제됨

     3)ex) 세션이 만료되었습니다. ⇒ 세션 유효기간 만료

   나) persistent cookies

     1)지정된 날짜와 기간이 있음.

9. Session in Django

   가) Django는 database-backed sessions 저장방식을 기본 값으로 사용

     1)session 정보는 Django DB에 django_session 테이블에 저장

   나) Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄

   다) Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않게끔 많은 도움을 줌

10. 쿠키와 세션 정리!!

    가) 클라이언트가 요청을 보내서 서버로부터 쿠키를 받는다

    나) 받은 쿠키를 브라우저에 저장한다.

    다) 서버를 재요청시 브라우저에 저장해두었던 쿠키를 요청과 함께 매번 보낸다. (장바구니, 깃랩 로그인)

바. Authentication in Web requests(요청에 대한 인증)

1. Form과 ModelForm : 사용자의 입력을 받을 때 방어수단
2. ArticleForm을 만들었지..
3. 인증은 우리가 직접 구현하기 어려움.. 장고는 built-in forms들을 제공(로그인, 가입, 변경) 장고에 있는 걸 쓸거임. 어제보다 더 간단할 수도? import 해오는 거 외우기!! (공식문서 보면서)

사. 로그인 : “session”을 create하는 과정 (user를 create 하는 건 회원가입)

1. 로그인을 하려면 테스트할 계정이 필요해서 admin을 만들었음.(회원가입이 없기 때문에)

2. AuthenticationForm : 로그인을 위한 built-in form, 로그인 하고자 하는 사용자로부터 정보를 입력받아 데이터가 유효한지 검증, request를 첫번째 인자로 취함!!

3. login(request, user, backend=None) 이것도 request를 첫번째 인자로 취함!!

   가) 인증된 사용자를 로그인시키는 로직으로 view함수에서 사용됨

   나) 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용

   다) HttpRequest 객체와 User 객체가 필요

   라) view함수 login과의 충돌을 방지하기 위해 import한 login 함수 이름을 auth_login으로 변경해서 사용

4. get_user()

   가) AuthenticationForm의 인스턴스 메서드

   나) 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환

5. 로그인 후 개발자 도구와 DB에서 Django로부터 발급받은 세션 확인

   가) DB는 django_session 테이블에서 확인

   나) 개발자도구 - Application - Cookies

6. 현재 로그인 되어있는 유저 정보 출력

   가) 템플릿에서 인증 관련 데이터를 출력하는 방법

     1)어떻게 base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있을까? => settings.py의 context processors 설정값 때문

     2)context processors

      * 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록

      * 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨

      * 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것

      * 현재 user 변수를 담당하는 프로세서는 django.contrib.auth.context_processors.auth

        ```python
        def auth(request):
        
            return {
                "user" : user,
            }
        ```

     3)현재 로그인한 사용자를 나타내는 User 클래스의 인스턴스가 템플릿 변수 {{ user }}에 저장됨

       * 인증이 되었으면 user, 인증이 안 되었으면 AnonymousUser로 출력됨

아. 로그아웃 : “session”을 delete하는 과정 (user를 delete 하는 건 회원탈퇴)

1. 세션은 두 곳에 있음 (클라이언트, 서버) → 양쪽다 지움

2. logout 함수를 따로 지원해줌 (인자는 request만 있음, 반환값 없음)

   가) 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

   나) 2가지 일 처리

     1)현재요청에 대한 세션 데이터를 DB에서 삭제

     2)클라이언트의 쿠키에서도 세션 아이디를 삭제

     3)양쪽에서 모두 다 지우는 이유(클라이언트에서도 지움) : 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 엑세스하는 것을 방지하기 위함

자. 회원가입

1. User를 Create하는 것

2. UserCreationForm : 권한이 없는 새 유저를 생성하는 ModelForm (유저모델에 저장이 되어야하기에 모델폼)

   가) 3개의 필드

     1)username

     2)password1

     3)password2

     2)와 3)을 비교 후 일치하면 ok

3. Custom user & Built-in auth forms

   가) AbstractBaseUser의 모든 subclass와 호환되는 forms

     1)아래 Form 클래스는 User 모델을 대체하더라도 커스텀하지 않아도 사용 가능

       * AuthenticationForm
       * SetPasswordForm
       * PasswordChangeForm
       * AdminPasswordChangeForm

     2)기존 User 모델을 참조하는 Form이 아니기 때문

   나) 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms : 유저를 바꾸더라도 모델폼 안에 있는 유저는 바뀌지 않음. 바꿔줘야 함.

     1)UserCreationForm

     2)UserChangeForm

     3)두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함

   다) get_user_model()

     1)"현재 프로젝트에서 활성화된 사용자 모델(active user model)"을 반환

     2)직접 참조하지 않는 이유 : 예를 들어 기존 User 모델이 아닌 User 모델을 커스텀한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문?

     3)Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조하고 있음

   라) UserCreationForm의 save 메서드 : user를 반환하는 것을 확인

차. 회원탈퇴

1. User를 Delete하는 것

카. 회원정보수정

1. User를 Update하는 것

2. UserChangeForm : 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스(admin 페이지)에서 사용되는 ModelForm

   가) 모델폼이기 때문에 instance 인자로 기존 유저 데이터 정보를 받는 구조 또한 동일함.

   나) CustomUserChangeForm 사용하기

타. 비밀번호변경

1. PasswordChangeForm : 사용자가 비밀번호를 변경할 수 있도록 하는 Form
2. 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
3. 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스?

파. Limiting access to logged-in users

1. 로그인 사용자에 대한 접근 제한하기(2가지 방법)

   가) is_authenticated : User model의 속성 중 하나, 사용자가 인증 되었는지 여부를 알 수 있는 방법

     1)request.user.is_authenticated

     2)로그인이면 True, anonymousUser면 False

     3)권한과는 관련 없으며, 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음. 그냥 로그인이냐 비로그인이냐만 판단함.

   나) login_required : decorator
