// 모든 요소가 판별 함수를 통과하면 참
// 하나라도 통과하지 못하면 거짓
// 빈배열 항상 true
// and

const arr = [1, 2, 3, 4, 5]

// 1.
// const result = arr.every(function (elem) {
//   return elem % 2 === 0
// })

// 2.
// const result = arr.every((elem) => {
//   return elem % 2 === 0
// })

// 3.
const result = arr.every((elem) => elem % 2 === 0)
console.log(result)