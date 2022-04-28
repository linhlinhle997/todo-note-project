<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-5 mx-auto">
      <div class="grid grid-cols-3">
        <div></div>
        <div class="flex justify-between col-span-2">
            <div class="flex justify-start relative lg:w-full xl:w-1/2 md:w-full text-left">
              <input @input="searchCategories()" v-model="search" type="text" placeholder="Search category..." class="w-full bg-gray-100 bg-opacity-50 rounded focus:ring-2 focus:ring-blue-200 focus:bg-transparent border border-gray-300 focus:border-blue-500 text-md outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          <router-link :to="`/category-add`" tag="button" class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-8 focus:outline-none rounded text-md">Add Category</router-link>
        </div>
      </div>
      <div class="flex justify-center mb-5 mt-5 text-3xl font-medium text-gray-900 title-font">
        Category List
      </div>
      <div class="flex flex-wrap -m-4">
        <div v-for="category in categories" class="p-4 md:w-1/3">
          <div class="border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
            <div class="p-6">
              <div class="flex justify-between">
                <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(category.created_date) }}
                </h2>
                <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  <span class="text-blue-500">{{count_Status(category.todos, false)}}</span> | <span class="text-gray-700">{{count_Status(category.todos, true)}}</span>
                </h2>
              </div>
              <div class="m-2">
                <router-link tag="button" :to="`/todo/todo-by-category/${category.id}/`">
                  <h1 class="title-font text-lg font-medium text-gray-900 mb-3">
                    {{ category.title }}
                  </h1>
                  <p class="leading-relaxed mb-3">{{ category.detail }}</p>
                </router-link>
              </div>
              <div class="flex items-center flex-wrap mt-auto w-full">
                <span class="text-gray-400 mr-3 inline-flex items-center lg:ml-auto md:ml-0 ml-auto leading-none text-sm pr-3 py-1">
                  <router-link :to="`/category/${category.id}/`" tag="button" class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 inline-block py-2 px-6 rounded text-opacity-75 text-xs font-medium tracking-widest">
                    Edit
                  </router-link>
                </span>
                <span class="text-gray-400 inline-flex items-center leading-none text-sm">
                  <button v-on:click="delete_category(category.id)" class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 inline-block py-2 px-6 rounded text-opacity-75 text-xs font-medium tracking-widest">
                    Delete
                  </button>
                </span>
              </div>
            </div>
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
      categories: [],
      search: '',
    }
  },
  mounted () { 
    this.get_categories();
    this.searchCategories();
  },
  methods: {
    get_categories() {
        axios({
            method:'get',
            url: '/api/category/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.categories= response.data);
    },
    delete_category(id) {
      axios({
        method: 'delete',
        url: '/api/category/' + id + '/',
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.get_categories());
    },
    searchCategories() {
      let api_url = '/api/category/';
      if(this.search!==''||this.search!==null) {
        api_url = `/api/category/?search=${this.search}`
      }
      axios({
        method:'get',
        url: api_url,
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.categories= response.data);
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY, HH:mm:ss')
      }
    },
    count_Status(todos, status) {
      return todos.filter(i => i.is_done==status).length
    },
  }
}
</script>