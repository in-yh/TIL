// 조건을 만족하는 첫번째 요소를 반환
// 찾았는데도 없다면 undefined 반환

const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Thor', age: 40 },
]

const avenger = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})

console.log(avenger)