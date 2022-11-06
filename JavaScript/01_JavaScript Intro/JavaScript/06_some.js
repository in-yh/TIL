// 하나라도 주어진 판별 함수를 통과하면 true
// 모든 요소가 통과 못하면 false
// 빈 배열이면 false
// or

const arr = [1, 2, 3, 4, 5]

// 1.
// const result = arr.some(function (elem) {
//   return elem % 2 === 0
// })

// 2.
// const result = arr.some((elem) => {
//   return elem % 2 === 0
// })

// 3. 
const result = arr.some((elem) => elem % 2 === 0)
console.log(result)