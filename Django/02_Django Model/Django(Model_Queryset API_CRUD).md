#### Django

* Django Model
* Queryset API
* CRUD with view functions



가. Database

1. 체계화된 데이터의 모임

2. 잘 정리하면 보다 작업을 쉽게 할 수 있음

3. 데이터베이스 기본 구조

   가) 스키마 

     1)데이터베이스의 뼈대

     2)자료의 구조, 표현 방법, 관계 등을 정의한 구조

   나) 테이블

     1)테이블(한 시트)이 모여 데이터베이스를 이룸

     2)필드(열, column, 속성)와 레코드(행, row, 튜플, 실제 데이터가 작성된 곳)를 사용해 조직된 데이터 요소들의 집합

     3)관계라고도 부름

   다) 필드

     1)속성 혹은 컬럼(column)

     2)각 필드에는 고유한 데이터 형식이 지정됨(INT, TEXT 등)

   라) 레코드

     1)튜플 혹은 행(row)

     2)테이블의 데이터는 레코드에 저장됨

     3)4명의 고객정보가 저장되어 있으면 레코드는 4개가 존재

   마) PK(Primary Key)

     1)기본 키(id 키)

     2)다른 항목과 절대로 중복될 수 없는 단일 값(unique) ex) 주민등록번호

   바) 쿼리(Query)

     1)데이터를 조회하기 위한 명령어, 내가 데이터베이스에 보내는 명령어

     2)조건에 맞는 데이터를 추출하거나 조작하는 명령어

     3)Query를 날린다. ⇒ 데이터베이스를 조작한다.

나. Django Model

1. Model은 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구 / 저장, 정리, 조작하는 도구

2. 필수적인 필드(컬럼)를 정의, 인스턴스를 통한 메서드를 통해 동작을 행하는 것 같음. ⇒ 이 둘을 통해 구조를 짠다.

3. 모델 클래스 1개 == 데이터베이스 테이블 1개 (테이블?)

   models.py 내 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것 (스키마?)

   ```python
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
   
   # 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
   # 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
   # 클래스 상속 기반 형태의 Django 프레임워크 개발 -> 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것
   
   # models 모듈을 통해 어떠한 타입의 DB필드(컬럼)을 정의할 것인지 정의
   # 클래스 변수 title과 content은 DB필드를 나타냄
   
   # 클래스 변수(속성)명 : DB 필드의 이름
   # 클래스 변수 값(models 모듈의 Field 클래스) : DB 필드의 데이터 타입
   ```

4. 모델을 통해서 데이터베이스에 간접적으로 접근, 조작 (직접 x)

5. 모델 ≠ 데이터베이스 / 독립적인 데이터베이스와 소통을 하는 것이 모델

6. 모델을 통한 데이터 관리가 핵심!

7. 매핑 : 하나의 값을 다른 값으로 대응시키는 것

   일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑

8. Migrations : models.py에 생긴 변화를 DB에 업데이트 해주는 것, **명령어 매우 중요!!!**

   ```bash
   python manage.py makemigrations 
   # migrations 폴더 안에 migrations 파일(설계도) 만들기 
   # 데이터베이스에 보내기 전 실제 최종 설계도 => 아직 DB 생기지 않음
   # 명령어 실행 후 migrations/0001_initial.py가 생성됨
   
   python manage.py migrate
   # 데이터베이스에 최종적으로 보내는 명령어
   # 모델의 변경사항과 데이터베이스를 동기화
   
   # 0001 뭐시기 출력되는데 숫자 4자리는 migration 파일.. 
   # 나는 migration 파일 하나 만들었는데 수많은 migration 파일은 뭐지?
   # 장고에 내장되어 있는 것들이 있음. 처음에 migrate하면 많이 출력되는 건 당연
   
   # 이제 db.sqlite3 에 쓰여짐
   # sqlite 설치 후
   # 오른쪽 클릭 후 open database
   # 밑에 생김
   
   # articles_article('앱_클래스' 조합하여 생김)
   # 누르면 스키마 정보 뜸
   
   python manage.py showmigrations 
   # migrate 되었는지 알려줌
   # X표시면 완료
   
   python manage.py sqlmigrate articles 0001
   # 앱 이름과 설계도 번호
   # 파이썬 언어가 SQL 언어로 바뀜, 왜냐면 DB에서는 파이썬 언어를 읽지 못해(SQL 언어를 읽음)
   ```

   ```python
   # DateTimeField()
   # 선택 인자
   # 1. auto_now_add : 최초 생성 일자를 기록, created_at에 넣음, 데이터가 실제로 만들어질 때 현재 날짜와 시간이 자동으로 초기화 되도록 함 ex) 게시판에 글 쓸 때
   # 2. auto_now : 최종 수정 일자, last-modified, 수정될 때마다 현재 날짜와 시간이 자동으로 갱신되도록 함.
   # (이름 헷갈리니깐 잘 분류!!) 시험!!
   
   # 컬럼이 5개이지만 입력을 받는 건 2가지뿐
   ```

