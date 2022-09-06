* Django Form
* Django ModelForm
* Handling HTTP requests
* View decorators



가. Django Form

1. 현재는 HTML form, input 태그를 통해서 사용자로부터 데이터 받았음

2. 요청을 모두 수용하다보면 비정상, 악의적 요청이 있을 수 있음 ⇒ 유효성 검증 반드시 필요

3. 많은 부가적인 것들이 많아 개발 생산성 늦춤 ⇒ Django Form이라고 하는 class를 이용함으로써 과중한 작업을 보다 더 쉽게 함

4. Django Form : 사용자가 보내는 데이터에 대한 주요 유효성 검사 도구

5. Form에 대한 Django의 역할

   가) Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

   나) Django는 Form과 관련한 유효성 검사를 단순화, 자동화할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.

     1)개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성

6. Django는 Form에 관련된 작업의 세 부분을 처리

   가) 렌더링을 위한 데이터 준비 및 재구성

   나) 데이터에 대한 HTML forms 생성 (.html에서 form 썼던 것처럼)

   다) 클라이언트로부터 받은 데이터 수신 및 처리

7. Form Class 

   가) 클래스 선언(model과 마찬가지로 상속을 통해 선언, forms 라이브러리에 Form 클래스 선언) 후 인스턴스로 부름

나. Django ModelForm

1. Model과 많이 겹치는데?  ⇒ Model 기반으로 한 form을 만들자!(재정의할 필요 없어짐)
2. Model을 통해 Form Class를 만들 수 있는 helper class

다. Handling HTTP requests

1. HTTP requests 처리에 따른 “view 함수 구조 변화”
2. new-create edit-update 하나로 합치자! 하나는 GET방식, 하나는 POST방식

라. View decorators : view 함수를 단단하게 만들기

1. 데코레이터 : 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수

