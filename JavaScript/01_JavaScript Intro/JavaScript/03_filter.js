// filter : map + true(참인 값만)

const products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

const fruitFilter = function (product) {
  return product.type === 'fruit' // 일치연산자
}

const newArry = products.filter(fruitFilter)

console.log(newArry)

// 2.
const newArry = products.filter(function (product) {
  return product.type === 'fruit'
})

// 3.
const newArry = products.filter((product) => {
  return product.type === 'fruit'
})