<template>
  <section class="text-gray-600 body-font overflow-hidden">
    <div class="container px-5 py-5 mx-auto">
      <div class="flex justify-center" >
        <a class="mb-10 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-8 focus:outline-none rounded text-lg">
          <router-link :to="`/todo-add`">Add Todo</router-link>
        </a>
      </div>
      <div class="-my-8 divide-y-2 divide-gray-100">
        <div v-for="todo in todos" class="py-8 flex flex-wrap md:flex-nowrap">
          <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
            <span class="font-semibold title-font text-gray-700">CATEGORY</span>
            <span>
              <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                {{ format_date(todo.created_date) }}
              </h2>
            </span>
            <span class="mt-5 flex justify-center text-lg">
              <p class="py-2 px-6 rounded text-red-500 bg-red-50" v-if="todo.is_done==true">
                Done
              </p>
              <p class="py-2 px-6 rounded text-red-500 bg-red-50" v-if="todo.is_done==false">
                Todo
              </p>
            </span>
          </div>
          <div class="md:flex-grow">
            <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
              {{todo.title}}
            </h2>
            <p class="leading-relaxed">
              {{todo.detail}}
            </p>
            <div class="flex justify-end mt-2">
              <button class="inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                <router-link :to="`/todo/${todo.id}/`">Edit</router-link>
              </button>
              <button v-on:click="delete_todo(todo.id)" class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-500 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                Delete
              </button>
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
  name: 'Todo',
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
            url: 'http://127.0.0.1:8000/api/todo/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.todos= response.data);
    },
    delete_todo(id) {
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/api/todo/' + id + '/',
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.get_todos());
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY, HH:mm:ss')
      }
    },
  }
}
</script>
