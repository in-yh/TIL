* Vue intro
* Why Vue
* Vue instance
* Basic of syntax
* Vue advanced



가. Vue intro

1. 사전 준비

   가) VSCode Vetur extension 설치 : 문법 하이라이팅, 자동완성, 디버깅 기능 제공

   나) Chrome Vue.js devtools extension 설치 및 설정 : 크롬 브라우저 개발자 도구에서 vue 디버깅 기능 제공

2. 개요

   가) Front-end 개발이란 무엇인가

   나) Front-end framework란 무엇인가

   다) Vue를 배우는 이유

   라) Vue 기초 문법

3. Front-end 개발이란 무엇인가

   가) 개요

   * 우리가 앞으로 할 일은 JavaScript를 활용한 Front-end 개발

   * Back-end 개발은 장고로 진행
   * Front-end 개발은? Vue.js (JavaScript Front-end Framework)

4. Front-end framework란 무엇인가

   가) Front-end(FE) 개발이란? 사용자에게 보여주는 화면 만들기

   나) Web App(SPA)을 만들 때 사용하는 도구

   * SPA - Single Page Application

   다) Web App이란?

   * 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
   * 개발자 도구 > 디바이스 모드
   * 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
   * 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

   라) SPA (Single Page Application) (하나의 페이지!)

   * Web App과 함께 자주 등장할 용어 SPA

   * 이전까지는 사용자의 요청에 적절한 페이지 별 template을 반환

   * SPA는 서버에서 "최초 1장의 HTML만 전달받아" 모든 요청에 대응하는 방식을 의미

     * 어떻게 한 페이지로 모든 요청에 대응할 수 있을까?
     * CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문
       * 이전에는 서버가 렌더링을 했는데 지금부터는 클라이언트가 렌더링을 함

     cf) SSR(Server Side Rendering)이란?

     * 기존 요청 처리 방식은 SSR
     * "Server"가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식(서버가 완성된 문서를 만들어서 렌더링함 / 클라이언트는 하는게 없음 그냥 받아서 출력)
     * 전달 받은 새 문서를 보여주기 위해 "브라우저는 새로고침을 진행"

   * CSR(Client Side Rendering)이란?

     * 최초 한 장의 HTML을 받아오는 것은 동일
       * 단, server로부터 최초로 받아오는 문서는 "빈 html 문서"(그리는 건 클라이언트가 그린다. 즉, 자바스크립트가)
     * 각 요청에 대한 대응을 자바스크립트를 사용하여 필요한 부분만 다시 렌더링
       * 새로운 페이지를 서버에 AJAX로 요청
       * 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달(DRF처럼)
       * JSON 데이터를 자바스크립트로 처리, DOM 트리에 반영(렌더링) => 브라우저가 렌더링해야 함(이게 Front-end framework가 하는 일! 백엔드 서버가 주는 데이터들을 이쁘게 구조에 맞게 렌더링하는 것!)

   * 왜 CSR 방식을 사용하는 걸까?

     * 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨

       == 클라이언트 - 서버 간 통신 즉, 트래픽 감소

       == 트래픽이 감소한다 = 응답 속도가 빨라진다.

     * 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행

       * SNS에서 추천을 누를 때마다 첫 페이지로 돌아간다 = 끔찍한 App!
       * 요청이 자연스럽게 진행이 된다 = UX 향상

     * BE와 FE의 작업 영역을 명확히 분리할 수 있음

       * 각자 맡은 역할을 명확히 분리한다 = 협업이 용이해짐

   * CSR은 만능일까?

     * 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요

     * Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요

     * 검색 엔진 최적화(SEO)가 어려움

       * 서버가 제공하는 것은 텅 빈 HTML
       * 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행

     * 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움

       cf) SEO, 검색 엔진 최적화

       * google과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
       * 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
         * SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전
       * 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결된 것은 아님

   * CSR과 SSR

     * 적절하게 둘을 활용할 수 있어야 함
     * SPA 서비스에도 SSR을 지원하는 Framework도 발전하고 있음
       * Vue의 Nuxt.js
       * React의 Next.js
       * Angular ..

   * 여러가지 Front-end framework : React, Angular, Vue, Svelte 등

5. Vue를 배우는 이유 : 쉽다!

나. Vue instance

1. M/V/VM Pattern

   가) View(HTML) <=> ViewModel(Vue) <=> Model(JavaScript의 객체)

   ​                                    DOM Listeners (DOM으로부터 이벤트를 듣고)

   ​									Directives (그 DOM을 조작)

   나) View - 우리 눈에 보이는 부분 = DOM!

   다) Model - 실제 데이터 = JSON!

   라) ViewModel(Vue) 중간에서 소통

   * View를 위한 Model
   * View와 연결(binding)되어 Action을 주고 받음
   * Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
   * View에서 사용자가 데이터를 변경하면, View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

   마) 정리

   * View는 Model을 모르고, Model도 View를 모른다.(독립성 증가, 적은 의존성)
   * DOM은 Data를 모르고, Data도 DOM을 모른다.

