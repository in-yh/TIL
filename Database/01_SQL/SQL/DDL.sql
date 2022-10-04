-- DDL은 테이블 구조를 관리(CREATE(생성), ALTER(수정), DROP(삭제))

-- CREATE TABLE
CREATE TABLE contacts ( -- CREATE TABLE 테이블이름 ( );
    name TEXT NOT NULL, -- 컬럼이름, 데이터타입, 제약조건(빈값 허용하지 않음)
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE -- 컴마 안됨!!
); -- 들여쓰기는 안해도 되지만, 세미콜론은 꼭 해야 됨!!
-- 실행하고자 하는 명령문에 커서 두고 마우스 우측 클릭 Run Selected Query 누르고 mydb.sqlite3에 연결해주면 됨 => mydb.sqlite3에 스키마 생성
-- pk값은 자동으로 생성되고 rowid로 만들어짐(숨겨져있음)

-- SQLite Data Types
-- 가. 종류
-- 1. NULL : 정보가 없거나 알 수 없음을 의미(NONE과 비슷) / 따옴표 없이 NULL이면
-- 2. INTEGER : 정수 / 따옴표, 소수점, 지수가 없으면
-- 3. REAL : 실수 / 따옴표, 소수점, 지수가 없으면
-- 4. TEXT : 문자 / 따옴표로 묶이면
-- 5. BLOB(Binary Large Object) : 입력된 그대로 저장된 큰 데이터 덩어리, 바이너리 등 멀티미디어 파일, 이미지 데이터 같은 것
-- cf1) Boolean은 없고 정수형(0, 1)으로 저장됨
-- cf2) 날짜, 시간 저장하기 위한 타입이 없음 / TEXT, REAL, INTEGER 값으로 저장할 수 있음(내장 함수가 내부적으로 존재)
-- cf3) Binary Data : 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일 / 컴퓨터는 모두 binary data로 되어 있음(다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것)

-- 나. 특징
-- 1. SQLite는 ‘동적 타입 시스템’을 사용(기존의 엄격하게 타입이 지정된 데이터베이스(MySQL 등)에서는 불가능한 작업을 유연하게 수행할 수 있음)
-- 2. 컬럼에 선언된 데이터 타입에 의해서가 아니라 컬럼에 '저장'된 값에 따라 데이터 타입이 결정됨 
-- 3. 또한, 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨 ⇒ 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지정되고, 문자 ‘1’을 넣을 경우는 TEXT 타입으로 지정됨 => 동적
-- 4. 다만, 다른 데이터베이스와의 호환성 문제가 있기 때문에 데이터 타입을 지정하는 것을 권장
-- 5. 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 자동 변환 되는 게 있음(예를 들어 TEXT 타입 컬럼에 정수 1을 저장할 경우 문자 타입의 '1'로 저장됨) => 정적

-- 다. Type Affinity : 타입 선호도, 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
-- 1. INT라고 써도 INTEGER로 인식
-- 2. 타입 선호도 존재 이유 : 호환성 때문

-- Constraints : 제약조건
-- 가. 개요
-- 1. 제약에 맞지 않다면 입력 거부
-- 2. 사용자가 원하는 조건의 데이터만 유지하기 위함 즉, 데이터 무결성(데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해)을 유지하기 위함

-- 나. 종류
-- 1. NOT NULL : 빈값을 허용하지 않도록 함
-- 2. UNIQUE :  이 값은 고유한 값이 됨(email)
-- 3. PRIMARY KEY : PK를 선언하지 않으면 rowid 자동 생성되나 직접 선언하고 싶다면 써도 됨 / 암시적으로 NOT NULL 조건이 포함되어 있음 / 무조건 INTEGER만 인식됨(INT 안됨)
--   예시) id INTEGER PRIMARY KEY,
-- 4. AUTOINCREMENT : PRIMARY KEY와 반드시 같이 사용됨 / 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지(1,2,3에서 3을 지우고 다시 쓰면 3을 쓰는데 AUTOINCREMENT 쓰면 3을 재사용 안 함) / 장고에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약조건
--   예시) id INTEGER PRIMARY KEY AUTOICREMENT,

-- rowid의 특징
-- 가. 테이블을 생성할 때마다 rowid가 자동으로 생성됨
-- 나. 1에서 시작
-- 다. 직접 id 컬럼을 선언한다면 INTEGER PRIMARY KEY 제약조건을 달아야 함 ⇒ rowid 컬럼의 별칭이 됨(rowid가 사라지지는 않음)
-- 라. AUTOINCREMENT가 없다면 삭제된 행 값을 다시 쓴다.
-- 마. 최대값은 공식문서 확인(2^64)
-- 바. 꽉 찼다면 사용되지 않은 정수를 찾을 수 없기에 에러 발생

-- ALTER TABLE : 기존 테이블 구조 수정
-- 가. 테이블의 이름
-- 나. 컬럼의 이름
-- 다. 새로운 컬럼을 추가
-- 라. 컬럼 삭제

ALTER TABLE contacts RENAME TO new_contacts; -- 테이블 이름 변경

ALTER TABLE new_contacts RENAME COLUMN name TO last_name; -- 컬럼 이름 변경

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL; -- 새 컬럼 추가
-- 테이블에 데이터가 없으면 문제 없으나 기존 데이터가 있으면 문제가 생김(이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성되나, 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러가 발생)
-- DEFAULT 'no address' (디폴트 값 추가) => 기존 데이터들의 address 컬럼값은 'no address'가 됨

ALTER TABLE new_contacts DROP COLUMN address; -- 컬럼 삭제
-- 삭제하지 못하는 경우 3가지
-- 컬럼이 다른 부분에서 참조되는 경우
-- PRIMARY KEY인 경우
-- UNIQUE 제약 조건이 있는 경우

-- DROP TABLE : 데이터베이스에서 테이블 삭제
DROP TABLE new_contacts;
-- 존재하지 않는 테이블 지우면 오류 발생
-- 한 번에 하나의 테이블만 삭제 가능(여러번 쓰면 되지)
-- 삭제하면 실행취소나 복구 못함
