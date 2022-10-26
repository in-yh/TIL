* DOM
* Event
* this



가. DOM

1. 개요

   가) 브라우저에서의 JavaScript

   * JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어

   * 데이터가 주기적으로 갱신되거나, 사용자와 상호 작용을 하거나, 애니메이션 등이 동작하게 하는 것을 가능하게 함

     cf) 스크립트 언어 : 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

   나) 웹 페이지에서의 JavaScript

   * JavaScript는 프로그래밍 언어로서의 역할도 가능하지만 클라이언트 사이드 JavaScript 언어 위에 올라가있는 기능들은 더 다양함
   * API라고 부르는 이 기능들은 JavaScript코드에서 사용할 수 있는 것들을 더 무궁무진하게 만들어 줌
   * 이 API는 일반적으로 2개의 범주로 분류할 수 있으며 이 다음에는 Brower APIs에 대해 작성하였음.
     * Browser APIs
     * Third party APIs
       * 브라우저에 탑재되지 않은 API
       * 웹에서 직접 코드와 정보를 찾아야 함
       * Google map api, kakao login api 등

2. Browser APIs 

   가) 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함

   나) JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음

   다) 종류

   * DOM
   * Geolocation API : 지리정보
   * WebGL : 그래픽
   * ...

   라) 브라우저가 웹 페이지를 불러오는 과정

   * 웹 페이지를 브라우저로 불러오면, 브라우저는 코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 실행
   * JavaScript는 `DOM API`를 통해 HTML과 CSS를 동적으로 수정, 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰임

3. DOM

   가) 문서 객체 모델(Document Object Model)

   나) 문서의 구조화된 표현을 제공, 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법을 제공

   * 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
   * HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음(문서를 변경, 조작하려면 접근해야하는데.. 이걸 해주는 게 DOM API / HTML, CSS, 자바 스크립트 브라우저(DOM API를 통해서 문서를 DOM적으로 만듦)에서 만들어진 다음에 최종적으로 우리가 보는 화면이 됨)

   다) HTML 문서를 구조화하여 각 요소를 객체(Object)로 취급

   라) 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작이 가능함

   마) DOM은 문서를 논리 트리로 표현 (document > Element : <html> > Element : <head> > Element : <title> > Text: "My title")

   바) DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음

   사) 웹 페이지는 일종의 문서

   아) 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함

   자) DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공

   차) DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

   카) 브라우저가 기본적으로 제공하는 API : DOM (모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용)

   타) 우리는 "DOM의 주요 객체"들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

4. DOM의 주요 객체

   가) window

   * DOM을 표현하는 창(창 전체를 의미하는게 윈도우)

   * 가장 최상위 객체(작성 시 생략 가능)

   * 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄 

     ```markdown
     * 새 탭 열기
     window.open()
     
     * 인쇄 대화 상자 표시
     window.print()
     
     * 경고 대화 상자 표시
     window.alert()
     ```

   나) document

   * window보다는 하위

   * 브라우저가 불러온 웹 페이지

   * 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함하고 있음

     ```markdown
     * 현재 문서의 제목(HTML의 <title> 값)
     document.title 
     '새 탭'
     
     * 제목 수정하기
     document.title = 'JavaScript'
     'JavaScript'
     document 객체에서 title 메서드를 활용해 title 태그를 바꿔준다.
     
     * cf) document는 window의 속성이다.
     document
     #document
     
     window.document (위와 같은 결과)
     #document
     ```

     cf) 파싱(Parsing)

     * 구문 분석, 해석
     * 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
     * PARSE → STYLE → LAYOUT

   다) navigator, location, history, screen 등

5. DOM 조작 (DOM API를 통해서 DOM 조작)

   가) 개요

   * Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
   * DOM 조작 순서!!
     * 선택 
     * 조작
       * 생성, 추가, 삭제 등

   나) 선택 관련 메서드

   * document.querySelectot(selector) : 단일 선택 (중요한 건 객체 하나 찾는다.)
     * 제공한 선택자와 일치하는 element 한 개 선택
     * 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)
   * document.querySelectorAll(selector) : 여러 개 선택
     * 제공한 선택자와 일치하는 “여러 element“를 선택
     * 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
     * 제공할 CSS selector를 만족하는 NodeList를 반환

   다) 조작 관련 메서드(생성)

   * document.createElement(tagName) : 태그를 만드는 거
     * 작성한 tagName의 HTML요소를 생성하여 “반환”

   라) 조작 관련 메서드(입력)

   * Node.innerText : 태그 안에 내용 쓰는 거
     * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text)
     * 사람이 읽을 수 있는 요소만 남김
     * 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨

   마) 조작 관련 메서드(추가)

   * Node.appendChild() : 배치. 누군가의 자식에 넣어줘야 함 왜? 우리는 dom구조로 되어있어서 어딘가의 하위 자식으로 넣어줘야 해. html은 다 그런 구조로 되어 있음.
     * 한 Node를 특정 부모 Node의 자식 NodeList 중 “마지막 자식”으로 삽입
     * 한번에 오직 하나의 Node만 추가할 수 있음
     * 추가된 Node 객체를 “반환”
     * 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

   바) 조작 관련 메서드(제거)

   * Node.removeChild()
     * DOM에서 자식 Node를 제거
     * 제거된 Node를 반환

   사) 조작 관련 메서드(속성 조회 및 설정)

   * Element.getAttribute(attributeName) : 속성 얻을 때
     * 해당 요소의 지정된 값(문자열)을 반환
     * 인자(attributeName)는 값을 얻고자 하는 속성의 이름
   * Element.setAttribute(name, value) : 속성 넣어주는 것(name과 value) 
     * 지정된 요소의 값을 설정
     * 속성이 이미 존재하면 값 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