다. ORM(Object Relational Mapping)

1. makemigrations로 인해 만들어진 설계도는 파이썬으로 작성되어 있는데 SQL만 알아 들을 수 있다는 DB가 어떻게 이 설계도를 이해하고 동기화를 이룰 수 있을까?
2. 장고(파이썬)와 DB(SQL) 이 사이를 번역해주는 것이 ORM
3. 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간(장고↔데이터베이스)에 데이터를 변환하는 프로그래밍 기술
4. Django는 내장 Django ORM을 사용
5. 한 마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체
6. 장점 : SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능, 높은 생산성
7. 단점 : 프로젝트가 엄청 커졌을 때는 SQL이 필요할 때가 온다

라. QuerySet API : ORM이 사용하는 메서드들의 이름

1. 외부 라이브러리 설치 및 설정

   ```bash
   # 실습 편의를 위해
   pip install ipython : 파이썬 기본 쉘보다 더 강력한 쉘 제공
   pip install django-extensions : 이건 settings 들어가서 앱등록까지('django_extensions',), Django 확장 프로그램 모음, shell_plus 등 다양한 확장 기능 제공
   
   # 패키지 목록 업데이트
   pip freeze > requirements.txt
   
   cf)
   Shell (깃배쉬가 Shell 종류 중의 하나)
   사용자와 운영체제 간의 소통을 돕는다.
   
   파이썬 쉘 : 파이썬 인터프리터라고도 함, 한 줄 입력하면 바로 출력해줌
   배쉬열어서
   python -i or ipython : 파이썬 쉘 켜짐
   exit() : 꺼짐
   데이터 테스트할 때 사용
   
   Django shell
   ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용, 다만 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에 Django 환경 안에서 진행할 수 있는 Django 쉘을 사용
   기본(python manage.py shell)이 안좋아서 
   django-extensions이 제공하는 더 강력한 shell_plus(python manage.py shell_plus) 설치
   
   파이썬 쉘이 장고 환경에서 켜진다. ipython도 켜짐
   이 쉘이 시작됨으로써 많이 사용하는 클래스, 메서드, 모듈이 자동으로 import됨, 우리가 만든 것도 import됨
   ```

2. 첫 ORM 명령어 사용하기

   ```bash
   Article.objects.all() : DB에 전체 데이터를 조회해줘
   ```

3. Database API

   가) Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움.

   나) 모델(Ariticle)을 정의하게 되면 만들고 읽고 수정하고 지울 수 있는 API를 제공

   다) 구문 

   ```bash
   Article.objects.all()
   Model class. Manager. Queryset API
                            이게 중요
   오브젝트 안에 API가 들어있고 그 API가 조작 명령 가능(생성 조회 수정 삭제)
   
   objects는 그냥 고정(안 중요), API를 제공하기 위해 있음.
   all이 중요!!
   
   Query : 데이터베이스에 데이터를 보여달라고 요청한다
   파이썬 코드가 ORM에 의해 SQL로 변환되어 넘어감
   돌아올 때도 ORM이 QuerySet이라는 자료형으로 변경되어 우리에게 전달됨
   
   QuerySet : 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
   순회 가능, 인덱스로 접근 가능
   ORM을 통해 만들어진 자료형, 필터를 걸거나 정렬 가능
   단일한 객체를 반환할 때는 QuerySet이 아닌 인스턴스로 반환됨
   ```

