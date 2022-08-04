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

4. cf) HTML과 CSS는 각자 문법을 갖는 별개의 언어

   cf) 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다. reset css가 있기 때문에

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
   * 소스 < pseudo-element, 요소 < pseudo-class, 속성, class < id < 인라인(태그 안에 지정) < !important(거의 절대자)
   
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

3. CSS 상속 - MDN에서 확인 가능

   가) CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속

     1)속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.

     2)상속되는 것 예시

       * Text 관련 요소(font, color, text-align), opacity(투명도), visibility(hidden) 등

     3)상속 되지 않는 것 예시

   * Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등

   ```html
   <body>
       <p>안녕하세요! <span>테스트</span> 입니다.</p>
   </body>
   
   <style>
     p {
       /* 상속됨 */
       color: red;
       /* 상속 안됨 */
       border: 3px solid black;
     }
     span{      
     }
   </style>
   ```

다. CSS 기본 스타일

1. 크기 단위

   가) px(픽셀)

     1)모니터 해상도의 한 화소인 '픽셀' 기준

     2)픽셀의 크기는 변하지 않기 때문에 고정적인 단위

   나) %

     1)백분율 단위

     2)가변적인 레이아웃에서 자주 사용

     3)같은 디바이스일 때!

   다) em

     1)(바로 위, 부모 요소에 대한) 상속의 영향을 받음

     2)배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

   라)rem

     1)(바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음

     2)최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

   ```html
   <body>
       <ul class="font-big">
           <li class="em">2em</li> <!--부모가 36이니깐 곱하기 2하면 72-->
           <li class="rem">2rem</li> <!--기본이 16이니깐 곱하기 2하면 32-->
           <li>no class</li> <!--부모 요소 그대로 상속받아서 36-->
       </ul>
   </body>
   
   <style>
     .font-big {
       font-size: 36px;      
     }
     .em { /* 자식태그에 em을 사용하면 바로 위 부모요소를 기준으로 상대적인 사이즈를 가짐 */
       font-size: 2em;
     }
     .rem { /* 최상위 요소(html)의 사이즈를 기준으로 상대적인 사이즈를 가짐 */
       font-size: 2rem;      
     }
   </style>
   ```

2. 크기 단위(viewport)

   가) 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)

   나) '디바이스'의 viewport를 기준으로 상대적인 사이즈가 결정됨

   다) vw(width), vh(height), vmin, vmax => 반응형!!

   ```html
   <body>
     <h1 class="px">px사용</h1>
     <h1 class="vw">vw사용</h1>
   </body>
   
   <style>
     h1 {
       color: black;
       backgroud-color: pink; /* 이 두가지는 상속됨 */
     }
     .px { /* 브라우저의 크기를 변경해도 그대로 */
       width: 200px;      
     }
     .vw { /* 브라우저의 크기에 따라 크기가 변함 */
       width: 50vw;      
     }
   </style>
   ```

3. 색상 단위

   가) 색상 키워드(: red;)

     1)대소문자를 구분하지 않음

     2)red, blue, black과 같은 특정 색을 직접 글자로 나타냄

   나) RGB 색상(: rgb(0, 255, 0);)

     1)16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식

     2)'#' + 16진수 표기법

     3)rgb() 함수형 표기법

   다) HSL 색상(: hsl(0, 100%, 50%);)

     1)색상, 채도, 명도를 통해 특정 색을 표현하는 방식

   라) a는 alpha(투명도)

   ```html
   p {color: black;}
   p {color: #000;}
   p {color: #000000;}
   p {color: rgb(0, 0, 0);}
   p {color: hsl(120, 100%, 0);}
   
   p {color: rgba(0, 0, 0, 0.5);}
   p {color: hsla(120, 100#, 0.5);} <!-- 모두 black! -->
   ```

4. CSS 문서 표현

   가) 텍스트

     1)font-family(폰트), font-style, font-weight(굵기)

     2)letter-spacing(자간), word-spacing(단어 간격), line-height(행간)

   나) 컬러(color), 배경(background-color, background-image)

   다) 기타 HTML 태그별 스타일링

     1)li(목록), table(표)

