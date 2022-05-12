<template>
  <section class="text-blue-500 body-font relative">
    <div class="container px-5 py-5 mx-auto">
      <div class="flex justify-start pb-5">
        <router-link tag="button" :to="`/category`" class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-5 inline-flex items-center focus:outline-none rounded text-md">
          <svg width="30" height="30" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
          </svg>
        </router-link>
      </div>
      <div class="flex flex-col text-center w-full">
        <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-blue-500">Edit Category</h1>
      </div>
      <form v-on:submit.prevent="update_category()">
        <div class="lg:w-1/2 md:w-2/3 mx-auto">
          <div class="flex flex-wrap -m-2">
            <div class="p-2 w-full">
              <div class="relative">
                <label for="title" class="leading-7 text-sm text-blue-500">Title</label>
                <input v-model="category_detail.title" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="description" class="leading-7 text-sm text-blue-500">Description</label>
                <textarea v-model="category_detail.description" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
              </div>
            </div>
            <div class="p-2 w-full">
              <div class="relative">
                <label for="create_date" class="leading-7 text-sm text-blue-500">Create date</label>
                <Datepicker v-model="category_detail.created_date" enableSeconds disabled/>
              </div>
            </div>
          </div>
          <div class="text-red-500 pt-3">
            <div v-for="value, key in error" >
              <div v-if="key!='detail'" v-for="text in value">
                * {{format_key(key)}}: {{text}} <br>
              </div>
              <div v-else>
                * {{format_key(key)}}: {{value}} <br>
              </div>
            </div>
          </div>
          <div class="flex justify-center mt-5">
              <button type="submit" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
                Save
              </button>
              <router-link tag="button" to="/category" class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-lg">
                Cancel
              </router-link>
          </div>
        </div>
      </form>
    </div>
  </section>
</template>
<script>
  import axios from 'axios'
  import moment from 'moment'
  import Datepicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css'
  import { ref } from 'vue';

  export default {
    name: 'Category Edit',
    created () {
      document.title = "Edit Category";
    },
    data () {
      return {
        category_detail: {},
        date: null,
        error: null,
        changeKey: null,
      }
    },
    mounted () {
      this.get_category();
    },
    components: { Datepicker },
    setup() {
      const date = ref(new Date());
      return {
        date,
      }
    },
    methods: {
      get_category() {
        axios({
          method: 'get',
          url: '/api/category/' + this.$route.params.categoryId + '/',
          headers: {
            Authorization: 'Token' + ' ' + this.$store.state.setUser.token
          },
        }).then(response => this.category_detail= response.data)
        .catch(err => console.log(this.error = err.response.data));
      },
      update_category() {
        axios({
          method: 'put',
          url: '/api/category/' + this.$route.params.categoryId + '/',
          data: this.category_detail,
          headers: {
            Authorization: 'Token' + ' ' + this.$store.state.setUser.token
          },
        }).then(response => {
          this.category_detail= response.data;
          this.$router.go(-1);
        }).catch(err => console.log(this.error = err.response.data));
      },
      format_date(value){
        if (value) {
          return moment(String(value)).format('DD/MM/YYYY, hh:mm:ss')
        }
      },
      format_key(key) {
        if(key == 'title')
          return this.changeKey = 'Title';
        if(key == 'description')
          return this.changeKey = 'Description';
        if(key == 'created_date')
          return this.changeKey = 'Create date';
        if(key == 'detail')
          return this.changeKey = 'Authentication';
      },
    }
  }
</script>