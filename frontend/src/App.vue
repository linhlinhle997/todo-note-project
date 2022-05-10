<template>
  <header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <span class="ml-3 text-xl hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link tag="button" to="/">Todo & Note</router-link>
        </span>
      </a>
      <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
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
      <div class="flex gap-4">
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
        <button v-on:click="logout()" class="inline-flex items-center text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-1 px-3 focus:outline-none rounded text-base mt-4 md:mt-0">
          Logout
          &nbsp;
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
            <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
          </svg>
        </button>
      </div>
    </div>
  </header>
  <router-view/>
</template>

<script>
	import axios from 'axios'

	export default {
		name: 'App',
		data () {
			return {
			}
		},
		mounted () {
      this.logout();
    },
		methods: {
			logout() {
				axios({
					method: 'post',
					url: '/api/logout/',
				}).then(response => {
					this.$router.push('/');
				});
			},
		},
	}
</script>