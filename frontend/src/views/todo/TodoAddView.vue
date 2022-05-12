<template>
	<section class="text-blue-500 body-font relative">
		<div class="container px-5 py-5 mx-auto">
			<div class="flex justify-start pb-5">
				<router-link tag="button" :to="`/todo`" class="text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-5 inline-flex items-center focus:outline-none rounded text-md">
					<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
					</svg>
				</router-link>
			</div>
			<div class="flex flex-col text-center w-full">
				<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-blue-500">Add Todo</h1>
			</div>
			<div class="lg:w-1/2 md:w-2/3 mx-auto">
				<div class="flex flex-wrap -m-2">
          <div class="p-2 w-full">
            <div class="relative">
              <label for="title" class="leading-7 text-sm text-blue-500">Title</label>
              <input v-model="todo.title" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="description" class="leading-7 text-sm text-blue-500">Description</label>
              <textarea v-model="todo.description" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <p class="leading-7 text-sm text-blue-500">Status</p>
              <label for="status" class="leading-7 text-sm text-gray-700">
                Done
              </label>
              <input v-model="todo.is_done" class="form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer" type="checkbox">
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="category" class="leading-7 text-sm text-blue-500">
                Category
              </label>
							<select v-model="selected" class="form-select appearance-none block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Default select example">
								<option v-for="category in categories" :value="category.id">
									{{ category.title }}
								</option>
							</select>
            </div>
          </div>
					<div class="p-2 w-full">
            <div class="relative">
              <label for="due_date" class="leading-7 text-sm text-blue-500">Due date</label>
              <Datepicker v-model="due_date" enableSeconds class="dp__theme_light">
                <template #calendar-header="{ index, day }">
                  <div :class="index === 5 || index === 6 ? 'red-color' : ''">
                    {{ day }}
                  </div>
                </template>
              </Datepicker>
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="create_date" class="leading-7 text-sm text-blue-500">Create date</label>
              <Datepicker v-model="create_date" enableSeconds disabled/>
            </div>
          </div>
        </div>
        <div class="text-red-500 pt-3 text-sm">
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
						<button v-on:click.prevent="add_todo()" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
							Save
						</button>
						<router-link tag="button" to="/todo" class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-lg">
							Cancel
						</router-link>
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
		name: 'Todo Add',
		created () {
      document.title = "Add Todo";
    },
		data () {
			return {
				todo: {},
				create_date: null,
				due_date: null,
				categories: [],
				selected: this.$route.params.categoryId,
				error: null,
				changeKey: null,
			}
		},
		mounted () {
			this.get_categories();
		},
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
					url: '/api/todo/',
					data: {
						title : this.todo.title,
						description: this.todo.description,
						is_done: this.todo.is_done,
						category: this.selected,
						due_date: moment(this.due_date).format('YYYY-MM-DDThh:mm:ss'),
						created_date: moment(this.create_date).format('YYYY-MM-DDThh:mm:ss'),
					},
					headers: {
						Authorization: 'Token' + ' ' + this.$store.state.setUser.token
					},
				}).then(response => {
					this.todo = response.data;
					this.$router.go(-1);
				}).catch(err => console.log(this.error = err.response.data));
			},
			get_categories() {
        axios({
          method:'get',
          url: '/api/category/',
					headers: {
						Authorization: 'Token' + ' ' + this.$store.state.setUser.token
					},
        }).then(response => this.categories= response.data.results)
				.catch(err => console.log(this.error = err.response.data));
			},
			format_key(key) {
				if(key == 'title')
					return this.changeKey = 'Title';
				if(key == 'description')
					return this.changeKey = 'Description';
				if(key == 'created_date')
					return this.changeKey = 'Create date';
				if(key == "due_date")
					return this.changeKey = 'Due date';
				if(key == "is_done")
					return this.changeKey = 'Status';
				if(key == 'detail')
					return this.changeKey = 'Authentication';
			},
		},
	}
</script>

<style>
    .red-color {
        color: #3b82f6;
    }
    .dp__theme_light {
      --dp-success-color: #3b82f6;
      --dp-success-color-disabled: #bfdbfe
;
    }
</style>