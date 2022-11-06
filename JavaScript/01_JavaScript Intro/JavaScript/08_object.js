// 객체(Object) 
// 중괄호 내부에 키와 밸류 쌍으로 표현(딕셔너리 형태)
// 키는 문자열 타입만 가능, key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
// 밸류는 모든 타입(함수포함) 가능
// 접근은 점 혹은 대괄호로 가능 
//  .get()
//  []
// 키 이름에 띄어쓰기가 있으면 대괄호 접근만 가능

// const myInfo = {
//   name: 'jack',
//   phoneNumber: '123456',
//   'samsung product': {
//     buds: 'Buds pro',
//     galaxy: 'S99',
//   },
// }

// console.log(myInfo.name)
// console.log(myInfo['name'])

// console.log(myInfo['samsung product']) // 키 이름에 띄어쓰기 있으므로 점으로 접근 불가능
// console.log(myInfo['samsung product'].galaxy)

// 객체 관련 ES6 문법
// 1. 속성명 축약 : 키와 할당하는 변수의 이름이 같으면 축약 가능
// 2. 메서드명 축약 : 메서드 선언 시 function 키워드 생략 가능
// const obj = {
// 	name: 'jack',
// 	greeting() {
// 		console.log('hi!')
// 	}
// }

// console.log(obj.name)
// console.log(obj.greeting())

// 3. 계산된 속성 : 키 이름이 동적으로 생성 가능
// 대괄호로 표현
// const key = 'country'
// const value = ['한국', '미국']

// const myObj = {
// 	[key]: value,
// }

// console.log(myObj)
// console.log(myObj.country)

// 4. 구조 분해 할당!! (중요!!) : 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
// 중괄호
// const userInformation = {
// 	name: '',
// 	userId: ''
// }
// const { name } = userInformation
// const { userId } = userInformation

// const { name, userId } = userInformation // 이렇게 합쳐서도 가능
// 5. Spread syntax(...)
// 배열과 마찬가지로 객체 내부에서 객체 전개 가능
// 얕은 복사에 활용 가능

// JSON
// 키-밸류 형태로 이루어진 자료 표기법 
// 오브젝트로 보이지만, "문자열"임!
// Object로 사용하기 위해서는 변환 작업이 필요(자바스크립트에서는 오브젝트로 바꿔야 함, 파이썬에서 딕셔너리로 바꿔주듯이)

const jsonData = {
	coffee: 'Americano',
	iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof objToJson) // string

// json -> Object (중요!)
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof jsonToObj) // object
console.log(jsonToObj.coffee) // Americano

// 파이썬에서는 response.json()을 사용해 딕셔너리로 바꿔줌..

// 이 json은 장고가 만들지 -> 그 json을 parse해서 object로 만든 후 vue.js가 받아서 조작
// json은 이렇게 어디든 변환해서 사용할 수 있기 때문에 그래서 json을 사용함! 오..

// 참조 > object > 배열, 함수, 기타
// 배열은 객체다
// 속성값이 있다. (length라는 속성값도 있다. / for in 으로 돌렸을 때 속성값이 출력된다.)

// 정리
// 반복문 : for, while, for in, for of, forEach
// 배열에서는 for, while, for of, forEach 4가지 쓸 수 있다.