#### Web

* 웹 사이트의 구성 요소
* 웹 표준과 크로스 브라우징
* 개발 환경 설정

#### HTML

* HTML 기본구조
* HTML 문서 구조화



가. Web

1. 웹 사이트의 구성 요소

   가) 웹 사이트란 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음

   나) 링크들이 있음, 웹 페이지(문서)를 연결한 것을 웹 사이트라고 함.

   다) 구성 요소 : HTML(구조), CSS(표현), Javascript(동작)

   ​                              건물          인테리어   엘베(IOT home)

   라) 웹사이트는 브라우저를 통해 동작함.

     ex) 브라우저 목록 : 크롬, 네이버웨일, edge, 파이어폭스

   HTML 문서            .hwp .doc 파일           파일들 실행됨

    브라우저           MSword, 한컴문서          이 기반에서

   마) 파일도 다른 프로그램에서 깨지는 경우가 있는 것처럼 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화) => 해결책으로 웹 표준(USB)이 등장

   바) 웹 표준

     1)웹에서 표준적으로 사용되는 기술이나 규칙

     2)어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징) -> 어딜가도 똑같이 나온다. (W3C, WHATWG) mozilla재단 아님

     3)브라우저별 호환성 체크 -> Can I Use

나. HTML(구조) : Hyper Text Markup Language

1. Hyper Text란? 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

     ex) 도서관에서 책을 보다가 모르는 걸 다른 책으로 참조하고 있는데.. 또 다른 책은 다른 도시에 있는데요? 왓? 한 곳에서 보고싶다!

2. Markup Language : 태그 등을 이용해서 문서나 데이터의 구조를 명시하는 언어, 그냥 글만 있으면 이해하기가 힘든데 그걸 태그로 명시화해줌

     ex) HTML, Markdown

3. HTML : 웹페이지를 작성(구조화)하기 위한 언어 / .html / HTML파일

4. HTML 스타일 가이드 : 2칸 띄운다. (안 지켜도 문제는 없으나..)

다. HTML 기본구조

1. HTML 기본구조

   가) html : 문서의 최상위(root) 요소

   나) head : 상속관계 아니고 html과 같은 선상에 있음, 문서 메타데이터 요소 / 찍은 곳, 시간, 해상도

     1)문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

     2)일반적으로 브라우저에 나타나지 않는 내용

   다) body : 문서 본문 요소

     1)실제 화면 구성과 관련된 내용 / 사진

2. head 예시

   가) <title> : 제목, 브라우저 상단 타이틀, 브라우저 탭에 있는 이름

   나) <meta> : 문서 레벨 메타데이터 요소

   다) <link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)

   라) <script> : 스크립트 요소 (JavaScript 파일/코드)

   마) <style> : CSS 직접 작성

     cf) head 예시 : Open Graph Protocol (유튜브 썸네일)

      * 메타 데이터를 표현하는 새로운 규약
        * HTML 문서의 메타 데이터를 통해 문서의 정보 전달
        * 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

3. HTML 요소 : 태그  + 내용

   가) HTML : 태그를 이용해서 구조를 만들고 브라우저로 실행하는 문서를 의미

   ```html
   <h1>contents</h1>
   시작태그/내용/종료태그
   ```

   나) 내용이 없는 태그들도 존재(닫는 태그가 없음) : br, hr, img, input, link, meta

   다) 요소는 중첩될 수 있음(태그 안에 또 다른 태그가 있을 수도)

     ex) html > head 잘못해서 오타나거나 하나 안 쓸 수도 있지만 오류는 안 남, 깨질 뿐

     ex) a 태그 안에 img 태그 넣을 수 있음. 이미지 누르면 다른 곳으로 넘어가는 것처럼

   라) 개발자 도구(ctrl + shift + i / 우클릭 -> 검사 -> 왼쪽 맨 위)를 통해 요소 선택하여 HTML 구조 탐색 가능 

4. 속성(태그 안에 존재) : 태그 안에 디테일한 정보를 주기 위해 존재

   ```html
   <a href="https://google.com"></a> => 하이퍼링크(HTML이 만들어진 이유!)
      속성명=속성값(이름과 값이 쌍으로 존재)
      공백 안 됨, 쌍따옴표 사용
   ```

   가) 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공

   나) 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

     1)모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)

     2)id : 문서 전체에서 유일한 고유 식별자 지정

     3)class : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)

     4)data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용 / 좋아요! 만들 때 씀

     5)style : inline 스타일

     6)title : 요소에 대한 추가 정보 지정

     7)tabindex : 요소의 탭 순서 / 네이버에서 tab 눌렀을 때 순서가 어떻게 갈지

   ```html
   코드 예시
   head
   body
   주석(ctrl + /) <!-- 주석 -->
   ```

5. 시맨틱 태그 : 의미 있다. 의미를 담아서 씀.(외워야 함!)

   가) HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것

     ex) h1태그는 '이 페이지에서 최상위 제목'인 텍스트를 감싸는 역할을 나타냄

   나) Non semantic 요소로는 div, span 등이 있으며 a, form, table, footer, article, nav, aside 태그들도 시맨틱 태그로 볼 수 있음

   다) 대표적인 시맨틱 태그 목록

     1)header : 문서 전체나 섹션의 헤더(머리말 부분)

     2)nav : 내비게이션

     3)aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠

     4)section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현

     5)article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역

     6)footer : 문서 전체나 섹션의 푸터(마지막 부분)

   라) 시맨틱 태그 안 쓰면 : 무슨의미? / 시맨틱 태그 쓰면 : 아 header 안에 nav가 있군, 의미 쉽게 파악 

   마)시맨틱 태그 사용 이유 

     1)개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현

     2)단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력

     3)요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함

     4)검색 엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

