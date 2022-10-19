// 배열 메서드 심화
// 공통적인 특징은 "순회"
// 메서드 호출 시 인자로 "callback 함수"를 받는 것이 특징
// callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

// 1.
const colors = ['red', 'blue', 'green']

// const printClr = function (color) {
//   console.log(color)
// }

// colors.forEach(printClr) // colors를 foreach(순회)하겠다, printClr가 콜백함수

// 2. 파이썬의 map과 비슷, 순회하며 콜백함수를 적용하겠다.
// colors.forEach(function (color) {
//   console.log(color)
// })

// 3. function 빼면서 화살표 추가
colors.forEach((color) => {
  console.log(color)
})

// 배열을 순회할 때 3가지
// for loop
// for of : break, continue 사용해야할 때
// forEach : 이걸 1순위!