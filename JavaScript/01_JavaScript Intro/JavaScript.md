* JavaScript 시작하기
* JavaScript 기초 문법 1
* 함수
* Array와 Object



가. JavaScript 시작하기

1. JavaScript 배워야 하는 이유

   가) 웹 기술의 기반이 되는 언어(HTML 문서의 콘텐츠를 동적으로 변경할 수 있음)

   나) 다양한 분야로 확장이 가능한 언어(웹을 넘어 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그래밍, 블록체인, 게임 개발 등)

2. JavaScript의 역사

   가) 웹을 조작하기 위한 언어인 만큼 “웹 브라우저”와도 깊은 연관 관계가 있음

   나) 웹 브라우저의 역할

   * URL을 통해 Web(WWW)을 탐색함
   * HTML/CSS/JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
   * 웹 서비스 이용 시 클라이언트의 역할을 함
   * 즉, 웹 페이지 코드를 이해하고, 보여주는 역할을 하는 것이 바로 웹 브라우저

   다) 웹 브라우저와 스크립트 언어

   * 웹 브라우저는 자바스크립트를 해석하는 엔진을 가지고 있음
   * 현재의 자바스크립트는 이제 시장에서 자리를 잡은 언어이며, 개발에서 큰 축을 담당하는 언어
   * 더이상 jQuery 등의 라이브러리를 사용할 필요가 없음(모든 웹 브라우저가 표준안을 따름)
   * 특히, 크롬의 V8의 경우 자바스크립트를 번역하는 속도가 매우 빠름
     * 웹 브라우저에서만 사용하지 말고 다른 개발에서도 활용해보자!
     * 자바스크립트를 밖으로 빼줌, 다른 영역에서의 활용(node.js / react.js), 웹 브라우저를 넘어 서버쪽까지 활용할 수 있음

3. JavaScript 실행환경 구성

   가) Web Browser로 실행하기 : Web Browser에는 JavaScript를 해석할 수 있는 엔진이 있어 실행할 수 있음 / 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 Vanilla JavaScript라고 부름

   * HTML 파일에 포함시키기 : HTML 파일에 직접 JavaScript를 작성 후 웹 브라우저로 파일 열기
   * 외부 JavaScript 파일 사용하기
   * Web Browser의 console에서 바로 입력하기
   
   나) Node.js로 실행하기 : 웹 브라우저를 이용하지 않고 JavaScript를 실행할 수 있음(엔진이 있으니까)
   
   ```bash
   설치 확인
   node -v
   npm -v
   
   파일 실행
   node hello.js
   ```

나. JavaScript 기초 문법 (mdn 참조)