6. 렌더링(Rendering) : 텍스트로 작성된 코드가 어떻게 웹 사이트가 되는 걸까? 렌더링!(웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정!)

   가) DOM(Document Object Model) 트리

     1)텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

      * HTML 문서에 대한 모델을 구성함

      * HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

        ```html
        <body>
            <h1>웹문서</h1>     1번 박스
            <ul>               2번 박스
                <li>HTML</li>
                <li>CSS</li>
            </ul>
        </body>
        ```

라. HTML 문서 구조화

1. 인라인 / 블록 요소

   가) HTML 요소는 크게 인라인 / 블록 요소로 나눔

   나) 인라인 요소는 글자처럼 취급

   다) 블록 요소는 한 줄 모두 사용

   ```html
   <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
   <b></b> : 굵은 글씨 요소, 중요하게 강조하고자 하는 요소
   <strong></strong> : strong은 마크업문서만 봐도 강조하는구나 라는 것을 알 수 있음. 문서를 구조화시키는데 좋은 역할!
   <i></i> : 기울임 글씨 요소, 중요하게 강조하고자 하는 요소
   <em></em>
   <br> : 텍스트 내에 줄 바꿈 생성 (엔터 아님)
   <img> : src 속성을 활용하여 이미지 표현
   <span></span> : 의미 없는 인라인 컨테이너, 무언가를 담을 때, 투명한 쇼핑백같은 존재
   <p></p> : 하나의 문단(paragraph)
   <hr> : 문장 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨(A Horizontal Rule)
   <ol></ol> : 순서가 있는 리스트
   <ul></ul> : 순서가 없는 리스트
   <pre></pre> : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지
   <blockquote></blockquote> : 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
   <div></div> : 의미 없는 블록 레벨 컨테이너
   ```

   ```html
   ! + tap : 기본 탬플릿 불러와짐
   ```

2. form

   가) <form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그, 사용자로부터 데이터를 입력받기 위해 쓰임, 로그인할 때 id, pw 입력할 때 사용(id, pw를 서버에 전송), 사용자가 브라우저를 통해서 서버 컴퓨터에다가 데이터를 전송하는게 form문(장고가서 배움)

   나) <form> 기본 속성

     1)action : form을 처리할 서버의 URL(데이터를 보낼 곳, 예를 들어 네이버나 구글)

     2)method : form을 제출할 때 사용할 HTTP 메서드, 데이터를 전송하기 위한 방법(GET 혹은 POST)

     3)enctype : method가 post인 경우 데이터 유형(암호화?, 파일 전송을 위해 써야한다. 텍스트 보낼 때는 기본값)

   ​    ex) 구글에 파이썬 쳐보고 주소 확인해보면 ?q=파이썬 (get 방식)

3. input

   가) 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨, form(종이) 안에 input(내용) 넣어서 데이터를 받는다

   나) <input> 대표적인 속성

     1)name : form control에 적용되는 이름(이름/값 페어로 전송됨)

     2)value : form control에 적용되는 값(이름/값 페어로 전송됨)

     3)required, disabled 등

     ```html
     <input type="text" name="q"> HTML 검색하고 주소 확인하면 ?q=HTML
     ```

4. input label : 이름을 쓰는 형식, input 태그에 대한 상세한 설명, input은 컨텐츠가 없기 때문에

   가) <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴

   ```html
   <label for=”agreement”></label>
   <input id=”agreement”> id는 태그의 스페셜한 별명이라고 보면 됨
   ```

   나) 아이디 _______________

   ​       Label   input

   ​        for        id

   ```html
   아이디 label 아이디를 눌러도 input에 입력가능하게끔..
   줄바꾸기 위해 div
   disabled 입력 안되게 함
   type="checkbox"
   ```

5. input 유형 - 일반

   가) text : 일반 텍스트 입력

   나) password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현

   다) email : 이메일 형식이 아닌 경우 form 제출 불가

   라) number : min, max, step 속성을 활용하여 숫자 범위 설정 가능

   마) file : accept 속성을 활용하여 파일 타입 지정 가능

6. input 유형 - 항목 중 선택

   가) 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함

   나) 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함

     1)checkbox : 다중 선택, for와 id 연결

     2)radio : 단일 선택

7. input 유형 - 기타

   가) 다양한 종류의 input을 위한 picker를 제공

     1)color : color picker

     2)date : date picker

   나) hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정

     1)hidden : 사용자에게 보이지 않는 input

8. 마크업 실습

   가) header

   ```html
   <!--a 태그 안에 img 태그-->
   <header>
       <a href="<!--연결한 URL 주소-->">
           <img src="<!--이미지 주소-->" alt="<!--이미지 깨졌을 때 대체-->">
       </a>
   </header>
   ```

   나) section

   ```html
   <section>
       <form action="#">
   		<div>
           	<label for="name">이름을 기재해주세요.</label><br>
   			<input type="text" id="name" name="name" autofocus>
   			<!--for와 id 연결-->
       	</div>
           <div>
           	<label for="region">지역을 선택해주세요.</label><br>
               <select name="region" id="region" required>
                   <option value="">선택</option>
                   <option value="서울">서울</option>
                   <option value="대전">대전</option>
                   <option value="광주">광주</option>
                   <option value="강원" disabled>강원</option>
               </select>
           </div>
   		<!--required는 필수, option 선택할 수 있게-->
   		<div>
               <p>체온을 선택해주세요.</p>
               <input type="radio" ... checked> <!--기본 check되어 있음-->
           </div>
   	<input type="submit" value="제출">
       </form>
   </section>
   ```

   다) footer

   ```html
   <footer>
       맨 아래입니다.
   </footer>
   ```


+EXTRA

```html
# 표(table) 만들기 tr : 행만들기, td : 열만들기, th : 헤드만들기
<table>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
```

