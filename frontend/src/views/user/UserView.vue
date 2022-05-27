<template>
  <section class="text-gray-600 body-font">
    <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
      <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
        <img class="object-cover object-center rounded" alt="hero" src="../../assets/image.jpg">
      </div>
      <div class="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
        <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-700">{{user.first_name}} {{user.last_name}}</h1>
        <p class="mb-4 leading-relaxed italic">@{{user.username}}</p>
        <p class="mb-8 leading-relaxed text-xl">{{user.email}}</p>
        <div class="flex justify-center">
          <router-link :to="`/user/${$store.state.setUser.user.id}/`" tag="button" class="inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-4 px-10 focus:outline-none rounded text-lg">
            <svg width="20" height="20" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
              <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
            </svg>
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'User',
    components: {},
    data() {
      return {
        user: {},
        error: null,
      }
    },
    mounted () { 
      this.get_user();
    },
    methods: {
      get_user() {
        axios({
          method: 'get',
          url: '/api/user/'+ this.$store.state.setUser.user.id + '/',
          headers: {
            Authorization: 'Token' + ' ' + this.$store.state.setUser.token
          },
          }).then(response => {
            this.user = response.data;
          }).catch(error => console.log(this.error =  error.response.data))
      }
    }
  }
</script>