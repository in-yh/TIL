// 비동기
function slowRequest(callBack) {
  console.log('1. 오래 걸리는 작업 시작 ...')
  setTimeout(function () {  // 3초를 기다리는 함수(오래 걸리는 작업)
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log('2. 콜백함수 실행됨') // 가장 마지막에 출력
}

slowRequest(myCallBack)
console.log('3. 다른 작업 실행')