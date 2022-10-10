# PJT 03

### 이번 pjt 를 통해 배운 내용

- Bootstrap을 이용한 반응형 웹페이지 구현



## A. nav_footer.html

- 요구 사항 :

  * Navigation Bar와 Footer 만들기

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * Bootstrap Navbar Component 참고
    * 스크롤 하더라도 항상 화면 상단 고정
    * 로고 이미지, 내비게이션 메뉴 하이퍼링크 역할 추가
    * Login 클릭 시 Modal 사용
    * Footer 수직 수평 가운데 정렬

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
    <title>Community</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top"> <!-- navbar dark는 해당 페이지에 있을 때 nav 이름을 활성화 시켜주기 위한 클래스 -->
      <div class="container-fluid">
        <a class="navbar-brand" href="02_home.html"><image src="./images/logo.png" class="logo" alt="logo image"></a> <!-- logo 이미지가 너무 커서 CSS파일로 조정 -->>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="02_home.html">Home</a> <!-- active와 aria-current="page" 추가해야 해당 페이지에서 nav 이름 활성화됨-->
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  
    <div class="modal" id="exampleModal" tabindex="-1"> <!-- id와 data-bs-target으로 이어줘야 함 (밖으로 빼기!! nav 안에 넣으면 닫히질 않음) -->
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
              </div>
              <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1">
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Submit</button> <!-- submit으로 바꿈 -->
          </div>
        </div>
      </div>
    </div>
  
    <footer class="d-flex justify-content-center align-items-center fixed-bottom"> <!-- flex 이용해서 가운데 정렬/ fixed 사용 -->
      <div class="text-dark mb-4">Web-bootstrap PJT, by Yuhyun Jeong</div>
    </footer>
  
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  - 이 문제에서 어려웠던 점 : 
    * Login 클릭 시 Modal 나오게 하는 법
    * 열려있는 페이지에 맞게 navbar 메뉴 활성화하는 법 
  - 내가 생각하는 이 문제의 포인트 :
    * Modal class의 id와 Login 하이퍼링크 data-bs-target을 맞추는 것 
    * nav class에 navbar-dark 쓰고, 각 페이지에 맞게 active와 aria-current="page" 추가해야 함.

------

 

## B. home.html

