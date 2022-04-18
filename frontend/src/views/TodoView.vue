<template>
  <section class="text-gray-400 bg-gray-900 body-font overflow-hidden">
    <div class="container px-5 py-24 mx-auto">
      <div class="-my-8 divide-y-2 divide-gray-800">
        <div v-for="todo in todos.results" class="py-8 flex flex-wrap md:flex-nowrap">
          <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
            <span class="font-semibold title-font text-white">Todo</span>
            <span class="mt-1 text-gray-500 text-sm">12 Jun 2019</span>
          </div>
          <div class="md:flex-grow">
            <h2 class="text-2xl font-medium text-white title-font mb-2">
              {{ todo.title }}
            </h2>
            <p class="leading-relaxed">
              {{ todo.detail }}
            </p>
            <p class="leading-relaxed mt-3">
              <span class="inline-block py-1 px-2 rounded bg-gray-800 text-gray-400 text-opacity-75 text-xs font-medium tracking-widest">
                {{ format_date(todo.due_date) }}
              </span>
            </p>
          </div>
          <div class="md:w-34">
            <div class="md:ml-auto flex flex-wrap items-center text-base">
              <a class="text-blue-400 mr-5 hover:text-white">
                Edit
              </a>
              <a class="text-blue-400 mr-5 hover:text-white">
                Delete
              </a>
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
      todos: [] 
    }
  },
  mounted () { 
    this.get_todos();
  },
  methods: {
    get_todos() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/category/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.todos= response.data);
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY')
      }
    },
  }
}
</script>