4. QuerySet API 

   ```bash
   QuerySet API를 활용해 데이터를 생성/조회/수정/삭제 해보자
   
   CRUD
   Create / Read / Update / Delete
   대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말
   ```

   가) Create

   ```bash
   데이터 객체를 만드는(생성하는) 3가지 방법
   첫 번째 방법(특정 테이블에 새로운 행을 추가하여 데이터 추가)
   article = Article() Article(class)로부터 article(instance) 생성
   article.title = 'first' 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
   article.content = 'django!' 
   article.save() 인스턴스로 save 메서드 호출, 꼭 save해줘야 써짐(레코드 생성)
   article 출력하면 id를 출력함
   시간은 UTC 유지됨
   
   두 번째 방법(인스턴스 생성 시 초기 값을 함께 작성하여 생성)
   article = Article(title='second', content='django!')
   article # None, save를 안해줘서
   article.save() # DB에 저장함
   article # id 2 출력
   Article.objects.all() # 전체 조회, <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]> 리스트 하나로
   article.title # 'second'
   article.content # 'django!'
   article.id # 2
   article.pk # 2 , id랑 완전 똑같음!
   
   세 번째 방법
   Article.objects.create(title='third', content='django!') # save 안 해도 DB에 적혀지고 출력까지 됨
   ```

   나) Read (제일 중요!!)

     1)어떻게 조회하는지가 중요!!, 거꾸로 조회, 몇번째부터 몇번째까지 조회 등등

     2)queryset을 받는냐 받지 않느냐, 목록을 받느냐 단일을 받느냐로 2가지로 분류됨

   ```bash
   all() 전체 데이터 조회
   Article.objects.all() # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
   articles = Article.objects.all()
   for article in articles: # 순회 가능
   	print(article)
   	
   get() : 단일 데이터 조회!! 유니크한 값 -> pk 조회할 때만 무조건 get!!
   객체를 찾을 수 없어도 에러, 둘 이상이어도 에러
   단일이기에 쿼리셋으로 오지 않음.
   Article.objects.get(id=1) # 변수 넣어서 사용
   Article.objects.get(pk=1)
   Article.objects.get(pk=100) # 찾을 수 없어서 에러
   Article.objects.get(content='django!') # 둘 이상이어서 에러
   #
   article = Article.objects.get(title='third') # 이 방식 많이 씀!
   article.title # 'third'
   article.content # 'django'
   article.pk # 3
   
   filter() : 쿼리셋 리턴
   Article.objects.filter(content='django!') # 세 개 다 찾아줌
   Article.objects.filter(content='python!') # 없어도 에러 나지 않고 빈 쿼리셋을 줌
   Article.objects.filter(title='first') # 하나여도 쿼리셋으로 줌! 주의!
   Article.objects.filter(pk=1) # 이렇게 하면 2가지 위험, 하나여도 쿼리셋으로 주기 때문에 한 겹을 더 벗겨내야함, 없으면 에러줘야하는데 그렇지 못함.
   
   Field lookups : 특정 레코드에 대한 조건을 설정하는 방법
   QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
   Article.objects.filter(content__contains='ja') # content에 'ja'가 포함된 것을 조회
   ```

   다) Update

   ```bash
   수정 전에 조회를 해야해 그리고 변수로 저장해줘야 돼
   article = Article.objects.get(pk=1) # get으로 해줘야함, filter안됨
   article.title = 'byebye' # save 안하면 무용지물
   article.save() # 수정시간 바뀜, 최초시간이 아니라
   ```

   라) Delete

   ```bash
   DELETE 너무 쉬워~~
   삭제도 하기 전에 조회
   article = Article.objects.get(pk=1)
   article.delete()
   1번 없어졌는데 그 다음에 생성이 되면 1번일까 4번일까, 4번이 됨!! 삭제되면 끝(재사용x)
   ```

   cf) 

   ```bash
   __str__() : 객체 출력할 때 표현법 바꾸는 법 
   
   class 내부에
   
   	def __str__(self):
   		return self.title # 장고 쉘 다시 껐다 키고
   
   Article.objects.all() # 2, 3이 아니라 second, third이 출력됨.
   
   # DB에 영향을 주지 않기 때문에 migrate 안해도됨
   ```

마. CRUD with view functions : 실제 구현은 Django(Model) 폴더에서..

  cf) create 구현하기 위해서는 view 함수가 몇 개 필요할까?

    1. 글을 작성할 페이지를 리턴
    1. 데이터 받아서 DB에 저장하는 함수