- 요구 사항 :

  * Header, Section 만들기

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * Carousel  사용
    * Card 사용

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
    <link rel="stylesheet" href="02_home.css">
    <title>Community</title>
  </head>
  <body>
    <!-- 01_nav_footer에서 완성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
    <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top"> <!-- navbar dark는 해당 페이지에 있을 때 nav 이름을 활성화 시켜주기 위한 클래스 -->
      <div class="container-fluid">
        <a class="navbar-brand" href="02_home.html"><image src="./images/logo.png" class="logo" alt="logo image"></a> <!-- logo 이미지가 너무 커서 CSS파일로 조정 -->>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="02_home.html">Home</a> <!-- active와 aria-current="page" 추가해야 해당 페이지에서 nav 이름 활성화됨-->
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  
    <div class="modal" id="exampleModal" tabindex="-1"> <!-- id와 data-bs-target으로 이어줘야 함 (밖으로 빼기!! nav 안에 넣으면 닫히질 않음) -->
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
              </div>
              <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1">
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Submit</button> <!-- submit으로 바꿈 -->
          </div>
        </div>
      </div>
    </div>
  
    <!-- 02_home.html -->
    <header> <!-- CSS 파일로 body 전체에 paddding-top 간격을 주면 적당한 위치에서 시작할 수 있음. (nav가 fixed라서 붕 뜨게 되기 때문에 padding을 안주면 nav에 가려짐)-->
      <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="./images/header1.jpg" class="d-block w-100" alt="header1">
          </div>
          <div class="carousel-item">
            <img src="./images/header2.jpg" class="d-block w-100" alt="header2">
          </div>
          <div class="carousel-item">
            <img src="./images/header3.jpg" class="d-block w-100" alt="header3">
          </div>
        </div>
      </div>
    </header>
  
    <h1 class="text-center fw-bold fs-2 m-3">Boxoffice</h1>
  
    <div class="container"> <!-- 좌우 여백 자동적으로 생김!! -->
      <section class="row g-4">
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie1.jpg" class="card-img-top" alt="movie1">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
          </div>
        </article>
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie2.jpg" class="card-img-top" alt="movie2">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a short card.</p>
            </div>
          </div>
        </article>
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie3.jpg" class="card-img-top" alt="movie3">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
            </div>
          </div>
        </article>
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie4.jpg" class="card-img-top" alt="movie4">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
          </div>
        </article>
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie5.jpg" class="card-img-top" alt="movie5">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
          </div>
        </article>
        <article class="col-12 col-sm-4">
          <div class="card h-100">
            <img src="./images/movie6.jpg" class="card-img-top" alt="movie6">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            </div>
          </div>
        </article>
      </section>
    </div>
    
    <footer class="d-flex justify-content-center align-items-center fixed-bottom"> <!-- flex 이용해서 가운데 정렬/ fixed 사용 -->
      <div class="text-dark mb-4">Web-bootstrap PJT, by Yuhyun Jeong</div>
    </footer>
  
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
  </body>
  </html>
  ```

  - 이 문제에서 어려웠던 점 : 
    * Header가 navbar에 가리는 점
    * Section의 여백 주기
  - 내가 생각하는 이 문제의 포인트 : 
    * CSS 파일로 body 전체에 paddding-top 간격을 주면 적당한 위치에서 시작
    * container를 하면 자동으로 여백 생김.

------

 

## C. community.html

* 요구 사항: 
  * Aside(게시판 목록), Section(게시판), Pagination 만들기

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * Aside 만들 때, Bootstrap List 사용
    * Section 만들 때, lg 기준으로 글과 표 나타내기
    * Bootstrap Pagination 사용

  ```html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
    <link rel="stylesheet" href="03_community.css">
    <title>Community</title>
  </head>
  <body>
    <!-- 01_nav_footer에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->
    <nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top"> <!-- navbar dark는 해당 페이지에 있을 때 nav 이름을 활성화 시켜주기 위한 클래스 -->
      <div class="container-fluid">
        <a class="navbar-brand" href="02_home.html"><image src="./images/logo.png" class="logo" alt="logo image"></a> <!-- logo 이미지가 너무 커서 CSS파일로 조정 -->>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="02_home.html">Home</a> 
            </li>
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="03_community.html">Community</a> <!-- active와 aria-current="page"를 community에 추가해줘야 함(해당 페이지에서 active 해줘야 함)-->
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  
    <div class="modal" id="exampleModal" tabindex="-1"> <!-- id와 data-bs-target으로 이어줘야 함 (밖으로 빼기!! nav 안에 넣으면 닫히질 않음) -->
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
              </div>
              <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1">
              </div>
              <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Check me out</label>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Submit</button> <!-- submit으로 바꿈 -->
          </div>
        </div>
      </div>
    </div>
  
    <!-- 03_community.html -->
    <main class="container">
      <h1 class="fw-bold fs-2">Community</h1>
      <!-- Aside - 게시판 목록 -->
      <div class="row">
        <aside class="col-12 col-lg-2"> <!-- lg 미만까지는 column 전체에 할당, lg 이상부터는 column 2줄에 할당-->
          <ul class="list-group">
            <li class="list-group-item"><a href="#" class="text-decoration-none">Boxoffice</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Movies</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Genres</a></li>
            <li class="list-group-item"><a href="#" class="text-decoration-none">Actors</a></li>
          </ul>
        </aside>
  
        <!-- Section - 게시판 -->
        <section class="col-12 col-lg-10"> <!-- lg 미만까지는 column 전체에 할당, lg 이상부터는 column 10줄에 할당-->
          <div class="row table-responsive">          
            <table class="table table-striped table-hover d-none d-lg-block"> <!-- lg 미만까지는 표 안 보이게 하고, lg 이상부터는 표 보이게 함. -->
              <thead class="table-dark">
                <tr>
                  <th scope="col" class="col-2">영화 제목</th> <!-- col-2 넣어줘야 표가 전체적으로 나옴. 안해주면 중간사이즈?로 나옴 -->
                  <th scope="col" class="col-2">글 제목</th>
                  <th scope="col" class="col-2">작성자</th>
                  <th scope="col" class="col-2">작성 시간</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Best Movie Ever</td>
                  <td>user</td>
                  <td>1 minute ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie test</td>
                  <td>user</td>
                  <td>1 minute ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie test</td>
                  <td>user</td>
                  <td>1 minute ago</td>
                </tr>
                <tr>
                  <th scope="row">Great Movie title</th>
                  <td>Movie test</td>
                  <td>user</td>
                  <td>1 minute ago</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="row">
            <article class="d-block d-lg-none"> <!-- lg 미만까지는 보이게 하고, lg 이상부터는 안 보이게 함. -->
              <hr>
              <div class="fs-2">Best Movie Ever</div>
              <div class="fs-4">Great Movie Title</div>
              <div class="fs-6 mb-2">user</div>
              <div class="fs-6">1 minute ago</div>
              <hr>
              <div class="fs-2">Movie Test</div>
              <div class="fs-4">Great Movie Title</div>
              <div class="fs-6 mb-2">user</div>
              <div class="fs-6">1 minute ago</div>
              <hr>
              <div class="fs-2">Movie Test</div>
              <div class="fs-4">Great Movie Title</div>
              <div class="fs-6 mb-2">user</div>
              <div class="fs-6">1 minute ago</div>
            </article>
          </div>
        </section>
      </div>
      <div class="d-flex justify-content-center my-4"> <!-- flex 이용해서 가운데 정렬 -->
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
      </div>
    </main>
  
    <footer class="d-flex justify-content-center align-items-center fixed-bottom"> <!-- flex 이용해서 가운데 정렬/ fixed 사용 -->
      <div class="text-dark mb-4">Web-bootstrap PJT, by Yuhyun Jeong</div>
    </footer>
  
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  - 이 문제에서 어려웠던 점 : 
    * 화면이 lg보다 작으면 text 형태로, lg보다 크면 표 형태로 나타내기  
  - 내가 생각하는 이 문제의 포인트 
    * d-none, d-lg-block 등 d- 이용하기!!

------

 

# 후기

- Bootstrap은 그저 빛, 내가 직접 만든 것보다 가져다 쓰는 게 거의 대부분, 짧게 배웠으나 그럴싸한 웹페이지를 만들 수 있는 아주 좋은 도구!