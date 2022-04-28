<template>
  <section class="text-gray-600 body-font overflow-hidden">
    <div class="container px-5 py-5 mx-auto">
            <div class="grid grid-cols-3">
        <div></div>
        <div class="flex justify-between col-span-2">
            <div class="flex justify-start relative lg:w-full xl:w-1/2 md:w-full text-left">
              <input @input="searchTodos()" v-model="search" type="text" placeholder="Search todo..." class="w-full bg-gray-100 bg-opacity-50 rounded focus:ring-2 focus:ring-blue-200 focus:bg-transparent border border-gray-300 focus:border-blue-500 text-md outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          <router-link :to="`/todo-add`" tag="button" class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-8 focus:outline-none rounded text-md">Add Category</router-link>
        </div>
      </div>
      <div class="-my-8 divide-y-2 divide-gray-100 py-5">
        <div class="flex justify-center py-5 text-3xl font-medium text-gray-900 title-font">
          Todo List
        </div>
        <div v-for="todo in todos">
          <div v-if="todo.is_done==false" class="py-8 flex flex-wrap md:flex-nowrap">
            <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
              <span class="font-semibold title-font text-gray-700">{{todo.category.title}}</span>
              <span>
                <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.created_date) }}
                </h2>
              </span>
              <span class="mt-5 mb-5 flex justify-center text-lg">
                <p class="py-2 px-6 rounded text-blue-500 bg-blue-50" v-if="todo.is_done==true">
                  Done
                </p>
                <span v-if="isDeadline(todo.due_date) == false">
                  <p class="py-2 px-6 rounded text-blue-500 bg-blue-50" v-if="todo.is_done==false">
                    Todo
                  </p>
                </span>
                <span v-else>
                  <p class="py-2 px-6 rounded text-red-500 bg-red-50" v-if="todo.is_done==false">
                    Todo is late
                  </p>
                </span>
              </span>
              <span>
                <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.due_date) }}
                </h2>
              </span>
            </div>
            <div class="md:flex-grow">
              <h2 class="text-xl font-medium text-gray-900 title-font mb-2 ">
                {{todo.title}}
              </h2>
              <p class="leading-relaxed">
                {{todo.detail}}
              </p>
              <div class="flex justify-end mt-2">
                <router-link tag="button" :to="`/todo/${todo.id}/`" class="inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  Edit
                </router-link>
                <button v-on:click="delete_todo(todo.id)" class="ml-4 mr-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  Delete
                </button>
              </div>
            </div>
          </div>
          <div v-else class="py-8 flex flex-wrap md:flex-nowrap">
            <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
              <span class="line-through font-semibold title-font text-gray-700">{{todo.category.title}}</span>
              <span>
                <h2 class="line-through mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.created_date) }}
                </h2>
              </span>
              <span class="mt-5 mb-5 flex justify-center text-lg">
                <p class="line-through py-2 px-6 rounded text-gray-700 bg-gray-100" v-if="todo.is_done==true">
                  Done
                </p>
                <p class="line-through py-2 px-6 rounded text-gray-700 bg-gray-100" v-if="todo.is_done==false">
                  Todo
                </p>
              </span>
              <span>
                <h2 class="line-through mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.due_date) }}
                </h2>
              </span>
            </div>
            <div class="md:flex-grow">
              <h2 class="line-through text-2xl font-medium text-gray-900 title-font mb-2 ">
                {{todo.title}}
              </h2>
              <p class="line-through leading-relaxed">
                {{todo.detail}}
              </p>
              <div class="flex justify-end mt-2">
                <router-link tag="button" :to="`/todo/${todo.id}/`" class="inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  Edit
                </router-link>
                <button v-on:click="delete_todo(todo.id)" class="ml-4 mr-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  Delete
                </button>
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
  name: 'Todo',
  data () {
    return {
      todos: [],
      search: '',
    }
  },
  mounted () { 
    this.get_todos();
    this.searchTodos();
  },
  methods: {
    get_todos() {
        axios({
            method:'get',
            url: '/api/todo/',
            auth: {
                username: 'admin',
                password: 'admin@123'
            }
        }).then(response => this.todos= response.data);
    },
    delete_todo(id) {
      axios({
        method: 'delete',
        url: '/api/todo/' + id + '/',
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.get_todos());
    },
    searchTodos() {
      let api_url = '/api/todo/';
      if(this.search!==''||this.search!==null) {
        api_url = `/api/todo/?search=${this.search}`
      }
      axios({
        method:'get',
        url: api_url,
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.todos= response.data);
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY, HH:mm:ss')
      }
    },
    isDeadline(due_date) {
      var date = new Date();
      due_date = new Date(due_date);
      if(date <= due_date){
        return false;
      }else{
        return true;
      }      
    },
  }
}
</script>
