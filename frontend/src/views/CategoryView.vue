<template>
  <section class="text-gray-400 bg-gray-900 body-font overflow-hidden">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-wrap -m-12">
        <div v-for="category in categories.results" class="p-12 md:w-1/2 flex flex-col items-start">
          <span class="inline-block py-1 px-2 rounded bg-gray-800 text-gray-400 text-opacity-75 text-xs font-medium tracking-widest">
            {{ format_date(category.created_date) }}
          </span>
          <h2 class="sm:text-3xl text-2xl title-font font-medium text-white mt-4 mb-4">
            {{ category.title }}
          </h2>
          <p class="leading-relaxed mb-8">
            {{ category.detail }}  
          </p>
          <div class="flex items-center flex-wrap pb-4 mb-4 border-b-2 border-gray-800 border-opacity-75 mt-auto w-full">
            <a class="text-blue-400 inline-flex items-center">
              <router-link :to="`/${id}`">Learn More</router-link>
              <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 12h14"></path>
                <path d="M12 5l7 7-7 7"></path>
              </svg>
            </a>
            <span class="text-gray-500 mr-3 inline-flex items-center ml-auto leading-none text-sm pr-3 py-1 border-r-2 border-gray-800">
              <span class="inline-block py-1 px-2 rounded bg-gray-800 text-gray-400 text-opacity-75 text-xs font-medium tracking-widest">
                Todo 5
              </span>
            </span>
            <span class="text-gray-500 inline-flex items-center leading-none text-sm">
              <span class="inline-block py-1 px-2 rounded bg-gray-800 text-gray-400 text-opacity-75 text-xs font-medium tracking-widest">
                Done 10
              </span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'Category',
  data () {
    return {
      categories: [] 
    }
  },
  mounted () { 
    this.get_categories();
  },
  methods: {
    get_categories() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/category/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.categories= response.data);
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY')
      }
    },
  }
}
</script>
