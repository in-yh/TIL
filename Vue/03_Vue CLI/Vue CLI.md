* Vue CLI
* SFC
* Pass Props & Emit Events



가. Vue CLI

1. Node.js

   가) 자바스크립트는 브라우저를 조작하는 유일한 언어

   * 하지만 브라우저 밖에서는 구동할 수 없었음

   나) 자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨

   * 크롬 V8 엔진을 제공하여 여러 OS환경에서 실행할 수 있는 환경을 제공
   * 브라우저만 조작 가능했으나, Server-Side-Programming 즉 서버에서도 가능해짐

2. NPM(Node Package Manage)

   가) 자바스크립트 패키지 관리자

   * 파이썬에 pip가 있다면 Node.js에는 npm
   * pip와 마찬가지로 다양한 의존성 패키지를 관리

   나) Node.js의 기본 패키지 관리자로 Node.js 설치 시 함께 설치

3. Vue CLI

   가) Vue CLI

   * Vue 개발을 위한 표준 도구
   * 프로젝트의 구성을 도와주는 역할
   * 확장 플러그인, GUI, Babel 등 다양한 tool 제공

   나) Quick Start

   ```bash
   설치
   $ npm install -g @vue/cli
   
   프로젝트 생성
   	vscode terminal에서 진행!!
   $ vue create vue-cli : vue create '프로젝트 이름'
   	Vue 2 선택(git bash에서는 선택할 수가 없음)
   $ cd vue-cli : vue-cli 폴더가 생성되고 여기 들어가 줘야 함, 프로젝트 디렉토리 이동 (ls : 현재 폴더 확인)
   $ npm run serve : 서버 키기, 프로젝트 실행 (ctrl + c : 서버 끄기)
   	Network : 모바일로 접속 가능
   ```

4. Vue CLI 프로젝트 구조

   가) master로 뜸 → git이 이미 생성 (TIL에는 이 git을 지워줘야 함)

   나) node_modules : node.js 환경의 여러 의존성 모듈, 파이썬에서 venv(가상환경)을 만드는 역할, gitignore에 저장됨(원격 저장소에 저장하지 않음), Vue 프로젝트를 생성하면 자동으로 추가됨

   * Babel 
     * 자바스크립트의 컴파일러 역할
     * 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
     * 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펨트럼이 매우 다양
       * 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
       * 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
       * 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 더 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음
       * arrow function도 바꿔서 사용
   * Webpack : vue cli에 이미 있음 / 수많은 의존성을 가진 모듈을 정적인 것으로 바꿔준다!(.jpg .css .js .png) ⇒ 무겁지만(개발자는 npm install을 사용해 다양한 모듈을 한 번에 설치하고) 각 모듈을 사용해 개발에 집중할 수 있다
     * static module bundler : 내부적으로 사용하는 모든 모듈을 관리
     * 모듈 간의 의존성 문제를 해결하기 위한 도구
     * 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
     * Module
       * 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
       * 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이 때 분리된 파일 각각이 모듈 즉, js 파일 하나가 하나의 모듈
       * 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
       * 여러 모듈 시스템 : ESM, AMD, CommonJS, UMD
       * Module 의존성 문제 : 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
         * Webpack은 이 모듈 간의 의존성 문제를 해결하기 위해 등장
     * Bundler
       * 모듈 의존성 문제를 해결해주는 작업이 Bundling
       * 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나
       * 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
       * Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
       * snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재
       * Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음
     * node_modules의 의존성 깊이
       * NPM의 kik 회수 사건(2016)
       * kik 개발자가 라이브러리 지우면서 코드 11줄 문제.. 바벨 먹통, 바벨을 쓰는 기업들의 모두 프로그램 먹통
       * 그 이후로는 내리는 NPM 절차 따로 생김 (24시간 이내로만 바로 내릴 수 있음)
       * 해결하고자 Node.js 만든 본인이 새로운 런타임 환경을 만듦 (본인이 Node.js를 만들었지만 문제점을 알고 있었으) ⇒ deno(자바스크립트를 구동하는 환경)
   * package.json : 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
   * package-lock.json 
     * node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
     * 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
     * 사용할 패키지의 버전을 고정
     * 개발 과정 간의 의존성 패키지 충돌 방지
     * 파이썬의 requirements.txt 역할을 함
   * public/index.html
     * Vue 앱의 뼈대가 되는 html 파일
     * Vue 앱과 연결될 요소가 있음
     * 여기에 그려나감, div id=”app”이 vue와 연결됨
   * src/
     * src/assets : 정적 파일을 저장하는 디렉토리(장고에서는 static)
     * src/components : 하위 컴포넌트들이 위치
     * src/App.vue : 최상의 컴포넌트, public/index.html과 연결됨
     * src/main.js
       * webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
       * public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
       * Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

나. SFC