나. Event

1. 개요

   가) Event란 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 혹은 발생(occurrence)으로, 각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것

   * 버튼을 클릭한다면 클릭에 대해 이벤트가 발생하고 우리는 이벤트를 통해 클릭이라는 사건에 대한 결과를 응답받거나, 조작을 할 수 있음

   나) 클릭 말고도 웹에서는 각양각색의 Event가 존재(키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등)

2. Event object

   가) 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

   나) Event 발생

   * 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
   * 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음

   다) DOM 요소는 Event를 받고(”수신”)

   라) 받은 Event를 “처리”할 수 있음

   * Event 처리는 주로 addEventListener()라는 Event처리기(Event handler)를 다양한 html요소에 "부착"해서 처리함

   마) Event handler - addEventListener()

   ```markdown
   “EventTarget”.addEventListener(”type”, “listener”)
   “대상”에 “특정 Event”가 발생하면, “할 일”을 등록하자
   ```

   * EventTarget.addEventListener(type, listener[, options])
     * 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
     *  Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상(EventTarget)으로 지정 가능
     * type
       * 반응할 Event유형을 나타내는 대소문자 구분 문자열
       * 대표 이벤트 : input, click, submit (mdn 확인)
     * listener
       * 지정된 타입의 Event를 수신할 객체
       * 콜백함수여야함
       * 콜백 함수는 발생한 Event의 데이터를 가진 Event객체를 유일한 매개변수로 받음
   * 정리
     * ~하면 ~한다.
       * 클릭하면, 경고창을 띄운다.
       * 특정 Event가 발생하면, 할 일(콜백 함수)을 등록한다.

   바) Event 취소

   * event.preventDefault()
     * 현재 Event의 기본 동작을 중단
     * HTML 요소의 기본 동작을 작동하지 않게 막음
     * HTML 요소의 기본 동작 예시
       * a 태그 : 클릭 시 특정 주소로 이동
       * form 태그 : form 데이터 전송

다. this (vue.js 할 때 필요)

1. 어떠한 object를 가리키는 키워드 (어딘가를 가리킬 때 필요)

   가) java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)

2. JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음

3. JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작

4. JavaScript는 해당 `함수 호출 방식`에 따라 this에 바인딩 되는 객체가 달라짐

5. 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 `함수가 어떻게 호출 되었는지에 따라 동적으로 결정`됨

6. this INDEX

   가) 전역 문맥에서의 this

   * 브라우저의 전역 객체인 window를 가리킴
     * 전역객체는 모든 객체의 유일한 최상위 객체를 의미
     * console.log(this) // window
   * node.js는 global로 출력

   나) 함수 문맥에서의 this : `함수 호출 방법에 의해 결정`됨

   * 단순 호출

     * 전역 객체를 가리킴

     * 전역은 브라우저에서는 window, Node.js는 global을 의미함

       ```markdown
       const myFunc = function () {
       	console.log(this)
       }
       
       // 브라우저
       myFunc() // window
       
       // Node.js
       myFunc() // global
       ```

   * Method (객체의 메서드로서)

     * 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩

       ```markdown
       const myObj = {
       	data: 1,
       	myFunc() {
       		console.log(this) // myObj
       		console.log(this.data) // 1
       	}
       }
       
       myObj.myFunc() // myObj
       ```

   * Nested

     * Function 키워드

       * forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴

       * 단순 호출 방식으로 사용되었기 때문

       * 이를 해결하기 위해 등장한 함수 표현식이 바로 "화살표 함수"

         ```markdown
         const myObj = {
         	numbers: [1],
         	myFunc() {
         		console.log(this) // myObj
         		this.numbers.forEach(function (number) {
         			console.log(number) // 1
         			console.log(this) // window 가 나옴!
         			// this가 왜 window? 호출 방식에 의해 결정된다. 함수 호출 중 메서드 호출이 아니라 단순 호출은 전역 객체를 가리킴. 아주 단순히 "방식"에 따라서 결정됨 => 이걸 해결하려고 나온게 화살표 함수!
         		})
         	}
         }
         
         myObj.myFunc()
         ```

     * 화살표 함수

       * 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴

       * 화살표 함수에서 this는 자신을 감싼 정적 범위

       * 자동으로 한 단계 상위의 scope의 context를 바인딩

       * 화살표 함수로만 바꿔도 정상적으로 객체를 가리킴, Nested 함수에서 this를 쓴다면 화살표 함수를 써야 함

         ```markdown
         const myObj = {
         	numbers: [1],
         	myFunc() {
         		console.log(this) // myObj
         		this.numbers.forEach((number) => {
         			console.log(number) // 1
         			console.log(this) // myObj
         		})
         	}
         }
         
         myObj.myFunc()
         ```

       * 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴(Lexical scope this)

       * Lexical scope

         * 함수를 어디서 호출하는지가 아니라 `어디에 선언`하였는지에 따라 결정
         * Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식

       * 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장!!!

       * this와 addEventListener

         * 하지만..
         * addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우, addEventListener를 호출한 대상을 (event.target) 뜻함
         * 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨 btn이 
         * 결론 : "addEventListener의 콜백 함수는 function키워드를 사용하기"
         * 시험문제 : this가 가리키는 것은?!

7. this 정리

   가) this가 런타임(호출되는 순간에 결정되는 것)에 결정되면 장점도 있고 단점도 있음

   나) 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있다.

   다) 이런 유연함이 실수로 이어질 수 있다는 것은 단점

   라) this가 좋은지 나쁜지는 우리가 판단할 문제가 아니다.

   마) 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데만 집중하면 됨