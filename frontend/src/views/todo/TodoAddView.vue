<template>
	<section class="text-gray-600 body-font relative">
		<div class="container px-5 py-24 mx-auto">
			<div class="flex flex-col text-center w-full">
				<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Add Category</h1>
			</div>
			<div class="lg:w-1/2 md:w-2/3 mx-auto">
				<div class="flex flex-wrap -m-2">
          <div class="p-2 w-full">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-gray-600">Title</label>
              <input v-model="todo.title" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="message" class="leading-7 text-sm text-gray-600">Detail</label>
              <textarea v-model="todo.detail" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label class="leading-7 text-sm text-gray-600" for="flexCheckDefault">
                Done
              </label>
              <input v-model="todo.is_done" class="form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer" type="checkbox">
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label class="leading-7 text-sm text-gray-600" for="flexSelect">
                Category
              </label>
              <select v-model="selected" class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Default select example">
                <option v-for="item in todo.category" :value="item">
                  {{ item.name }}
                </option>
              </select>
            </div>
          </div>
					<div class="p-2 w-full">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-gray-600">Due date</label>
              <Datepicker v-model="due_date" enableSeconds/>
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-gray-600">Create date</label>
              <Datepicker v-model="create_date" enableSeconds/>
            </div>
          </div>
        </div>
				<div class="flex justify-center mt-8">
						<button v-on:click="add_todo()" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
							Save
						</button>
						<button class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
							<router-link to="/todo">Cancel</router-link>
						</button>
				</div>
			</div>
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
		name: 'Todo Detail',
		data () {
			return {
				todo: {},
				create_date: null,
				due_date: null,
			}
		},
		mounted () {},
		components: { Datepicker },
		setup() {
			const create_date = ref(new Date());
			const due_date = ref(new Date());
			return {
				create_date,
				due_date,
			}
		},
		methods: {
			add_todo() {
				axios({
					method: 'post',
					url: 'http://127.0.0.1:8000/api/todo/',
					data: {
						title : this.todo.title,
						detail: this.todo.detail,
						is_done: this.todo.is_done,
						category: this.todo.category,
						due_date: moment(this.due_date).format('YYYY-MM-DDThh:mm:ss'),
						created_date: moment(this.create_date).format('YYYY-MM-DDThh:mm:ss'),
					},
					auth: {
						username: 'admin',
						password: 'admin@123'
					}
				}).then(response => {
					this.todo = response.data;
					this.$router.push({path: '/todo'});
				});
			},
		},
	}
</script>