// console.log('hello, javascript')

// 함수 선언식
// function add(num1, num2) {
//   return num1 + num2 
// }

// console.log(add(2, 7))

// 함수 표현식 : 익명함수 사용
// const sub = function (num1, num2) {
//   return num1 - num2
// }

// console.log(sub(2, 7))

// 기본인자 사용
// const greeting = function (name = 'Anonymous') {
//   return `Hi ${name}`  
// }

// console.log(greeting())
// 매개변수보다 인자의 개수가 많아도 적어도 출력 됨

// Spread syntax(...)
// 전개구문
// 1. 배열과의 사용
// 2. 함수와의 사용 : 가변인자와 같은 거.. 없으면 빈배열 혹은 2개이상이면 리스트로 받음

// 함수 선언식, 함수 표현식 모두 타입은 function 
// 함수 선언식은 호이스팅이 발생 (함수 호출 이후에 선언해도 동작)
// 함수 표현식은 호이스팅 발생하지 않음 (변수로 평가되어 변수의 scope 규칙을 따름) 이걸 사용!

// 화살표 함수(Arrow Function) : 항상 익명함수, 표현식에서만 사용가능
// 1. function 키워드 생략
// 2. 함수의 매개변수가 하나뿐이라면 '()'도 생략 가능
// 3. 함수의 내용이 한 줄이라면 '{}'와 'return'도 생략 가능
// const greeting = function (name) {
//   return `Hi ${name}`  
// }

// 1단계 가장 많음!
// const greeting = (name) => { // 여기서 화살표를 넣어줘야 해
//   return `Hi ${name}`  
// }
// 인자가 없다면 () or _ 로 표시

// 2단계 권장하지 않음
// const greeting = name => {
//   return `Hi ${name}`  
// }
// object를 return한다면 return을 명시적으로 적어준다.

// 3단계 소괄호 치는 것을 권장 (name)
// const greeting = name => `Hi ${name}`  
// return을 적지 않으려면 괄호를 붙어야 한다.

// 즉시 실행 함수
// 선언되자마자 실행되는 함수, 다시 같은 함수를 다시 호출할 수 없음, 일회성 함수이므로 익명함수로 사용하는 것이 일반적
// ((num) =>  num ** 3)(2) // 소괄호에 넣어 


// Array Object
// 자바스크립트의 데이터 타입 중 참조 타입에 해당하는 타입은 array와 object이며, 객체라고도 말함

// Array
// 키와 속성들을 담고 있는 참조 타입의 객체
// 순서 보장
// 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
// 음의 정수 인덱스는 array.length 형태로 접근 가능
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1]) // undefined
console.log(numbers.length)
console.log(numbers[numbers.length-1]) // 5, 인덱스에 넣어줘야지

// 배열 메서드 기초
numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1)) // 특정값이 존재하는지 판별 후 반환
console.log(numbers.includes(100))

console.log(numbers.indexOf(3)) // 2, 가장 첫번째 요소의 인덱스 반환
console.log(numbers.indexOf(100)) // -1, 없으면 -1 반환

console.log(numbers.join()) // 쉼표 있음
console.log(numbers.join('')) // 쉼표 없어짐
console.log(numbers.join(' ')) // 공백 들어감
console.log(numbers.join('-')) // -들어감


// function palindrome(str) {
//     console.log(str === str.split('').reverse().join(''))
//   }
  
//   palindrome('level') // => true
//   palindrome('hi') // => false

// .split('') : 문자열을 나눠서 리스트에 넣어줌 / 파이썬에서는 split()쓰면 띄어쓰기에 구분에 따라 나뉘어짐(split('')은 오류) , list('level')과 같은 결과임
// .reverse() : '배열'을 뒤집어줌
// .join('') : 작은 따옴표 있어야만 쉼표 없이 합쳐짐
