import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// vuex의 핵심 컨셉 4가지
export default new Vuex.Store({
  state: {
    // state
    //  중양에서 관리하는 모든 상태 정보
    //  $store.state로 접근 가능
    //  store의 state에 message 데이터 정의
    //  Vue 개발자 도구에서의 Vuex, 관리 화면을 Vuex로 변경, 관리 되고 있는 state 확인 가능
    message: 'message in store'
  },
  getters: {
    // state를 활용하기에 첫번째 인자는 state, 두번째 인자는 getters
    messageLength(state) {
      return state.message.length 
    },

    // messageLength를 이용해서 새로운 값을 계산
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    // state를 변경하는 유일한 방법
    CHANGE_MESSAGE(state, newMessage) { // state를 바꿔줘야 하기에 state로 작성, 이름 명시적 구분 위해 대문자로 작성
      // 첫 번째 인자는 state, 두 번째 인자는 payload
      
      // console.log(state)
      // console.log(newMessage)
      state.message = newMessage
    }
  },
  actions: {
    // state를 변경할 수 있는 mutations 호출
    // component에서 dispatch()에 의해 호출됨
    changeMessage(context, newMessage) { 
      // actions의 첫 번째 인자는 context
      //  context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
      //  dispatch()를 사용해 다른 actions도 호출할 수 있음
      //  단, actions에서 state를 직접 조작하는 것은 삼가야 함
      // actions의 두 번째 인자는 payload
      //  넘겨준 데이터를 받아서 사용 

      // console.log(context)
      // console.log(newMessage)
      context.commit('CHANGE_MESSAGE', newMessage)
      // context.commit('mutation 메서드 이름', 추가데이터)
    }
  },
  modules: {
  }
})