라. Selectors 심화

1. 결합자

   가) 자손 결합자(공백) : selector A 하위의 모든 selector B 요소

   ```html
   <style>
     div span {
       color: red;      
     }
   </style>
   
   <div>
     <span>이건 빨강입니다.</span>
     <p>이건 빨강이 아니다.</p>
     <p>
       <span>이건 빨강입니다.</span>
     </p>
   </div>
   ```

   나) 자식 결합자(>) : selector A 바로 아래의 selector B 요소

   ```html
   <style>
     div > span {
       color: red;      
     }
   </style>
   
   <div>
     <span>이건 빨강입니다.</span>
     <p>이건 빨강이 아니다.</p>
     <p>
       <span>이건 빨강이 아니다.</span>
     </p>
   </div>
   ```

   다) 일반 형제 결합자(~) : selector A의 형제 요소 중 뒤에 위치하는 selector B 요소를 모두 선택

   ```html
   <style>
     p ~ span {
       color: red;      
     }
   </style>
   
   <span>이건 빨강이 아니다. p태그 앞에 있기 때문에</span>
   <p>문단 있음</p>
   <b>그리고 코드도 있음</b>
   <span>이건 빨강입니다.</span>
   <b>코드있음</b>
   <span>이건 빨강입니다.</span>
   ```

   라) 인접 형제 결함자(+) : selector A의 형제 요소 중 바로 뒤에 위치하는 selector B 요소를 선택

   ```html
   <style>
     p + span {
       color: red;      
     }
   </style>
   
   <span>이건 빨강이 아니다. p태그 앞에 있기 때문에</span>
   <p>문단 있음</p>
   <span>이건 빨강입니다.</span>
   <b>코드있음</b>
   <span>이건 빨강이 아니다. p태그와 인접한 형제가 아니기 때문</span>
   ```

   ```html
   	#ssap > p:nth-child(2) {
   		color: red;
   	}
   n번째 자식이 p 태그(해당 태그)가 아니면 적용시키지 않음, p 태그(해당 태그)면 적용
   
   	#ssap > p:nth-of-type(2) {
   		color: blue;
   	}
   p 태그(해당 태그)만의 순서를 세고 n번째 자식을 바꿈(어떤 태그가 중간에 끼어도 상관없음)
   ```

마.  CSS Box model 

1. 원칙 : 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치) (아랍어는 오른쪽에서 왼쪽으로)

2. 가로 : Inline Direction, 세로 : Block Direction => Normal Flow

3. Box model

   가) 모든 HTML 요소는 box 형태로 되어 있음

   나) 하나의 박스는 네 부분(영역)으로 이루어짐

     1)margin : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다.

     2)border : 테두리 영역, 피부

     3)padding : 내용과 테두리 사이 공간, 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용, 살

     4)content : 글이나 이미지 등 요소의 실제 내용, 뼈

   다) margin

   ```html
   .margin {
     margin-top: 10px;
     margin-right: 20px;
     margin-bottom: 30px;
     margin-left: 40px;
   }
   
   <!--shorthand를 통해서 표현 가능-->
   .margin-1 {
     margin: 10px; <!--상하좌우-->
   }
   
   .margin-2 {
     margin: 10px 20px; <!--상하/좌우-->
   }
   
   .margin-3 {
     margin: 10px 20px 30px; <!--상/좌우/하-->
   }
   
   .margin-4 {
     margin: 10px 20px 30px 40px; <!--12시/3시/6시/9시-->
   }
   ```

   라) padding

   ```html
   .margin-padding {
     margin: 10px;
     padding: 30px;
   }
   ```

   마) border

   ```html
   .border {
     border-width: 2px;
     border-style: dashed;
     border-color: black;
   }
   
   <!--shorthand를 통해서 표현 가능-->
   .border {
     border: 2px dashed black;
   }
   ```

   바) 실습

   ```html
   <body>
       <div class="box1">div</div>
       <div class="box2">div</div>
   </body>
   
   <style>
     .box1 {
       width: 500px;
       border-width: 2px;
       border-color: black;
       border-style: dashed;
       padding-left: 50px;
       margin-bottom: 30px; <!--선 바깥에 여백-->
     }
       
     .box2 {
       width: 500px;
       border: 2px solid black;
       padding: 20px 30px;
     }
   </style>
   ```

   ```html
   <body>
       <div class="box">content-box</div>
       <div class="box box-sizing">border-box</div>
   </body>
   
   <style>
     .box {
       width: 100px;
       margin: 10px auto;
       padding: 20px;
       border: 1px solid black;
       color: white;
       text-align: center;
       background-color: blueviolet;
     } /* 보라색의 넓이는 100 + 20*2 + 1*2 = 142px (width + padding*2 + border*2) */
       
     .box-sizing {
       box-sizing: border-box;
       margin-top: 50px;
     } /* 내가 원하는 너비 100px! */
   </style>
   
   기본적으로 모든 요소의 box-sizing은 'content-box'
     Padding을 제외한 순수 contents영역만을 box로 지정
   다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
     그 경우 box-sizing을 'border-box'로 설정
   ```

