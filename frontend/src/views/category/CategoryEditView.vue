<template>
<section class="text-blue-500 body-font relative">
  <div class="container px-5 mx-auto">
    <div class="flex justify-start py-5">
      <a class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-8 inline-flex items-center focus:outline-none rounded text-lg">
        <router-link :to="`/category`">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
        </router-link>
      </a>
    </div>
    <div class="flex flex-col text-center w-full">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-blue-500">Edit Category</h1>
    </div>
    <form v-on:submit.prevent="update_category()">
      <div class="lg:w-1/2 md:w-2/3 mx-auto">
        <div class="flex flex-wrap -m-2">
          <div class="p-2 w-full">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-blue-500">Title</label>
              <input v-model="category_detail.title" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="message" class="leading-7 text-sm text-blue-500">Detail</label>
              <textarea v-model="category_detail.detail" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-blue-500">Create date</label>
              <Datepicker v-model="category_detail.created_date" enableSeconds disabled/>
            </div>
          </div>
        </div>
        <div class="flex justify-center mt-8">
            <button type="submit" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
              Save
            </button>
            <button class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-lg">
              <router-link to="/category">Cancel</router-link>
            </button>
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
  name: 'Category Detail',
  data () {
    return {
      category_detail: {},
      date: null,
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
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.category_detail= response.data);
    },
    update_category() {
      axios({
        method: 'put',
        url: '/api/category/' + this.$route.params.categoryId + '/',
        data: this.category_detail,
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => {
        this.category_detail= response.data;
        this.$router.go(-1);
      });
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY, hh:mm:ss')
      }
    },
  }
}
</script>