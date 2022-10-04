CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 가. Simple query
-- SELECT 문을 사용하여 간단하게 단일 테이블에서 데이터 조회하기
-- 다양한 절과 함께 사용할 수 있으며 SELECT문은 SQLite에서 가장 복잡한 문
-- ORDER BY, DISTINCT, WHERE, LIMIT, LIKE, GROUP BY

-- 이름과 나이 조회하기
SELECT first_name, age FROM users;

-- 전체 데이터 조회하기(그러나, rowid는 나오지 않음)
SELECT * FROM users;

-- rowid 조회
SELECT rowid, first_name FROM users;

-- 나. Sorting rows
-- ORDER BY

-- 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT first_name, age FROM users
ORDER BY age ASC; -- ASC 써도 되고 안 써도 되고

-- 이름과 나이를 나이가 많은 순서대로 조회하기
SELECT first_name, age FROM users
ORDER BY age DESC; -- 내림차순

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;
-- NULL이 껴있다면 가장 작은 값으로 취급(ASC에서는 시작할 때 출력)

-- 다. Filtering data : 중복제거, 조건설정
-- Clause : SELECT DISTINCT, WHERE, LIMIT
-- Operator : LIKE, IN, BETWEEN

-- SELECT DISTINCT : 중복제거
-- 모든 지역 조회하기
SELECT country FROM users;

-- 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;

-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users
ORDER BY country;

-- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users;
-- 두 개가 세트가 되어서 중복되는 거 제거

-- 이름과 지역 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users
ORDER BY country;
-- NULL값이 여러가지라면 하나만 남긴다


-- WHERE : 조건설정 (나중에 UPDATE, DELETE문에서도 사용)
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;


-- LIKE : 패턴 일치를 기반으로 데이터 조회 / SELECT, UPDATE, DELETE 문의 WHERE 절에서 사용
-- 와일드카드
-- % : 0개 이상의 문자가 올 수 있음 (영% : 영, 영미 등)
-- _ : 1개 문자가 있음을 의미 (영_ : 영미 등) 무조건 채워줘야 함
-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name FROM users
WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';

-- 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age LIKE '2_';

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';


-- IN : 일치여부 확인
-- 부정하려면 NOT IN 사용
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');
-- OR로도 가능
SELECT first_name, country FROM users
WHERE country = '경기도' OR country = '강원도';

-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');


-- BETWEEN : 범위에 있는지 테스트
-- SELECT, DELETE, UPDATE문의 WHERE절에서 사용 가능
-- 부정하려면 NOT BETWEEN 사용
-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age BETWEEN 20 AND 30;
-- AND로도 가능
SELECT first_name, age FROM users
WHERE age >= 20 AND age <= 30;

-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 AND 30;
-- OR로도 가능
SELECT first_name, age FROM users
WHERE age < 20 or age > 30;


-- LIMIT : 결과에서 행 수 제한
-- SELECT문에서 선택적으로 사용
-- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10;

-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users 
ORDER BY balance DESC LIMIT 10; -- 정렬 후 10개의 행을 가져옴

-- 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age FROM users
ORDER BY age LIMIT 5;


-- OFFSET : OFFSET을 사용하면 특정 지정된 위치에서부터 데이터 조회 가능
-- OFFSET 10 하면, 11부터 20을 가져올 수 있음
-- 11번째부터 20번째 데이터의 rowid와 이름 조회하기
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

-- 라. Grouping data
-- 지역을 조회한 후 GROUP화, GROUP의 결과를 COUNT함(무언가를 집계할 때 사용)
-- SELECT문에서 사용 가능, SELECT문의 FROM절 뒤에 작성(WHERE절이 포함된 경우 WHERE절 뒤에 작성해야 함)
-- AVG(), COUNT(), MAX(), MIN(), SUM()
-- 숫자를 기준으로 계산되어져야 하기 때문에 반드시 데이터 타입이 INTEGER여야 함
-- users 테이블의 전체 행 수 조회하기
SELECT COUNT(*) FROM users;

-- 나이가 30살 이상인 사람들의 평균 나이 조회하기
SELECT AVG(age) FROM users WHERE age >= 30;

-- 각 지역별로 몇 명씩 살고 있는지 조회하기(GROUP BY 사용하기)
-- 각 지역별은 지역 별로 그룹을 나눌 필요가 있음을 의미함
-- country 컬럼으로 그룹화
SELECT country FROM users GROUP BY country;
-- 마지막으로 몇 명씩 사는지 계산하기 위해서 그룹별로 포함되는 데이터의 수를 구함
SELECT country, COUNT(*) FROM users GROUP BY country;
-- 각 지역별로 그룹이 나뉘어졌기 때문에 COUNT(*)는 지역별 데이터 개수를 세게 됨
-- COUNT(*), COUNT(age)를 쓰던 상관없으나 이름만 달라짐 / 그룹화된 country를 기준으로 카운트하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일

-- 각 성씨가 몇 명씩 있는지 조회하기
SELECT last_name, COUNT(*) AS number_of_name FROM users
GROUP BY last_name;
-- AS로 이름 바꿀 수 있음

-- 인원이 가장 많은 성씨 순으로 조회하기
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;

-- 각 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users
GROUP BY country;

-- 마. Changing data
-- 데이터를 삽입, 수정, 삭제하기 (INSERT(CREATE 아님!!), UPDATE, DELETE) 
-- 사전준비 : 새 테이블 생성
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);


-- INSERT : 컬럼목록을 생략하고 쓸 수 있지만 VALUES를 그럼 모두 다 넣어줘야 함
-- 단일 행 삽입
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

-- 여러 행 삽입
INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원');


-- UPDATE : SET과 WHERE와 같이 씀
-- WHERE을 안 쓰면 모든 행에 있는 데이터가 바뀜
-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정하기
UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;


-- DELETE : FROM과 WHERE와 같이 씀
-- 마찬가지로 WHERE 없으면 모든게 삭제됨
-- 5번 데이터 삭제하기
DELETE FROM classmates
WHERE rowid = 5;

-- 삭제된 것 확인하기
SELECT rowid, * FROM classmates;

-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates 
WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates; -- 테이블만 남기고 모두 다 지움