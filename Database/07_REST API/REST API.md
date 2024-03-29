* REST API
* Response JSON
* Django REST framework - Single Model
* Django REST framework - N:1 Relation



가. HTTP

1. Hyper Text Transfer Protocol

2. HTML 문서와 같은 리소스(자원, 리소스)들을 가져올 수 있도록 하는 프로토콜(규칙)

3. 웹 상에서 컨텐츠를 전송하기 위한 약속

4. 웹에서 이루어지는 모든 데이터 교환의 기초가 됨

5. “클라이언트-서버 프로토콜”이라고도 부름

6. 요청(request), 응답(reponse)

7. HTTP 특징

   가) Stateless(무상태) (쿠키와 세션에서 진행했었음)

   * 동일한 연결에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
   * 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
   * 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함

8. HTTP Request Methods : 요청 시에 서버에 요구

   가) 리소스에 대한 행위(수행하고자 하는 동작)를 정의

   나) 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의

   다) HTTP Method 예시

   * GET, POST, PUT, DELETE
   *   R        C       U         D

   cf) 리소스 : HTTP 요청의 대상을 리소스(자원)라고 함

   라) 대표 HTTP Request Methods

   * GET : 서버에 리소스의 표현을 요청, 검색에만 요청해야 함
   * POST : 데이터를 지정된 리소스에 제출, 서버의 상태를 변경
   * PUT : 요청한 주소의 리소스를 수정
   * DELETE : 지정된 리소스를 삭제

9. HTTP response status codes : 응답 시 완료 상태 여부 나타냄

   가) Informational responses 100

   나) Successful reponses 200

   다) Redirection messages (redirect할 때 호출됨) 300

   라) Client error responses 404, 403

   마) Server error responses 500

   => 요청에 행동의 정의가 되어 있다면 응답에는 상태가 정의되어 있다.

나. 웹에서의 리소스 식별

1. HTTP 요청의 대상을 리소스라고 함

2. 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음

3. 각 리소스는 식별을 위해 UR’I’로 식별됨

4. URI : 통합 자원 식별자, Uniform Resource Identifier

   가) 인터넷에서 하나의 리소스를 가리키는 ‘문자열’

   나) URI에는 두 가지가 있음

   다) 가장 일반적인 URI는 웹 주소로 알려진 ‘URL’(경로)

   라) 특정한 이름으로 리소스를 식별하는 URI는 URN(이름) (중요치 않음)

5. URL : 통합 자원 ‘위치’,  Uniform Resource Locator

   가) 웹에서 주어진 리소스의 주소

   나) 특정 리소스가 어디 있는지(주소)를 알려주기 위한 약속

   다) URL 구조

   * Scheme(or protocol)
     * 브라우저가 리소스를 요청하는데 사용해야 하는 프로토콜
     * http(s) 말고도 mailto: ftp: 이런게 있음
   * Authority
     * :// 로 구분 후 작성시작
     * domain과 port가 콜론으로 구분됨
       * Domain Name
         * 요청중인 웹 서버를 나타냄
         * IP 주소를 사용하는 것도 가능(근데 외우기 어렵잖아 이름을 붙이는게 Domain Name)
       * Port 
         * 리소스에 접근하는데 사용되는 기술적인 문
         * HTTP - 80 / HTTPS - 443
         * 이건 “생략 가능” (나머지는 생략 불가능)
         * 장고의 경우 80+00으로 기본 포트로 설정되어 있음
   * Path
     * 리소스 경로
     * 초기에는 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현
     * 예를 들어 /articles/create/가 실제 articles 폴더 안에 create 폴더 안을 나타내는 것은 아님
   * Parameters (GET 방식)
     * 웹 서버에 제공하는 추가적인 데이터
     * 파라미터는 ‘&’ 기호로 구분되는 키밸류 쌍 목록
     * 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
   * Anchor
     * 리소스의 다른 부분에 대한 앵커
     * 북마크
     * 같은 문서 안의 특정 위치로 이동시켜주는 것
     * “서버에 전송되지 않음” 
     * 브라우저에 필요한거임
     * 하이퍼링크와 비슷한 기능을 하는 인터넷상의 다른 문서와 연결된 문자 혹은 그림

   cf) URN : 통합 자원 이름

   * URL과 달리 자원의 위치에 영향을 받지 않는다.
   * URL의 단점을 극복하기 이해 등장했으며 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원을 식별
   * 하지만 이름만으로 실제 리소스를 찾는 방법은 보편화 되어 있지 않아 현재는 URL을 대부분 사용

6. 웹에서의 리소스 식별

   가) 자원의 식별자(URI)

   * 자원의 “위치”로 자원을 식별  ⇒ URL
   * 고유한 이름으로 자원을 식별  ⇒ URN

다. REST API

1. API

   가) 애플리케이션과 프로그래밍(프로그래밍 언어)으로 소통하는 방법

   나) API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음

   다) API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공, 프로그래밍 언어로 소통 

   cf) GUI : 그래픽 유저 인터페이스 (드래그 하는 것) / CLI : 명령어로 소통하는것 (깃배쉬)

2. Web API

   가) 웹 서버 또는 웹 브라우저를 위한 API

   나) 요즘은 Open API를 활용하는 추세 (개발자라면 누구나 사용할 수 있도록 공개된 API)

   다) API은 다양한 타입의 데이터를 응답 (HTML, XML, “JSON” 등)

3. REST : 무언가를 표현하는 건데

   가) API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

   나) 규약은 아닌데 

   다) 소프트웨어 아키텍쳐 디자인 제약 모음

   라) REST 원리를 따르는 시스템을 RESTful하다고 부름

   마) REST 기본 아이디어는 리소스 즉 자원

   * “자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술”

4. REST에서 자원을 정의하고 주소를 지정하는 방법

   가) 자원의 식별 : URI

   나) 자원의 행위 : HTTP Method 

   다) 자원의 표현 : JSON으로 표현된 데이터 제공, 자원과 행위를 통해 궁극적으로 표현되는 결과물

5. JSON 

   가) 자바 스크립트의 표기법을 따른 단순 문자열

   나) 파이썬의 딕셔너리, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는  키-밸류 형태의 구조를 갖고 있음

   다) 사람이 읽고 쓰기 쉽고 기계가 해석하고 만들어내기 쉽다.

   라) 현재 API에서 가장 많이 사용하는 데이터 타입

6. REST 정리

   가) 자원을 정의하고 자원에 대한 주소를 지정하는 방법의 모음

   * 자원을 식별 - URI
   * 자원에 대한 행위 - HTTP Methods
   * 자원을 표현 - JSON

라. Response JSON : JSON 형태로의 서버 응답 변화

1. 지금까지는 페이지(html)를 응답하는 서버

2. 하지만 사실 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음

3. 이제는 JSON 데이터를 응답하는 서버로의 변환

4. 그렇다면 사용자에게 보여질 화면은 누가 구성하는가?

5. 장고로부터 JSON데이터를 받아서 프로트엔드 프레임워크(Vue.js)가 담당할 예정

6. 더 이상 장고는 템플릿 부분에 대한 역할을 담당하지 않게 되며 프론트엔드와 백엔드가 분리되어 구성되게 됨

7. 장고 : 파이썬 (데이터(json)를 주는 서버로서 탈바꿈!)

   Vue.js : 자바스크립트