바. CSS Display

1. 원칙 : 모든 요소는 네모(박스모델)이고, 좌측상단에 배치, display에 따라 크기와 배치가 달라진다.

2. 인라인 / 블록 요소

   가) 인라인 : text만 공간 차지, 기본너비는 컨텐츠 영역만큼

   나) 블록 : 그 줄 모두 공간 차지, 기본너비는 가질 수 있는 너비의 100%, 너비를 가질 수 없다면 자동으로 부여되는 margin

3. 대표적으로 활용되는 display

   가) display: block

     1)줄 바꿈이 일어나는 요소, 테트리스처럼 한 줄 다 차지하면서 쌓인다.

     2)화면 크기 전체의 가로 폭을 차지한다.

     3)블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.

   나) display: inline

     1)줄 바꿈이 일어나지 않는 행의 일부 요소, 글자처럼 취급

     2)content 너비만큼 가로 폭을 차지한다.

     3)width, height, margin-top, margin-bottom을 지정할 수 없다.

     4)상하 여백은 line-height로 지정한다.

   다) display: inline-block

     1)block과 inline 레벨 요소의 특징을 모두 가짐

     2)inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

   라) display: ***none***

     1)해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

     2)이와 비슷한 visibility: ***hidden***은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다. 처음에 숨겼다가 나중에 보여줄 일 있을 때 사용

   cf) 이외 다양한 display 속성은 https://developer.mozila.org/ko/docs/Web/CSS/display

4. 블록 레벨 요소와 인라인 레벨 요소

   가) 블록 레벨 요소와 인라인 레벨 요소 구분

   나) 대표적인 블록 레벨 요소

     1)div / ul, ol, li / p / hr / form 등

   다) 대표적인 인라인 레벨 요소

     1)span / a / img / input, label / b, em, i, strong 등

5. 속성에 따른 수평 정렬

   가) 왼쪽정렬 :   margin-right: auto; (오른쪽을 여백으로 채움)     text-align: left;

   나) 오른쪽정렬 :   margin-left: auto;     text-align: right;

   다) 가운데정렬 :   margin-right: auto;     text-align: center;

   ​                               margin-left: auto;

   ```html
   <body>
       <h1>나는 block입니다.</h1>
       <div>block</div>
       <p>나는 <span>인라인</span> 속성입니다.</p>
       <hr>
       <h2>display none vs visibility hidden</h2>
       <div>1</div>
       <div class="none">2</div>
       <div class="hidden">3</div>
       <div>4</div>
   </body>
   
   <style>
     div {
       width: 100px;
       height: 100px;
       border: 2px solid black;
       background-color: crimson;
     }
       
     .none {
       display: none; /* 공간도 부여되지 않음 */
     }
       
     .hidden {
       visibility: hidden;      
     }
   </style>
   ```

