#### CSS Layout

* float
* flexbox

#### bootstrap

* bootstrap grid system

#### Responsive web



가. CSS Layout techniques

1. Display
2. Position
3. Float : 옛날에 많이 씀
4. Flexbox
5. Grid
6. 기타 : Responsive Web Design, Media Queries(핸드폰, 태블릿에서 볼 수 있도록)

나. Float

1. CSS 원칙 : Inline Direction(글자), Block Direction(블록, 레고 쌓이듯이) -> 이렇게는 우리가 원하는 레이아웃(구조)을 만들지 못함

2. 모든 요소는 네모(박스모델)이고, 위에서 아래로 왼쪽에서 오른쪽으로 쌓인다.

3. 어떤 요소를 감싸는 형태로 배치는? 혹은 좌/우측에 배치는?(기사-사진 나란히 하는 거)

4. 그래서 나온게 float, 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함. float left, float right 적용시키면 요소가 normal flow를 벗어나도록 함.

5. Float 속성

   가) none : 기본값

   나) left : 요소를 왼쪽으로 띄움

   다) right : 요소를 오른쪽으로 띄움

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
     <style>
       /* CSS 작성*/
       .box {
         width: 150px;
         height: 150px;
         border: 1px solid black;
         background-color: crimson;
         margin: 20px;
       }
       .left {
         float: left; /* float 붕 뜸 -> 겹치게 됨 */
       }
       .right {
         float: right; /* 오른쪽으로 정렬 */
       }
     </style>
   </head>
   <body>
     <!-- 클래스 선택자 .   div.box*3 하면 box 클래스가 있는 div 3개 만듦-->
     <div class="box left">float left</div> <!-- ctrl + alt + 화살표 아래 : 여러개 쓰기 -->
     <div class="box left">float left</div>
     <div class="box right">float right</div>
     <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque distinctio beatae culpa? Culpa sed id saepe quidem aut unde cum, laudantium obcaecati illum eveniet inventore tenetur illo quae! Ut, quod!</p>
   </body>
   </html>
   ```

6. 활용사례 : 옛날에 메뉴들 나눌 때 float 많이 씀

다. Flexbox(주로 활용)

1. CSS Flexible Box Layout

   가) 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

   나) 축 : main axis(메인 축), cross axis(교차 축)

   다) 구성 요소 : Flex Container(부모 요소), Flex item(자식 요소)

     1)Flex Container(부모 요소)

       * flexbox 레이아웃을 형성하는 가장 기본적인 모델
       * Flex Item들이 놓여있는 영역
       * display 속성을 flex 혹은 inline-flex로 지정

     2)Flex Item(자식 요소)

       * 컨테이너에 속해 있는 컨텐츠(박스)

   ```html
   .flex-container { <!-- Flex Container(부모 요소) -->
     display: flex; 쓰면 블록이 마치 인라인(내용물의 크기만큼만 차지)처럼 변경됨.
     display : inline-flex 파란색 사각형이 줄어듦. 요소들만큼만 파란색 사각형이 생김. <!-- Flex Item(자식 요소) -->
   
     꼬지의 방향을 정한다!
     flex-direction : row; 기본 (1 2 3) ---->
     flex-direction : column; 기본, 아래로
     flex-direction : row-reverse;  반대편에 배치됨 (3 2 1) <--- 굉장히 헷갈림.. 이거만 마스터 하면 됨,, 양 많음..
     flex-direction : column-reverse; 아래부터 1번으로 배치  3 ^
                                                          2 | 
                                                          1 |
   }
                                                          
   역방향의 경우 html 태그 선언 순서와 시각적으로 다르니 유의
                                                          
   ---> 축이 이렇게 생김 1 2 3 main axis / 먹을 때 위아래로 뜯어먹는 것처럼, main과 수직인 거는 cross axis
   ^
   |                3
   |                2
   | 축이 이렇게 생김 1 main axis / 오른쪽 왼쪽이 cross axis
         
   Flex는 부모 요소에 적용시켜야 됨!! Item한테 하는게 아니다!! (사각형 안에 정렬하는 것임!!)
   ```

2. 왜 Flexbox를 사용해야하나? 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position, 수직 정렬 & 아이템의 너비와 높이 혹은 간격을 동일하게 배치하기 위해

3. Flex 속성

   가) 배치 설정 : flex-direction, flex-wrap

   나) 공간 나누기 : justify-content (main axis), align-content(cross-axis)

     1)123띔띔띔이 아니라 1띔2띔3띔 이렇게 하기도 함

   다) 정렬 : align-items(모든 아이템을 cross axis 기준으로), align-self(개별 아이템)

4. flex-wrap 

   가) 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정

   나) 즉 기본적으로 컨테이너 영역을 벗어나지 않도록 함

   다) wrap : 아이템 크기 줄이지 않고 줄바꿈 함.

   라) nowrap : 아이템 크기를 줄이고 해당 칸 안에 다 끼워넣음.

5. flex-flow 

   가) flex-direction과 flex-wrap의 shorthand

   나) flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성

     ex1) flex-flow: row nowrap;

     ex2)                                            4 5 6 

   ​          flex-flow: wrap-reverse : 1 2 3 최신글을 쓰고 싶을 때

6. justify-content : 'main-axis' 기준으로 공간 배분!!

   가) flex-start : 기본 값

   나) flex-end : 오른쪽 정렬인데 (                 1 2 3) row-reverse랑 순서 다름

   다) center : 자주 씀

   라) space-between : 1 공간 2 공간 3 (공간 사이의 너비 같다)

   마) space-around : 공간 1 공간 공간 2 공간 공간 3 공간 (어라운드의 공간을 똑같이)

   바) space-evenly : 공간 1 공간 2 공간 3 공간 (전체 영역 간격을 동일하게)

     ex) justify-content: space-evenly;

7. align-content : 'cross-axis' 기준!!(아이템이 한 줄로 배치되는 경우 확인할 수 없음)

   가) 위와 같음

8. align-items : 모든 아이템을 cross-axis 기준으로

   가) stretch : 쭉 늘린다. 컨테이너를 가득 채움

   나) flex-start

   다) flex-end

   라) center : 많이 씀

   마) baseline : 글자 선에 맞춤, 카드선이 아니라

9. align-self : 개별 아이템을 cross-axis 기준으로, 나만 정렬

   가) stretch

   나) flex-start

   다) flex-end

   라) center

10. 기타 속성

    가) flex-grow : 남은 영역을 아이템에 분배(main 기준) 크기만큼 비율 가짐

    나) order : 배치 순서, 많이 쓰진 않음, 눈에 보이는게 실행순서가 아니라서

11. 활용 레이아웃

    가) 수직 수평 가운데 정렬

    ```html
    .container {
      display: flex;
      justify-content : center;
      align-items : center;
    }
    ```

    나) 카드배치

라. Bootstrap : 이미 만들어져 있는..

1. 웹 과목의 열매! 빠르고 반응형(모바일 대응 가능)으로 만들 수 있음, 세상에서 인기 제일 많은, 컴포넌트를 제공 ex) 넷플릭스

2. html vs bootstrap(글씨도 크고, 윗마진도 없음) => 약간씩 다름

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
     <!-- CDN 가져오기!! -->
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous"> 
   </head>
   <body>
     <h1>bootstrap으로 만든 h1태그</h1> <!-- 마진도 거의 없고 폰트나 굵기도 다름 -->
   
     <div class="row row-cols-1 row-cols-md-2 g-4"> <!-- 카드 포맷을 쓸 수 있음 -->
       <div class="col">
         <div class="card">
           <img src="..." class="card-img-top" alt="...">
           <div class="card-body">
             <h5 class="card-title">Card title</h5>
             <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
           </div>
         </div>
       </div>
       <div class="col">
         <div class="card">
           <img src="..." class="card-img-top" alt="...">
           <div class="card-body">
             <h5 class="card-title">Card title</h5>
             <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
           </div>
         </div>
       </div>
       <div class="col">
         <div class="card">
           <img src="..." class="card-img-top" alt="...">
           <div class="card-body">
             <h5 class="card-title">Card title</h5>
             <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
           </div>
         </div>
       </div>
       <div class="col">
         <div class="card">
           <img src="..." class="card-img-top" alt="...">
           <div class="card-body">
             <h5 class="card-title">Card title</h5>
             <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
           </div>
         </div>
       </div>
     </div>
       
     <!-- CDN 가져오기!! script 태그는 닫는 body 태그 바로 위에 -->
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

3. Bootstrap 기본 원리

   가) spacing (Margin and padding)

   ```html
   {property}{sides}-{size}
   margin or padding / top, bottom 등등 / 크기
   <div class="mt-3 ms-5">bootstrap-spacing</div>
    
   mt-3
   margin top 3
   
   ms-5
   margin start 5
   
   위아래 16px 주고 싶다면? my-3
   .mx-0? 좌우 마진 0
   .mx-auto? 좌우 마진 알아서 채워줌, 수평 중앙 정렬, 가로 가운데 정렬
   .py-0? 패딩 위아래 0
   ```

     1)sides

       * t : top
       * b : bottom
       * s : start, left
       * e : end, right
       * x : 양옆
       * y : 위아래
       * blank

     2)size

       * 마진, 패딩 안줌
       * 1 :  0.25rem(4px) / 1rem : 16px(기본)
       * 2 : 0.5rem(8px)
       * 3 : 1rem(16px)
       * 4 : 1.5rem(24px)
       * 5 : 3rem(48px)
       * auto : 양옆 자동으로 채워주는 것

   나) Color

   다) Text

   라) Display

   마) Position

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
     <title>Document</title>
     <style>
       body {
         height: 5000px;
       }
       .box { /* 부트스트랩이랑 안겹치게 해야함 */
         width: 100px;
         height: 100px;
         background-color: crimson;
         border: 2px solid black;
         color: white;
       }
       .bigbox {
         width: 500px;
         height: 500px;
         background-color: yellowgreen;
         border: 2px solid black;
         color: white;
       }  
     </style>
   </head>
   <body>
     <h2>Spacing</h2>
     <div class="mt-3 ms-5 box">margin top 3 ms-5</div> <!--div.mt-3.ms-5.box-->
     <div class="m-4 box">margin 4</div>
     <div class="mx-auto box">mx-auto/가운데정렬</div>
     <div class="ms-auto box">ms-auto/오른쪽정렬</div>
   
     <hr>
   
     <h2>Color</h2>
     <div class="bg-primary">이건 파랑</div> <!--div.bg-primary-->
     <div class="bg-secondary">이건 회색</div>
     <div class="bg-danger">이건 빨강</div>
     <div class="bg-warning">이건 노랑</div>
     <p class="text-success">이건 초록색</p>
     <p class="text-danger">이건 빨간색</p>
     <p class="text-light">이건 흰색</p>
       
   
     <hr>
   
     <h2>Text</h2>
     <p class="text-start">text-start</p>
     <p class="text-center">text-center</p>
     <p class="text-end">text-end</p>
     <a href "#" class="text-decoration-none text-dark">Non-underline-Link</a> <!--a.text-decoration-none     자주 씀!!-->
     <p class="fw-bold">Bold text</p> <!-- fontweight -->
     <p class="fw-normal">Normal weight text</p>
     <p class="fw-light">Light weight</p>
     <p class="fs-italic">Italic text</p> <!-- fontstyle -->
   
     <hr>
   
     <h2>Position</h2>
     <!-- <div class="box fixed-top">fixed-top</div>
     <div class="box fixed-bottom">fixed-bottom</div> -->
   
     <button type="button" class="btn btn-primary position-relative"> <!-- relative -->
       Mails <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-secondary">+99 <span class="visually-hidden">unread messages</span></span>
     </button>
   
     <div class="bigbox position-relative"> <!--relative 안하면 브라우저 맨 위로 위치함-->
       <div class="box position-absolute top-0 start-0">top0/start0</div> 
       <div class="box position-absolute top-0 end-0">top0/end0</div> 
       <div class="box position-absolute bottom-0 start-0">bottom0/start0</div> 
       <div class="box position-absolute bottom-0 end-0">bottom0/end0</div> 
     </div>
   
     <h2>Display</h2>
     <div class="d-inline p-2 text-bg-primary">d-inline</div> <!-- d-inline 넣었기에 인라인요소로 변경-->
     <div class="d-inline p-2 text-bg-dark">d-inline</div>
     <div class="d-none p-2 text-bg-dark">d-inline</div> <!--코드는 있으나 눈에 보이지 않음-->
   
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

4. Bootstrap 컴포넌트

   가) Bootstrap 내 컴포넌트 탭 및 검색으로 원하는 UI요소 찾고 변환 후 활용

   나) Buttons

   다) Dropdowns : 여러 개 중 선택할 때

   라) Forms

   마) Navbar : 많이 씀

   바) Carousel(캐러셀) : 회전목마라 부름

   사) Modal : 젤 많이 씀, 경고 띄울 때, 다른 곳 클릭하면 없어짐(팝업과 다름)

   아) Flexbox

   자) Card : 반응형 위해 나온 것 => 그리드 시스템!

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
     <title>Document</title>
   </head>
   <body>
     <h2>Button</h2>
     <button type="button" class="btn btn-primary">Primary</button>
     <button type="button" class="btn btn-secondary">Secondary</button>
     <button type="button" class="btn btn-success">Success</button>
     <button type="button" class="btn btn-danger">Danger</button>
     <button type="button" class="btn btn-warning">Warning</button>
     <button type="button" class="btn btn-info">Info</button>
     <button type="button" class="btn btn-light">Light</button>
     <button type="button" class="btn btn-dark">Dark</button>
     <button type="button" class="btn btn-link">Link</button>
   
     <hr>
     <h2>Dropdown</h2>
     <div class="dropdown">
       <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
         하나를 골라보세요.
       </button>
       <ul class="dropdown-menu">
         <li><a class="dropdown-item" href="#">Action</a></li>
         <li><a class="dropdown-item" href="#">Another action</a></li>
         <li><a class="dropdown-item" href="#">Something else here</a></li>
       </ul>
     </div>
   
     <hr>
   
     <h2>Form</h2>
     <div class="mb-3">
       <label for="exampleFormControlInput1" class="form-label">Email address</label>
       <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
     </div>
     <div class="mb-3">
       <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
       <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
     </div>
   
     <label for="exampleColorInput" class="form-label">Color picker</label>
     <input type="color" class="form-control form-control-color" id="exampleColorInput" value="#563d7c" title="Choose your color">
   
     <h2>Navbar</h2>
     <nav class="navbar navbar-expand-lg bg-secondary">
       <div class="container-fluid">
         <a class="navbar-brand" href="#">Navbar</a>
         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
         </button>
         <div class="collapse navbar-collapse" id="navbarSupportedContent">
           <ul class="navbar-nav me-auto mb-2 mb-lg-0">
             <li class="nav-item">
               <a class="nav-link active" aria-current="page" href="#">Home</a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="#">Link</a>
             </li>
             <li class="nav-item dropdown">
               <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                 Dropdown
               </a>
               <ul class="dropdown-menu">
                 <li><a class="dropdown-item" href="#">Action</a></li>
                 <li><a class="dropdown-item" href="#">Another action</a></li>
                 <li><hr class="dropdown-divider"></li>
                 <li><a class="dropdown-item" href="#">Something else here</a></li>
               </ul>
             </li>
             <li class="nav-item">
               <a class="nav-link disabled">Disabled</a>
             </li>
           </ul>
           <form class="d-flex" role="search">
             <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
             <button class="btn btn-outline-success" type="submit">Search</button>
           </form>
         </div>
       </div>
     </nav>
   
     <hr>
   
     <h2>Carousel 캐러셀</h2>
     <!-- <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
       <div class="carousel-inner">
         <div class="carousel-item active">
           <img src="image/ssap.png" class="d-block w-100" alt="...">
         </div>
         <div class="carousel-item">
           <img src="image/ssap2.png" class="d-block w-100" alt="...">
         </div>
         <div class="carousel-item">
           <img src="image/ssap3.jpg" class="d-block w-100" alt="...">
         </div>
       </div>
     </div> -->
     <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
       <div class="carousel-inner">
         <div class="carousel-item active">
           <img src="image/ssap.png" class="d-block w-100" alt="...">
         </div>
         <div class="carousel-item">
           <img src="image/ssap2.png" class="d-block w-100" alt="...">
         </div>
         <div class="carousel-item">
           <img src="image/ssap3.jpg" class="d-block w-100" alt="...">
         </div>
       </div>
       <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
         <span class="carousel-control-prev-icon" aria-hidden="true"></span>
         <span class="visually-hidden">Previous</span>
       </button>
       <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
         <span class="carousel-control-next-icon" aria-hidden="true"></span>
         <span class="visually-hidden">Next</span>
       </button>
     </div>
   
     <hr>
   
     <h2>Modal</h2>
     <!-- Button trigger modal -->
   <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
     Launch demo modal
   </button>
   
   <!-- Modal -->
   <!-- 중첩해서 들어가 있으면 안 됨, body랑 같은 레벨에 넣기 -->
   <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"> <!--여기 id랑 위에 data-bs-target이랑 묶어주는 거임-->
     <div class="modal-dialog">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
           <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
         </div>
         <div class="modal-body">
           ...
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary">Save changes</button>
         </div>
       </div>
     </div>
   </div>
   
   <hr>
   <h2>Flexbox</h2>
   <div class="d-flex justify-content-start">...</div>
     <div class="d-flex align-items-start">...</div>
     <div class="d-flex">
     <div class="align-self-start">Aligned flex item</div>
   </div>
   
   <hr>
   <h2>Card > Grid card</h2>
   <div class="row row-cols-1 row-cols-md-2 g-4"> <!--반응형 웹-->
     <div class="col">
       <div class="card">
         <img src="image/ssap.png" class="card-img-top" alt="...">
         <div class="card-body">
           <h5 class="card-title">Card title</h5>
           <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
         </div>
       </div>
     </div>
     <div class="col">
       <div class="card">
         <img src="image/ssap.png" class="card-img-top" alt="...">
         <div class="card-body">
           <h5 class="card-title">Card title</h5>
           <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
         </div>
       </div>
     </div>
     <div class="col">
       <div class="card">
         <img src="image/ssap.png" class="card-img-top" alt="...">
         <div class="card-body">
           <h5 class="card-title">Card title</h5>
           <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
         </div>
       </div>
     </div>
     <div class="col">
       <div class="card">
         <img src="image/ssap.png" class="card-img-top" alt="...">
         <div class="card-body">
           <h5 class="card-title">Card title</h5>
           <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
         </div>
       </div>
     </div>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

5. Bootstrap Grid System(web design) : 요소들의 디자인과 배치에 도움을 주는 시스템

   가) 기본요소

     1)Column : 실제 컨텐츠를 포함하는 부분

     2)Gutter : 칼럼과 칼럼 사이의 공간(사이 간격)

     3)Container : Column들을 담고 있는 공간

   나) Bootstrap Grid System은 flexbox로 제작됨

   다) container, rows, column으로 컨텐츠를 배치하고 정렬

   라) 반드시 기억해야할 2가지!! => 12개의 column, 6개의 grid breakpoints(화면크기에 따라서, 그 분기점이 되면 다르게 보여줌)

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
     <style>
       body {
         height: 3000px;
       }
   
       .box {
         background-color: lightgoldenrodyellow;
         border: 1px solid black;
         text-align: center;
         /* padding-top: 0.75rem;
         padding-bottom: 0.75rem; */
       }
   
       .parent {
         border: 1px solid black;
         height: 600px;
         background-color: lightpink;
       }
     </style>
   </head>
   <body>
     <!-- container 쓰는 순간 margin이 생김, 안쓰면 공백없이 너무 불편해보임 -->
     <div class="container">
       <h2 class="text-center">column</h2>
       <!-- 배열이 왼쪽에서 오른쪽으로 잘 되게끔.. -->
       <div class="row">
         <div class="col box">1</div>
         <div class="col box">2</div>
         <div class="col box">3</div>
         <div class="col box">4</div>
       </div>
   
       <div class="row">
         <div class="box col">1</div>
         <div class="box col">2</div>
         <div class="w-100"></div> <!--넓이 100%, 한 칸 띄어줌-->
         <div class="box col">3</div>
         <div class="box col">4</div>
       </div>
       <hr>
       <div class="row">
         <div class="box col">1</div>
         <div class="box col">2</div>
        </div>
        <div> 
         <div class="row">
         <div class="box col">3</div>
         <div class="box col">4</div>
       </div>
   
       <hr>
   
       <div class="row">
         <div class="box col-3">1</div> <!--숫자는 비율을 나타냄-->
         <div class="box col-6">2</div>
         <div class="box col-3">3</div>
       </div>
   
       <hr>
   
       <div class="row">
         <div class="box col-1">1</div>
         <div class="box col-1">2</div>
         <div class="box col-1">3</div>
         <div class="box col-1">4</div>
         <div class="box col-1">5</div>
         <div class="box col-1">6</div>
         <div class="box col-1">7</div>
         <div class="box col-1">8</div>
         <div class="box col-1">9</div>
         <div class="box col-1">10</div>
         <div class="box col-1">11</div>
         <div class="box col-1">12</div>
         <div class="box col-1">13</div> <!--기본이 12이기에 한 줄 넘어감-->
       </div>
   
       <hr>
   
       <div class="row">
         <div class="box col-9">col-9</div>
         <div class="box col-4">col-4</div> <!--12넘어가서 다음줄로 감-->
         <div class="box col-3">col-3</div>
       </div>
   
       <!-- 크기에 따라서 비율이 변경되도록 설정 -->
       <h2>Grid breakpoint</h2>
       <div class="row">
         <div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div>
         <div class="box col-8 col-sm-2 col-md-4 col-lg-2">2</div>
         <div class="box col-2 col-sm-2 col-md-4 col-lg-5">3</div> <!-- 12를 맞추되 비율은 다르게 설정함 -->
       </div>
   
       <!-- nesting은 중첩 가능 -->
       <!-- offset은 비우고 싶을 때 사용 -->
     </div>
     
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

+연습문제

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="shop.css">
  <title>Title</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
  <!-- nav -->
  <nav class="d-flex justify-content-between align-items-center bg-light px-4 py-3">
    <div class="fs-5">Samsung</div>
    <div>
      <a href="#" class="text-decoration-none text-dark me-3">Contact</a>
      <a href="#" class="text-decoration-none text-dark me-3">Cart</a>
      <a href="#" class="text-decoration-none text-dark me-3">Login</a>
    </div>
  </nav>

  <div class="container">
    <!-- section -->
    <section>
      <img src="images/main.png" alt="phone-image" class="img-fluid">
    </section>

    <!-- article -->
    <article class="text-center"> <!--위에다가 해야함-->
      <div class="fw-bold fs-5 my-5">Our New Products</div>

      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
        <a href="#" class="col text-decoration-none text-dark fw-bold">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </div>
        </a>

        <a href="#" class="col text-decoration-none text-dark fw-bold">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </div>
        </a>

        <a href="#" class="col text-decoration-none text-dark fw-bold">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </div>
        </a>

        <a href="#" class="col text-decoration-none text-dark fw-bold">
          <div class="card">
            <img src="images/buds.jpg" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </div>
        </a>

      </div>

    </article>

    <!-- footer -->
    <footer class="d-flex justify-content-center mb-5 pt-5">
      <a href="" style="width: 30px;" class="mx=3"> <!-- a는 글자 -->
        <img src="images/instagram.png" alt="" class="img-fluid"> <!--부모의 100%-->
      </a>
      <a href="" style="width: 30px;" class="mx=3">
        <img src="images/facebook.png" alt="" class="img-fluid">
      </a>
      <a href="" style="width: 30px;" class="mx=3">
        <img src="images/twitter.png" alt="" class="img-fluid">
      </a>
    </footer>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
```



