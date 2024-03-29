* UX&UI
* Vue Router
* Navigation Guard
* Articles app with Vue



가. UX&UI

1. 개요

   가) 우리는 비슷한 것끼리 묶거나 내용을 구성해서 인지하는 것이 편하다는 것을 알고 있다.

   나) 만약 그렇지 않을 경우 불편하다는 느낌을 받거나 의사결정을 하는데 많은 시간이 걸리기도 한다.

   다) 이러한 요소들은 유저와 밀접한 부분이기에 매우 중요하며 모든 서비스에서 반드시 고려되어야 한다.

   라) 단순한 느낌이나 심미적인 부분만 고려하는 것이 아닌 `체계적인 설계를 통해 기획`해야 한다.

2. UX&UI

   가) UX(User Experience)

   * 데이터를 보니 사람들이 여기 있는 메뉴바를 잘 사용하지 않는 것 같아. 차라리 크기를 확 줄이거나 위치를 조정해보면 어떨까?
   * 유저와 가장 가까이에 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
   * 유저가 느끼는 느낌, 태도 그리고 행동을 디자인
     * 백화점 1층에서 느껴지는 좋은 향수 향기
     * 러쉬 매장 근처만 가도 맡을 수 있는 러쉬 향기
     * 로딩이 너무 길어서 사용하고 싶지 않았던 사이트 등
   * 좋은 UX를 설계하기 위해서는 
     * 사람들의 마음과 생각을 이해하고 정리해서 우리 제품에 녹여내는 과정이 필요
     * 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요

   나) UI(User Interface)

   * 메뉴바의 위치는 다른 구성 요소 배치와 함께 생각했을 때 여기가 좋겠어. 유저는 위에서부터 내려와서 여기에서 결정하는 시나리오를 따를 것 같아

   * 유저에게 보여지는 화면을 디자인

   * UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 Front-end 개발자와 가장 많이 소통

     cf) Interface

     * 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
       * 즉, 사용자가 기기를  쉽게 동작 시키는데 도움을 주는 시스템
     * 우리 일상 속에 인터페이스 예시
       * CLI(command-line interface)나 GUI(Graphic User Interface)를 사용해서 컴퓨터를 조작

   * 좋은 UI를 설계하기 위해서는

     * 예쁜 디자인 즉 심미적인 부분만 중요하다기보다는 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하는 부분까지 고려되어야 함
     * 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등이 필요
     * UI 디자인에 있어 가장 중요한 것은 `협업`

   다) 디자이너와 기획자 그리고 개발자

   * 많은 회사에서 UX/UI 디자인을 함께하는 디자이너를 채용하거나 UX는 기획자, UI는 디자이너의 역할로 채용하기도 함
   * UX(직무 : UX Researcher, User Researcher)
     * (구글) 사용자의 경험을 이해하기 위한 통계모델을 설계
     * (MS) 리서치를 기획하고 사용자에 대한 지표를 정의
     * (Meta) 정성적인 방법과 정량적인 방법을 사용해서 사용자 조사를 실시
   * UI(직무 : Product Designer, Interaction Designer)
     * (구글) 다양한 디자인 프로토타이핑 툴을 사용해서 개발 가이드를 제공
     * (MS) 시각 디자인을 고려해서 체계적인 디자인 컨셉을 보여줌
     * (Meta) 제품을 이해하고 더 나은 UI Flow와 사용자 경험을 디자인
   * 개발자는 단순히 기능 개발만 하는 사람이 아니며 제품에 대해 고민하고 소통하는 능력이 반드시 필요
   * 다양한 분야와의 협업이 필수적이기에 기본적인 UX/UI에 대한 이해

   라) 생각하는 UX&UI 디자인

   * UI 디자인은 너무나 깔끔하게 되었으나 UX를 고려하지 않아 유저들은 잔디밭 위로 지름길을 만들어 다녔고, 심지어 너무 많이 다녀서 잔디마저 모두 사라져버린 상황
   * UX/UI를 디자인 하는 것은 굉장히 섬세하면서 어려운 작업
   * 학문으로서의 UX&UI
     * UX와 UI는 단순히 누군가의 직감에 의해서 결정되는 것이 아님
     * 하나의 학문으로서 연구되고 있는 분야이며 심리학과도 밀접한 연관이 있음
       * UX/UI 그리고 HCI
         * GUI : 유저가 보는 일반적인 시각적인 디자인
         * UI : 유저가 보거나 듣는 등 비시각적인 부분까지 포함한 디자인
         * UX : 유저가 겪는 모든 경험(컴퓨터와 관련이 없는 부분까지도 포함)
         * HCI(Human Computer Interaction) : 인간과 컴퓨터 사이의 상호작용에 대한 학문
     * 점점 더 복잡해지는 기술과 반대로 점점 더 단순하고 대중화 되어야하는 유저에 대한 경험으로 인해 계속해서 연구되는 중요한 분야
     * 예술에 정답이 없듯, 디자인에도 정답이 정해져 있지 않음
     * 전세계의 많은 디자이너 또는 연구자들이 데이터에 기반해서 연구한 다양한 가이드 존재
     * Apple의 UI

   마) Prototyping

   * Software prototyping
     * 애플리케이션의 프로토타입을 만드는 것
     * 즉 개발 중인 소프트웨어 프로그램의 완성되기 전 버전을 만드는 것
     * 한 번에 완성 버전이 나올 수 없기에 중간마다 현재 상태를 체크하는 과정
   * Prototyping Tool 시장
     * UI/UX 디자인을 prototyping하기 위한 도구는 굉장히 많고 빠른 패러다임의 변화로 인해 치열한 경쟁이 계속되고 있음
     * 현재는 `Figma`라는 툴을 많이 사용
   * Figma
     * 인터페이스 디자인을 위한 협업 웹 애플리케이션
     * `협업`에 중점을 두면서 UI/UX 설계에 초점을 맞춤
     * 왜 Figma?
       * 웹 기반 시스템을 가짐(웹 환경에서 동작, 매우 가벼운 환경에서 실행 가능, 모든 작업 내역이 웹에 저장됨)
       * `실시간으로 팀원들이 협업`할 수 있는 기능 제공
       * 직관적이고 다양한 디자인 툴 제공
       * Figma 사용자들이 만든 다양한 플러그인이 존재
       * 대부분의 기능을 무료로 사용
     * 성공의 이유
       * 성능의 희생을 일부 감수하고 가벼운 환경 선택, 웹 기반으로 원활한 협업이 이루어지도록 함
       * `디자인` 그 자체에만 집중할 수 있게 함
       * Adobe 사가 인수함
   * 프로젝트를 시작하기 전에
     * 개발부터 시작하지 말고 반드시 충분한 기획을 거칠 것
     * 우리가 완성하고자 하는 대략적인 모습을 그려보는 과정이 필요(프로토타입), 완성본만 보면 안되고 중간과정이 필요
     * 이러한 과정을 통해서 기획에서 빠진 화면이나 API 등을 확인할 수 있음
     * 설계와 기획이 끝난 후 개발을 시작해야 체계적인 진행이 가능함
   * 프로젝트와 협업
     * 협업은 프로젝트와 팀이 성공하기 위한 토대
     * 어떻게 효과적으로 잘 협업할 수 있는지 다양한 방법과 도구를 찾아보고 학습하며 여러 프로젝트를 경험하는 과정이 반드시 필요

