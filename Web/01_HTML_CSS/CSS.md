#### CSS

* CSS Selectors
* CSS 단위
* Selectors 심화
* Box model
* Display
* Position



가. CSS(Cascading Style Sheets) : 스타일을 지정하기 위한 언어, 선택(HTML 태그를 선택)하고 스타일을 지정한다. 계단식(약간 상속 느낌?)

1. CSS 구문

   ```html
   h1 {
     color: blue;
     font-size: 15px; <!--콜론과 세미콜론-->
   }
   ```

   가) h1 : 선택자(Selector)

   나) color: blue; : 선언(Declaration)

   다) font-size : 속성(Property), 어떤 스타일 기능을 변경할지 결정

   라) 15px : 값(Value), 어떻게 스타일 기능을 변경할지 결정

2. CSS 정의 방법

   가) 인라인 - 태그에다가 바로 style을 넣어서 적용, 실수 많음(중복도 있을 것이고 찾기도 어려워서)

   ```html
   <h1 style="color: blue; font-size: 100px;">Hello</h1>
   ```

   나) 내부 참조 - <head> 태그 내 <style> 지정, 코드가 너무 길어짐

   ```html
   <style>
       h1 {
           color: blue;
           font-size: 100px;
       }
   </style>
   ```

   다) 외부 참고 - 외부 CSS 파일을 <head> 내 <link>를 통해 불러오기, 가장 좋음!!

   ```html
   mystyle.css 내부
   h1 {
   	color: blue;
   	font-size: 20px;
   }
   
   index.html <head> 내부
   <link rel="stylesheet" href="mystyle.css">
   ```

   ```html
   ! + tab : 기본구조 완성
   ctrl + b : 목록 열고 숨기기
   h1*5 : 5개 만들어짐
   shift alt 화살표 아래 : 커서 여러 개 만들어져서 같이 쓸 수 있음
   ```

3. CSS 개발자 도구(F12)

   가) styles : 해당 요소에 선언된 모든 CSS

   나) computed : 해당 요소에 최종 계산된 CSS

나. CSS Selectors(선택자)

1. 선택자 유형

   가) 기본 선택자 : 전체 선택자, 요소 선택자, 클래스 선택자, 아이디 선택자, 속성 선택자

   나) 결합자 : 자손 결합자, 자식 결합자, 일반 형제 결합자, 인접 형제 결합자

   다) 의사 클래스/요소

2. 기본 선택자 : 여러 개 고를 수도 있음. 선택자: 데이터

   ```html
   <style>
     /* 전체 선택자 */
     * {             /* *는 모두 선택 */
       color: red;
     }
       
     /* 요소선택자, 태그선택자 */
     h2 {            /* HTML 태그를 직접 선택 */
       color: orange;
     }
       
     h3,
     h4 {
       font-size= 10px;  
     }
   
     /* 클래스 선택자 */
     .green {        /* 마침표(.) 문자로 시작, class="" 로 지정하고 쓸때는 .(클래스이름) */
       color: green;    
     }
       
     /* id 선택자 */
     #purple {       /* # 문자로 시작, #(ID이름) 로 쓰임 */
       color: purple;    
     }
   </style>
   
   요소 -> 서울사람
   클래스 -> (성)최씨, 정씨
   아이디 -> (이름)길동
   범위가 점점 좁아짐 -> 파워가 쎔(계단식)
   * < pseudo-element, 요소 < pseudo-class, 속성, class < id < 인라인(태그 안에 지정) < !important(거의 절대자)
   
   lorem + tab : 아무글자 있어보이게 나옴
   ```

   ```html
   <!--Quiz-->
   h2 {
     color: darkviolet !important;
   }
   
   p {
     color: orange;
   }
   
   .blue {
     color: blue;
   }
   
   .green{
     color: green;
   }
   
   #red{
     color: red;
   }
   
   <p>1</p> 오렌지
   <p class="blue">2</p> 블루
   <p class="blue green">3</p> 그린
   <p class="green blue">4</p> 그린(위에 적는 순서에서 나중에 나온 애가 이김)
   <p id="red" class="blue">5</p> 레드
   <h2 id="red" class="blue">6</h2> 다크바이올렛(!important가 있기 때문에, 그러나 꼬이기 쉬워서 잘 안 씀)
   <p id="red" class="blue" style="color: yellow;">7</p> 옐로우(인라인)
   <h2 id="red" class="blue" style="color: yellow;">8</h2> 다크바이올렛
   ```

   