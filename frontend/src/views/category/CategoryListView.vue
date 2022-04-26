<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-5 mx-auto">
      <div class="flex justify-end">
        <a class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-8 focus:outline-none rounded text-lg">
          <router-link :to="`/category-add`">Add Category</router-link>
        </a>
      </div>
      <div class="flex justify-center mb-10 mt-5 text-2xl font-medium text-gray-900 title-font">
        Category List
      </div>
      <div class="flex flex-wrap -m-4">
        <div v-for="category in categories" class="p-4 md:w-1/3">
          <div class="border-2 border-gray-200 border-opacity-60 rounded-lg overflow-hidden">
            <div class="p-6">
              <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                {{ format_date(category.created_date) }}
              </h2>
              <div class="m-2">
                <router-link :to="`/todo/todo-by-category/${category.id}/`">
                  <h1 class="title-font text-lg font-medium text-gray-900 mb-3">
                    {{ category.title }}
                  </h1>
                  <p class="leading-relaxed mb-3">{{ category.detail }}</p>
                </router-link>
              </div>
              <div class="flex items-center flex-wrap mt-auto w-full">
                <span class="text-gray-400 mr-3 inline-flex items-center lg:ml-auto md:ml-0 ml-auto leading-none text-sm pr-3 py-1">
                  <button class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 inline-block py-2 px-6 rounded text-opacity-75 text-xs font-medium tracking-widest">
                    <router-link :to="`/category/${category.id}/`">Edit</router-link>
                  </button>
                </span>
                <span class="text-gray-400 inline-flex items-center leading-none text-sm">
                  <button v-on:click="delete_category(category.id)" class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-500 inline-block py-2 px-6 rounded text-opacity-75 text-xs font-medium tracking-widest">
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
    }
  },
  mounted () { 
    this.get_categories();
  },
  methods: {
    get_categories() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/api/category/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.categories= response.data);
    },
    delete_category(id) {
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/api/category/' + id + '/',
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.get_categories());
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY, HH:mm:ss')
      }
    },
  }
}
</script>