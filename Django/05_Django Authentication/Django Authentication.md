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

