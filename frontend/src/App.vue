<template>
  <header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <span class="ml-3 text-xl hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link tag="button" to="/">Todo & Note</router-link>
        </span>
      </a>
      <nav v-if="$store.state.authenticated==true" class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
        <router-link tag="button" to="/category" class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          Category
        </router-link>
        <router-link tag="button" to="/todo" class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          Todo
        </router-link>
        <!-- <router-link tag="button" to="/note" class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          Note
        </router-link> -->
      </nav>
      <nav v-else class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center"></nav>
      <div v-if="$store.state.authenticated==false" class="flex gap-4">
        <router-link tag="button" to="/signup" class="inline-flex items-center text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-1 px-3 focus:outline-none rounded text-base mt-4 md:mt-0">
          Sign Up
        </router-link>
        <router-link tag="button" to="/login" class="inline-flex items-center text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-1 px-3 focus:outline-none rounded text-base mt-4 md:mt-0">
          Login
          &nbsp;
          <svg width="16" height="16" fill="currentColor" class="bi bi-box-arrow-right" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
            <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
          </svg>
        </router-link>
      </div>
      <div v-else class="flex gap-4">
        <button v-on:click="logout()" class="inline-flex items-center text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-1 px-3 focus:outline-none rounded text-base mt-4 md:mt-0">
          Logout
          &nbsp;
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
            <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
          </svg>
        </button>
        <router-link tag="button" to="/about" class="inline-flex items-center text-blue-500 hover:text-blue-50 bg-blue-50 hover:bg-blue-500 border-0 py-1 px-3 focus:outline-none rounded text-sm mt-4 md:mt-0">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
          </svg>
          @{{$store.state.setUser.user.username}}
        </router-link>
      </div>
    </div>
  </header>
  <router-view/>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'App',
    components: {},
    data() {
      return {
        error: null,
      }
    },
    methods: {
      logout: function () {
        axios({
          method: 'get',
          url: '/api/logout/',
          headers: {
            Authorization: 'Token' + ' ' + this.$store.state.setUser.token
          },
          }).then(response => {
            this.$store.commit('setUser', '');
            this.$store.commit('setAuthenticated', false);
            localStorage.removeItem('vuex');
            this.$router.push('/');
          }).catch(error => console.log(this.error =  error.response.data))
        }
    }
  }
</script>