import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

const store = createStore({
  plugins: [createPersistedState()],
  state: {
    setUser: {},
    authenticated: false,
  },
  mutations: {
    setUser(state, data) {
      state.setUser = (data);
      // console.log("User set in store");
    },
    setAuthenticated(state, data) {
      state.authenticated = data;
      // console.log("Authenticated set in store");
    }
  },
  getters: {},
  actions: {},
})

export default store;