사. CSS Position

1. CSS position

   가) 문서 상에서 요소의 위치를 지정

   나) static : 모든 태그의 기본 값(기준 위치)

     1)일반적인 요소의 배치 순서에 따름(좌측 상단)

     2)부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

     ```html
     div {
       height: 100px;
       width: 100px;
       background-color: #9775fa;
       color: black;
       line-height: 100px;
       text-align: center;
     }
     ```

   다) 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능

     1)relative : 상대 위치

      * 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)

      * 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(기존 위치(normal position) 대비 offset)

        ```html
        .relative {
          position: relative;
          top: 100px;
          left: 100px;
        }
        ```

     2)absolute : 절대 위치

      * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남), 공중으로 뜬다고 생각하면 편함, 스크롤 오르내릴 때 몸이 없어져

      * static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동) => 나중에 배울 flex를 쓰자!

        ```html
        .parent {
          position: relative;
        }
        
        .absolute-child { <!--static이 아닌 친구를 찾는다. 부모가 relative인 친구를 만난다.-->
          position: absolute;
          top : 50px;
          left : 50px;
        }
        ```

     3)fixed : 고정 위치

      * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남), 공중으로 붕 떠서 항상 고정 위치에

      * 부모 요소와 관계없이 viewport를 기준으로 이동

        * 스크롤 시에도 항상 같은 곳에 위치함

        ```html
        .fixed {
          position: fixed;
          bottom: 0;
          right: 0;
        }
        ```

     4)sticky : 스크롤에 따라 static -> fixed로 변경, 스크롤 따라서 내려옴, 광고 같은 거, 몸은 위에 있다.

       * 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

   라) absolute vs relative

   ```html
   <style>
   /* 공통 스타일링*/
     div {
       box-sizing: border-box;
       width: 100px;
       height: 100px;
       border: 1px solid black;
     }
       
     .parent{
       position: relative;
       width: 300px
       height: 300px
     }
   </style>
   
   Q 
   1,1   1,2   1,3
   
   2,1   2,2   2,3
   
   3,1   3,2   3,3
   
   1,1에 형이 있고 2,1에 동생이 있을 때
   형에게 top: 100px;을 적용했을 때 absolute와 relative의 차이는?
   
   absolute라면 형은 2,2로 동생은 1,1로 간다. 형의 기존 1,1은 없어지기 때문, 동생자리가 있기에 형은 2,1이 아닌 2,2로 가는건가?
   relative라면 형은 2,2로 동생은 2,1 그대로이다. 형의 기존 1,1 없어지는 게 아님.
   ```

   ```html
   <body>
     <div class="parent">
       <div class="absolute">형</div>
       <div class="sibling">동생</div>
     </div>
     <div class="parent">
       <div class="relative">형</div>
       <div class="sibling">동생</div>
   </body>
       
   <style>
     /*공통 스타일링*/
     div {
       box-sizing: brother-box;      
       width: 100px;
       height: 100px;
       border: 1px solid black;
     }
       
     .parent {
       position: relative;
       width: 300px
       height: 300px
     }    
   </style>
       
   <style>
     /*차이점 확인해보기*/ 
     .absolute {
       position: absolute;
       top: 100px;
       left: 100px;
       background-color: crimson;
     }
       
     .sibling {
       background-color: deepskyblue;      
     }
       
     .relative {
       position: relative;
       top: 100px;
       left: 100px;
       background-color: crimson;
     }
   </style>
   ```


+연습문제

```html
<img src="사진 주소(절대주소, 상대주소)" alt="사진 안 나올 시 어떤 문구 나오게 할건지">
cf) 절대주소 : C:/Users/ ~~~ .png
cf) 상대주소 : ../images/ ~~~ .png
../ : 이전
./ : 현재
/ : 루트

<a href="링크할 주소"><img src="사진 주소(절대주소, 상대주소)" alt="사진 안 나올 시 어떤 문구 나오게 할건지"></a>
```

