<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-5 mx-auto">
      <div class="grid grid-cols-3">
        <div></div>
        <div class="flex justify-between col-span-2">
          <div class="pr-5 flex justify-start relative lg:w-full xl:w-1/2 md:w-full text-left">
            <input @input="searchCategories()" v-model="search" type="text" placeholder="Search category..." class="w-full bg-gray-100 bg-opacity-50 rounded focus:ring-2 focus:ring-blue-200 focus:bg-transparent border border-gray-300 focus:border-blue-500 text-md outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
          <router-link :to="`/category-add`" tag="button" class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-5 focus:outline-none rounded text-md">
            <svg width="30" height="30" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
              <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
            </svg>
          </router-link>
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
                <h2 class="mb-1 inline-block py-1 px-2 mr-5 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(category.created_date) }}
                </h2>
                <div class="inline-block mb-1 py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  <span class="inline-flex items-center text-blue-500">
                    <svg width="16" height="16" fill="currentColor" class="bi bi-activity" viewBox="0 0 16 16">
                      <path fill-rule="evenodd" d="M6 2a.5.5 0 0 1 .47.33L10 12.036l1.53-4.208A.5.5 0 0 1 12 7.5h3.5a.5.5 0 0 1 0 1h-3.15l-1.88 5.17a.5.5 0 0 1-.94 0L6 3.964 4.47 8.171A.5.5 0 0 1 4 8.5H.5a.5.5 0 0 1 0-1h3.15l1.88-5.17A.5.5 0 0 1 6 2Z"/>
                    </svg>
                    {{count_Status(category.todos, false)}}
                    &nbsp;
                  </span>
                  <span class="inline-flex items-center text-gray-700">
                    <svg width="16" height="16" fill="currentColor" class="bi bi-check-lg" viewBox="0 0 16 16">
                      <path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/>
                    </svg>
                    {{count_Status(category.todos, true)}}
                  </span>
                </div>
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
                    <svg width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                      <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                    </svg>
                  </router-link>
                </span>
                <span class="text-gray-400 inline-flex items-center leading-none text-sm">
                  <button v-on:click="delete_category(category.id)" class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 inline-block py-2 px-6 rounded text-opacity-75 text-xs font-medium tracking-widest">
                    <svg width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                      <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                    </svg>
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
        }).then(response => this.categories= response.data);
    },
    delete_category(id) {
      axios({
        method: 'delete',
        url: '/api/category/' + id + '/',
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