1. Component

   가) UI를 독립적이고 재사용 가능한 조각들로 나눈 것

   * 즉, 기능별로 분화한 코드 조각

   나) CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미

   다) 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임

   * Web시간에 배운 HTML 요소들의 중첩을 떠올려 보자!
     * Body tag를 root node로 하는 tree의 구조이다
     * 마찬가지로, Vue에서는 src/App.vue를 root node로 하는 tree의 구조를 가짐

   라) 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공

   마) 우리가 사용하는 웹 서비스도 여러 개의 컴포넌트로 이루어져 있음

   바) 하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리할 수 있음

   사) 

   |          | <Root>      |          |
   | -------- | ----------- | -------- |
   | <Header> | <Main>      | <Aside>  |
   |          | <Article>*2 | <Item>*3 |

   아) 장고에서의 예시

   * 우리는 base.html과 index.html을 분리하여 작성하였지만, 하나의 화면으로 볼 수 있다
     * 즉, 한 화면은 여러 개의 컴포넌트로 이루어질 수 있음
   * base.html을 변경하면 이를 extends하는 모든 화면에 영향을 미침
     * 유지 보수를 쉽게 해줌
   * index.html에서 for문을 통해 여러 게시글들을 하나의 형식에 맞추어서 출력해줌
     * 형식을 재사용하고 있었음
     * 우리는 너무 자연스럽게 컴포넌트 기반으로 개발을 진행하고 있었다!
   * Component based architecture 특징 : 관리가 용이, 재사용성, 확장 가능, 캡슐화, 독립적

2. SFC(Single File Component)

   가) component in Vue

   * 그렇다면 Vue에서 말하는 component란 무엇일까?
     * 이름이 있는 재사용 가능한 Vue instance
   * 그렇다면 Vue instance란?
     * new Vue()로 만든 인스턴스

   나) SFC(Single File Component)

   * 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.
     * 즉, Single File Component
   * Vue instance에서는 HTML, CSS, JavaScript 코드를 한 번에 관리
     * 이 Vue instance를 기능 단위로 작성하는 것이 핵심!
   * 컴포넌트 기반 개발의 핵심 기능

   다) 정리

   * HTML, CSS, JavaScript를 .vue라는 확장자를 가진 파일 안에서 관리하며 개발
   * 이 파일을 Vue instance, 또는 Vue component라고 하며, 기능 단위로 작성
   * Vue CLI가 Vue를 Component based하게 사용하도록 도와줌

3. Vue component 구조

   가) 템플릿(HTML)

   * HTML의 body 부분
   * 눈으로 보여지는 요소 작성
   * 다른 컴포넌트를 HTML 요소처럼 추가 가능

   나) 스크립트(JavaScript)

   * 자바스크립트 코드가 작성되는 곳
   * 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨
   * 인스턴스 만드는 행위가 없어짐(const app = new Vue()) 왜냐면 파일이 컴포넌트니깐

   다) 스타일(CSS)

   * 컴포넌트의 스타일을 담당

4. Vue component 구조 정리

   가) 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦

   나) root에 해당하는 최상단의 component가 App.vue

   다) 이 App.vue를 index.html과 연결

   라) 결국 index.html 파일 하나만을 rendering(이게 바로 SPA)

5. Vue component 실습

   가) 현재 구조

   * Vue CLI를 실행하면 이미 HelloWorld.vue라는 컴포넌트가 생성되어 있고 App.vue에 등록되어 사용되고 있음
     * npm run serve 명령어를 진행했을 때 나온 화면의 대부분이 HelloWorld.vue

   cf) node_modules 다운받으려면 : npm install

다. Pass Props & Emit Events

1. Data in components

   가) 우리는 정적 웹 페이지가 아닌, 동적 웹페이지를 만들고 있음

   * 즉, 웹 페이지에서 다뤄야 할 데이터가 등장
   * User data, 게시글 data, 등등…

   나) 한 페이지 내에서 같은 데이터를 공유해야 함

   * 하지만 페이지들은 component로 구분이 되어있음

   다) Mycomponent에 정의된 data를 MyChild에서 사용하려면 어떻게 해야할까?

   라) MyChild에도 똑같은 data를 정의

   * MyComponent의 data와 MyChild의 데이터가 동일한 data가 맞는가?
   * MyComponent의 data가 변경된다면 MyChild도 같이 변경이 될까?
   * 아니다. 각 Component는 독립적이므로 서로 다른 data를 갖게 될 것이다.
   * 그렇다면 완전히 동일한 data를 서로 다른 Component에서 보여주려면 어떻게 해야 할까?
   * 필요한 컴포넌트들끼리 데이터를 주고받으면 될까?
     * 데이터의 흐름을 파악하기 힘듦
     * 개발 속도 저하
     * 유지보수 난이도 증가
   * 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 하자!
     * 데이터의 흐름을 파악하기 용이
     * 유지보수하기 쉬워짐

2. pass props & emit event

   가) 부모 ⇒ 자식으로의 데이터의 흐름

   * pass props의 방식

   나) 자식 ⇒ 부모로의 데이터의 흐름

   * emit event의 방식

3. Pass Props

   가) 요소의 속성을 사용하여 데이터 전달

   나) props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

   다) 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함

4. Emit Event : 아래에서 위로 갈 때는 소리를 쳐야 함, 부모가 청취해야 함

   가) 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생 시킴

   나) 이벤트를 발생시키는 게 어떻게 데이터를 전달하는 것이냐?

   * 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
   * 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음

