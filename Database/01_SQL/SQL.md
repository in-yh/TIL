#### Database

* Database
* SQL
* DDL(Data Definition Language)
* DML(Data Manipulation Language)



가. Database

1. 스프레드 시트와 달리 프로그래밍 언어를 사용해 작동시킴

2. 가장 많이 쓰이는 유형은 RDB라고 부르는 관계형 데이터베이스

3. RDB는 각각의 데이터를 테이블(스프레드시트와 똑같이 생김)에 기입함

4. 쉽게 생각하면 스프레드시트 파일의 모음이 RDB이다~

5. DB 학습의 기초 : 데이터베이스에 데이터를 어떻게 입력(저장, 수정, 삭제)하고 어떻게 출력(조회)하는가 => 결국 CRUD!!

6. DBMS(Database Management System) : 데이터베이스를 조작하는 프로그램

   가) 예시 : Oracle, MySQL, SQLite

   나) SQL : 데이터베이스를 조작하기 위해 사용하는 언어를 SQL이라고 함

7. 웹 개발에서 대부분의 데이터베이스는 RDBMS을 사용하여 SQL 언어를 통해 데이터와 프로그래밍을 구성

나. RDB(관계형 데이터베이스)

1. 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식

2. 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 있음

3. 기본구조

   가) 스키마 : 테이블의 구조, 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술

   나) 테이블

     1)필드(컬럼)

     2)레코드(행)

     3)기본 키 : PK

4. RDBMS : 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램 / 다 똑같은 언어(SQL)를 사용 / SQLite, MySQL 등

5. SQLite

   가) 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스

   나) 장고 프레임워크의 기본 데이터베이스

다. SQL

1. RDBMS의 ‘데이터를 관리’하기 위해 설계된 특수 목적의 프로그래밍 언어
2. RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
3. 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
4. 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음
5. SQL은 데이터베이스와 상호작용하는 방법

라. SQL Commands

1. 종류

   가) DDL(Data Definition Language, 데이터 정의 언어) : 테이블과 스키마를 정의(생성, 수정, 삭제) / CREATE, DROP, ALTER

   나) DML(Data Manipulation Language, 데이터 조작 언어) :  데이터를 조작(여기가 바로 CRUD!!) / INSERT, SELECT, UPDATE, DELETE

   다) DCL(Data Control Language, 데이터 제어 언어) :  권한 설정을 담당하는 부분은 지원하지 않아 생략

2. SQL Syntax

   가) 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고(대문자 권장), 세미콜론(;)으로 끝남

   나) Statement(문) > Clause(절) / 절은 단독적으로 실행할 수 없음

마. DDL : 테이블 혹은 스키마를 정의, 만드는 것 뿐만 아니라 수정, 삭제도 함

* CREATE TABLE
* SQLite Data Types
* Constraints
* ALTER TABLE
* DROP TABLE

1. 사전 준비

   ```bash
   winpty sqlite3 : sqlite 켜기
   sqlite3 : alias 등록 후 켜기
   .exit : sqlite 끄기
   
   데이터베이스 mydb.sqlite3 파일 생성
   DDL.sql 파일 생성
   실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼 클릭 후 Run Selected Query 선택 : sql과 데이터베이스가 연결이 안 되어 있으면, 위에 sql과 데이터베이스 연결하게끔 뭐가 뜸
   ```

바. DML : 데이터 조작하기(CRUD)

* Simple query
* Sorting rows(정렬)
* Filtering data(필터)
* Grouping data(그룹)
* Changing data(수정)

1. INSERT, SELECT, UPDATE, DELETE

   ​     C            R              U            D

2. csv 파일 데이터를 import해서 사용하는 법

   ```bash
   # bash
   # csv 파일을 SQLite 테이블로 가져오기
   sqlite3 # sqlite3 켜기
   # DML.sql 파일 생성 후 테이블 생성 + 데이터베이스와 연결까지 해야함
   .open mydb.sqlite3 # 데이터베이스 파일 열기
   .mode csv # 모드(.mode)를 csv로 설정
   .import users.csv users # .import 명령어를 사용하여 csv 데이터를 테이블로 가져오기
   .exit # 끄기
   ```

사. 마무리

1. Database

   가) RDB

2. SQL

3. DDL

   가) CREATE TABLE

     1)Data Type

     2)Constraints

   나) ALTER TABLE

   다) DROP TABLE

4. DML

   가) SELECT

     1)SELECT DISTINCT

   나) ORDER BY

   다) WHERE

     1)LIKE, IN, BETWEEN

   라) LIMIT, OFFSET

   마) GROUP BY

     1)Aggregate Function

   바) INSERT / UPDATE / DELETE