나. Vue Router

1. Routing

   가) 네트워크에서 다음 경로를 선택하는 프로세스

   나) 웹 서비스에서의 라우팅

   * 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

   다) /articles/index/에 접근하면 articles의 index에 대한 결과를 보내줌

2. Routing in SSR

   가) Server가 모든 라우팅을 통제

   나) URL로 요청이 들어오면 응답으로 완성된 HTML 제공

   * 장고로 보낸 요청의 응답 HTML은 완성본인 상태였음

   다) 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

3. Routing in SPA/CSR

   가) 서버는 하나의 HTML(index.html)만을 제공

   나) 이후에 모든 동작은 하나의 HTML 문서 위에서 자스 코드를 활용

   * DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리

   다) 즉, 하나의 URL만 가질 수 있음

4. Why routing?

   가) 그럼 동작에 따라 URL이 반드시 바뀌어야 하나? NO!, 단 유저의 사용성 관점에서는 필요함

   나) 라우팅이 없다면,

   * 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
   * 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
     * 새로고침 시 처음 페이지로 돌아감
     * 링크를 공유할 시 처음 페이지만 공유 가능
   * 브라우저의 뒤로 가기 기능을 사용할 수 없음

5. Vue Router

   가) Vue의 공식 라우터

   나) SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

   다) 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
   
   * 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
   * SPA의 단점 중 하나인 "URL이 변경되지 않는다."를 해결
   * 보여지는 컴포넌트만 교체되는 것이고, URL을 바꿔준다. 페이지는 하나인데 마치 이동하는 것처럼 착각하게 만든다.(사실은 싱글 페이지, 여러개인 것처럼 보여짐, 뒤로가기 가능)
   
   라) (참고) MPA(Multiple Page Application)
   
   * 여러 개의 페이지로 구성된 애플리케이션
   * SSR 방식으로 렌더링
   
   마) 시작하기
   
   * ```bash
     vue create vue-router-app // Vue 프로젝트 생성
     cd vue-router-app // 디렉토리 이동
     vue add router // Vue CLI를 통해 router plugin 적용
     // 기존에 프로젝트를 진행하고 있던 도중에 router를 추가하게 되면 App.vue를 덮어쓰므로 필요한 경우 명령을 실행하기 전에 파일을 백업해두어야 함
     
     history mode 사용여부 -> yes
     // History mode
     //	브라우저의 History API를 활용한 방식
     // 		새로고침 없이 URL 이동 기록을 남길 수 있음
     //	우리에게 익숙한 URL 구조로 사용 가능
     //		예시) http://localhost:8080/index
     //	History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨('#'을 통해 URL을 구분하는 방식)
     //		예시) http://localhost:8080#index
     ```
   

다. Navigation Guard

1. 