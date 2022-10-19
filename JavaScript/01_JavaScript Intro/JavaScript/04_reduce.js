// 하나의 '결과값'(총합, 총평균값)을 반환
// acc : 누적변수

const numbers = [90, 80, 70, 100]

// 총합

const sumNum = numbers.reduce(function (result, number) { // result가 acc
  return result + number
}, 0) // 초기값 0
// 두개인자(콜백함수, 초기값)

console.log(sumNum)

// 3.
const sumNum = numbers.reduce((result, number) => { 
  return result + number
}, 0)

// 평균값
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length