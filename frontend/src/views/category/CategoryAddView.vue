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
							<input v-model="category.title" type="text" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
						</div>
					</div>
					<div class="p-2 w-full">
						<div class="relative">
							<label for="message" class="leading-7 text-sm text-gray-600">Detail</label>
							<textarea v-model="category.detail" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
						</div>
					</div>
					<div class="p-2 w-full">
						<div class="relative">
							<label for="name" class="leading-7 text-sm text-gray-600">Create date</label>
							<Datepicker v-model="date" enableSeconds disabled/>
						</div>
					</div>
				</div>
				<div class="flex justify-center mt-8">
						<button v-on:click="add_category()" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
							Save
						</button>
						<button class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
							<router-link to="/category">Cancel</router-link>
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
		name: 'Category Detail',
		data () {
			return {
				category: {},
				date: null,
			}
		},
		mounted () {},
		components: { Datepicker },
		setup() {
			const date = ref(new Date());
			return {
				date,
			}
		},
		methods: {
			add_category() {
				axios({
					method: 'post',
					url: 'http://127.0.0.1:8000/api/category/',
					data: {
						title : this.category.title,
						detail: this.category.detail,
						created_date: moment(this.date).format('YYYY-MM-DDThh:mm:ss'),
					},
					auth: {
						username: 'admin',
						password: 'admin@123'
					}
				}).then(response => {
					this.category = response.data;
					this.$router.go(-1);
				});
			},
		},
	}
</script>