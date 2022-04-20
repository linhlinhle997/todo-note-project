<template>
<section class="text-gray-600 body-font relative">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-col text-center w-full mb-12">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Edit Category</h1>
    </div>
    <div class="lg:w-1/2 md:w-2/3 mx-auto">
      <div class="flex flex-wrap -m-2">
        <div class="p-2 w-full">
          <div class="relative">
            <label for="name" class="leading-7 text-sm text-gray-600">Title</label>
            <input value="{category_detail.title}" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>
        <div class="p-2 w-full">
          <div class="relative">
            <label for="message" class="leading-7 text-sm text-gray-600">Detail</label>
            <textarea id="message" name="message" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
          </div>
        </div>
        <div class="p-2 w-full">
          <button class="flex mx-auto hover:text-blue-50 hover:bg-blue-500 text-blue-500 bg-blue-50 border-0 py-2 px-8 focus:outline-none rounded text-lg">Save</button>
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
  name: 'Category Detail',
  data () {
    return {
      category_detail: [],
    }
  },
  mounted () {
    this.get_category();
  },
  methods: {
    get_category() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/category/' + this.$route.params.id + '/',
        auth: {
          username: 'admin',
          password: 'admin@123'
        }
      }).then(response => this.category_detail= response.data);
    },
    format_date(value){
      if (value) {
        return moment(String(value)).format('DD/MM/YYYY')
      }
    },
  }
}
</script>