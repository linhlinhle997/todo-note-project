<template>
  <section class="text-gray-600 body-font overflow-hidden">
    <div class="container px-5 py-5 mx-auto">
      <div class="grid grid-cols-3 pb-5">
        <div></div>
        <div class="flex justify-between col-span-2">
          <div class="pr-5 flex justify-start relative lg:w-full xl:w-1/2 md:w-full text-left">
            <input @input="searchTodos()" v-model="search" type="text" placeholder="Search todo..." class="w-full bg-gray-100 bg-opacity-50 rounded focus:ring-2 focus:ring-blue-200 focus:bg-transparent border border-gray-300 focus:border-blue-500 text-md outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
          <div>
            <router-link tag="button" :to="`/todo-add`" class="hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-5 inline-flex items-center focus:outline-none rounded text-md">
              <svg width="30" height="30" fill="currentColor" class="bi bi-plus" viewBox="0 0 16 16">
                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
              </svg>
            </router-link>
          </div>
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
              <span class="mr-5">
                <h2 class="mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.created_date) }}
                </h2>
              </span>
              <button v-on:click="update_todo(todo.id)" class="mt-5 mb-5 flex justify-center text-lg">
                <span v-if="isDeadline(todo.due_date) == false" class="py-2 px-6 rounded text-blue-500 bg-blue-50 hover:text-blue-50 hover:bg-blue-500" >
                  Todo
                </span>
                <span v-else class="inline-flex items-center py-2 px-6 rounded text-red-500 bg-red-50 hover:text-red-50 hover:bg-red-500">
                  <svg width="15" height="15" fill="currentColor" class="bi bi-alarm" viewBox="0 0 16 16">
                    <path d="M8.5 5.5a.5.5 0 0 0-1 0v3.362l-1.429 2.38a.5.5 0 1 0 .858.515l1.5-2.5A.5.5 0 0 0 8.5 9V5.5z"/>
                    <path d="M6.5 0a.5.5 0 0 0 0 1H7v1.07a7.001 7.001 0 0 0-3.273 12.474l-.602.602a.5.5 0 0 0 .707.708l.746-.746A6.97 6.97 0 0 0 8 16a6.97 6.97 0 0 0 3.422-.892l.746.746a.5.5 0 0 0 .707-.708l-.601-.602A7.001 7.001 0 0 0 9 2.07V1h.5a.5.5 0 0 0 0-1h-3zm1.038 3.018a6.093 6.093 0 0 1 .924 0 6 6 0 1 1-.924 0zM0 3.5c0 .753.333 1.429.86 1.887A8.035 8.035 0 0 1 4.387 1.86 2.5 2.5 0 0 0 0 3.5zM13.5 1c-.753 0-1.429.333-1.887.86a8.035 8.035 0 0 1 3.527 3.527A2.5 2.5 0 0 0 13.5 1z"/>
                  </svg>
                  &nbsp;
                  Todo
                </span>
              </button>
              <span class="mr-5">
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
                  <svg width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                    <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                  </svg>
                </router-link>
                <button v-on:click="delete_todo(todo.id)" class="ml-4 mr-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  <svg width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="py-8 flex flex-wrap md:flex-nowrap">
            <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
              <span class="line-through font-semibold title-font text-gray-700">{{todo.category.title}}</span>
              <span class="mr-5">
                <h2 class="line-through mb-1 inline-block py-1 px-2 rounded text-gray-700 bg-gray-100 text-opacity-75 text-xs font-medium tracking-widest">
                  {{ format_date(todo.created_date) }}
                </h2>
              </span>
              <button v-on:click="update_todo(todo.id)" class="mt-5 mb-5 flex justify-center text-lg">
                <span class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 w-12 h-12 rounded inline-flex items-center justify-center">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="w-6 h-6" viewBox="0 0 24 24">
                    <path d="M20 6L9 17l-5-5"></path>
                  </svg>
                </span>
              </button>
              <span class="mr-5">
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
                  <svg width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                    <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                  </svg>
                </router-link>
                <button v-on:click="delete_todo(todo.id)" class="ml-4 mr-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-sm">
                  <svg width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                  </svg>
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
      todo_detail: {},
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
    async update_todo(id) {
      await axios({
          method:'get',
          url: '/api/todo/' + id + '/',
          auth: {
            username: 'admin',
            password: 'admin@123'
          }
      }).then(response => {
        this.todo_detail = response.data;

        axios({
          method: 'put',
          url: '/api/todo/' + id + '/',
          data: {
            title : this.todo_detail.title,
            detail: this.todo_detail.detail,
            is_done: this.todo_detail.is_done == true ? false : true,
            category: this.todo_detail.category,
            due_date: this.todo_detail.due_date,
          },
          auth: {
            username: 'admin',
            password: 'admin@123'
          }
        }).then(response => this.get_todos());
      });
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
  },
  watch: {
    
  }
}
</script>