1. 코드 작성법

   가) 세미콜론

   * 자바스크립트는 세미콜론을 선택적으로 사용 가능
   * 없어도 ASI에 의해 자동으로 세미콜론이 삽입됨
   * 안 쓰는 것이 추세

   나) 들여쓰기와 코드 블럭

   * 파이썬은 4칸 들여쓰기 사용, 자바스크립트는 2칸 들여쓰기 사용
   * 블럭은 중괄호 { } 를 사용해 코드 블럭을 구분

   다) 코드 스타일 가이드 : Airbnb Style Guide 참조

   라) 주석 : 한 줄 주석(//), 여러 줄 주석(/* */), ctrl + /

2. 변수와 식별자

   가) 식별자는 변수를 구분할 수 있는 변수명을 말함

   나) 식별자는 반드시 문자, 달러 또는 밑줄로 시작

   다) 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

   라) 예약어 사용 불가능 : for, if, function 등

   마) 방법

   * 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용
   * 파스칼 케이스(PascalCase) : 클래스, 생성자에 사용
   * 대문자 스네이크 케이스(SNAKE_CASE) : 상수에 사용, 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미, 재할당 안하는 경우

   바) 변수 선언 키워드

   * let : 블록 스코프 지역 변수를 선언(추가로 동시에 값을 초기화)

     * 재할당 가능 & 재선언 불가능

       ```javascript
       let number = 20 // 1. 선언 및 초기값 할당
       number = 20 // 2. 재할당
       
       let number = 10 // 1. 선언 및 초기값 할당
       let number = 20 // 2. 재선언 불가능
       ```

   * const : 블록 스코프 읽기 전용 상수를 선언(추가로 동시에 값을 초기화)

     * 재할당 불가능 & 재선언 불가능

       ```javascript
       const number = 10 // 1. 선언 및 초기값 할당
       number = 10 // 2. 재할당 불가능
       
       const number = 10 // 1. 선언 및 초기값 할당
       const number = 20 // 2. 재선언 불가능
       
       // 선언 시 반드시 초기값을 설정해야 하며, 이후 값 변경이 불가능

   * var : 변수를 선언(추가로 동시에 값을 초기화)

     * 재할당 가능 & 재선언 가능
     * "호이스팅" 되는 특성으로 인해 예기치 못한 문제 발생 가능
     * ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
     * 함수 스코프를 가짐

     cf) 선언, 할당, 초기화

     * 선언 : 변수를 생성하는 행위 또는 시점, 값을 지정하지 않은 것
     * 할당 : 선언된 변수에 값을 저장하는 행위 또는 시점, 값 저장
     * 초기화 : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점, 선언+할당

     cf) 블록 스코프

     * if, for, 함수 등의 중괄호({}) 내부를 가리킴
     * 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

     cf) 함수 스코프

     * 함수의 중괄호 내부를 가리킴
     * 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

     cf) 호이스팅

     * 변수를 선언 이전에 참조할 수 있는 현상

     * var로 선언된 변수는 선언 이전에 참조할 수 있으며, 이러한 현상을 호이스팅이라 함

     * 변수 선언 이전의 위치에서 접근 시 undefined를 반환

       ```javascript
       console.log(name) // undefined => 선언 이전에 참조
       var name = '홍길동' // 선언
       
       // 위 코드를 암묵적으로 아래와 같이 이해함
       var name // undefined로 초기화
       console.log(name)
       var name = '홍길동'
       ```

     * 즉, JavaScript에서 변수들은 실제 실행시에 코드의 최상단으로 끌어 올려지게 되며 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 일어남

     * 반면 let, const는 호이스팅이 일어나면 에러를 발생시킴

     * 변수를 선언하기 전에 접근이 가능한 것은 코드의 논리적인 흐름을 깨뜨리는 행위이며 이러한 것을 방지하기 위해 let, const가 추가되었음 (즉, var는 사용하지 않아야 하는 키워드!!)

     | 키워드 | 재선언 | 재할당 | 스코프      | 비고                    |
     | ------ | ------ | ------ | ----------- | ----------------------- |
     | let    | X      | O      | 블록 스코프 | ES6부터 도입            |
     | const  | X      | X      | 블록 스코프 | 블록 스코프ES6부터 도입 |
     | var    | O      | O      | 함수 스코프 | 사용X                   |

   * const를 기본으로 사용하고 재할당이 필요한 경우 let 사용(for문 사용시)

3. 데이터 타입

   가) 원시 타입 : Number, String, Boolean, undefined, null, Symbol

   * Number : 정수 또는 실수형 숫자를 표현하는 자료형

     * NaN : Not-A-Number(숫자가 아님)를 나타냄

     * Number.isNaN()의 경우 주어진 값이 유형이 Number이고 값이 NaN이면 true, 아니면 false를 반환

       ```javascript
       Number.isNaN(NaN) // true
       Number.isNaN(0 / 0) // true
       
       Number.isNaN('NaN') // false
       Number.isNaN(undefined) // false
       Number.isNaN({}) // false
       Number.isNaN('blabla') // false
       ```

     * NaN을 반환하는 경우

       * 숫자로서 읽을 수 없음(parseInt("어쩌구"), Number(undefined))
       * 결과가 허수인 수학 계산식(Math.sqrt(-1))
       * 피연산자가 NaN(7**NaN)
       * 정의할 수 없는 계산식(0*Infinity)
       * 문자열을 포함하면서 덧셈이 아닌 계산식("가" / 3)

   * String

     * 작은 따옴표로 많이 씀

     * 곱셈, 나눗셈, 뺄셈을 안되지만 덧셈을 통해 문자열 붙일 수 있음.

       ```javascript
       별찍기
       console.log('*'.repeat(1))
       console.log('*'.repeat(2))
       console.log('*'.repeat(3))
       console.log('*'.repeat(4))
       console.log('*'.repeat(5))
       ```

     * Quote를 사용하면 선언 시 줄 바꿈이 안됨

     * 대신 escape sequence를 사용할 수 있기 때문에 \n를 사용해야 함

     * `Template Literal` 파이썬의 f-string과 같음

       * 백틱(``)과 ${  } 사용

         ```javascript
         const age = 10
         const message = `홍길동은 ${age}세입니다.`
         ```

     * Empty Value : 값이 존재하지 않음을 표현하는 값

       * null : 개발자가 변수의 값이 없음을 의도적으로 표현할 때, 타입이 객체(Object)!!(실수로 인해..)
       * undefined : 값이 정의되어 있지 않음을 표현하는 값, 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨, 타입은 undefined

   * Boolean : true, false

     * 자동 형변환 규칙 

       | 데이터 타입 | false      | true             |
       | ----------- | ---------- | ---------------- |
       | undefined   | 항상 false | X                |
       | null        | 항상 false | X                |
       | Number      | 0, -0, NaN | 나머지 모든 경우 |
       | String      | 빈 문자열  | 나머지 모든 경우 |
       | Object      | X          | 항상 true        |

   나) 참조 타입 : Objects, Array, Function, ...

4. 연산자

   가) 할당 연산자(+=, -=, *=)

   나) 비교 연산자(<, >)

   * 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

     * 알파벳 순서상 후순위가 더 크다

     * 소문자>대문자

   다) 동등 연산자(==) : 비교할 때 암묵적 타입 변환 통해 타입을 일치시킨 후 같은 값인지 비교(1=='1'는 true), 특별한 경우 제외하고 사용하지 않음

   라) 일치 연산자(===) : 암묵적 타입 변환이 발생하지 않음(1==='1'는 false), 이걸 사용함!!

   마) 논리 연산자 : &&, ||, !, 단축평가 지원

   바) 삼항 연산자

   * 가장 앞의 조건식이 참이면 :(콜론) 앞의 값이 반환되며, 그 반대일 경우 : 뒤의 값이 반환되는 연산자
     * 조건식 ? (참) : (거짓)

5. 조건문

   가) if, else if, else

   * 조건은 소괄호 안에 작성
   * 실행할 코드는 중괄호 안에 작성
   * 블록 스코프 생성

   나) switch : 조건이 많은 경우 switch 사용하면 가독성 향상

   * break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

   * 블록 스코프 생성

     ```javascript
     switch(expression) {
         case 'first value': {
             // do something
             [break]
         }
         case 'second value': {
             // do something
             [break]
         }
         [default: {
         	// do something 
         }]
     }
     ```

6. 반복문 : while, for, for...in, for...of

   가) while

   ```javascript
   while (조건문) {
       // do something
   }
   ```

   나) for

   ```javascript
   for ([초기문]; [조건문]; [증감문]) {
       // do something
   }
   
   for (let i = 0; i < 6; i++) {
       console.log(i)
   }
   // 0, 1, 2, 3, 4, 5
   ```

   다) for...in

   * 객체(object)의 속성을 순회할 때 사용

   * 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

     ```javascript
     const fruits = {a:'apple', b:'banana'}
     
     for (const fruit in fruits) {
         console.log(key) // a, b
         console.log(fruits[key]) // apple, banana
     }
     ```

   라) for...of

   * 반복 가능한 객체를 순회할 때 사용

   * 반복 가능한(iterable) 객체의 종류 : Array, Set, String 등

     ```javascript
     const numbers = [0, 1, 2, 3]
     
     for (const number of numbers) {
         console.log(number) // 0, 1, 2, 3
     }
     ```

   마) for...in과 for...of 차이

   * for...in은 "속성 이름"을 통해 반복

   * for...of는 "속성 값"을 통해 반복

     ```javascript
     const arr = [3, 5, 7]
     
     for (const i in arr) {
         console.log(i) // 0 1 2
     }
     // 딕셔너리와 같은 "객체" 순회에 적합
     
     for (const i of arr) {
         console.log(i) // 3 5 7
     }
     // Iterable 순회에 적합
     ```

   cf) for와 let / for...in, for...of와 const

   * for : for의 경우에는 최초 정의한 i를 재할당하면서 사용하기 때문에 const를 사용하면 "에러 발생"
   * for...in, for...of : 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음

   | 키워드   | 종류   | 연관 키워드          | 스코프      |
   | -------- | ------ | -------------------- | ----------- |
   | if       | 조건문 | -                    | 블록 스코프 |
   | switch   | 조건문 | case, break, default | 블록 스코프 |
   | while    | 반복문 | break, continue      | 블록 스코프 |
   | for      | 반복문 | break, continue      | 블록 스코프 |
   | for...in | 반복문 | 객체 순회            | 블록 스코프 |
   | for...of | 반복문 | Iterable 순회        | 블록 스코프 |

   

