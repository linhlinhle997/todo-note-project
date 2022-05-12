<template>
	<section class="text-blue-500 body-font relative">
		<div class="container px-5 py-5 mx-auto">
			<div class="flex flex-col text-center w-full">
				<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-blue-500">Login</h1>
			</div>
			<div class="lg:w-1/2 md:w-2/3 mx-auto">
				<div class="flex flex-wrap -m-2">
					<div class="p-2 w-full">
						<div class="relative">
							<label for="Email" class="leading-7 text-sm text-blue-500">Email</label>
							<input v-model="user.email" type="email" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
						</div>
					</div>
					<div class="p-2 w-full">
						<div class="relative">
							<label for="Password" class="leading-7 text-sm text-blue-500">Password</label>
							<input v-model="user.password" type="password" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
						</div>
					</div>
				</div>
				<div v-if="error!=null" class="text-red-500 text-sm pt-3">
          * {{error.detail}} <br>
        </div>
				<div class="flex justify-center mt-5">
						<button v-on:click.prevent="login()" class="inline-flex text-blue-500 hover:text-blue-50 hover:bg-blue-500 bg-blue-50 border-0 py-2 px-6 focus:outline-non rounded text-lg">
							Submit
						</button>
						<router-link tag="button" to="/" class="ml-4 inline-flex text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-700 border-0 py-2 px-6 focus:outline-none rounded text-lg">
							Cancel
						</router-link>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
	import axios from 'axios'
	import { validationMixin } from 'vuelidate'
	import { required, maxLength, email } from 'vuelidate/lib/validators'

	export default {
		name: 'Login',
		created () {
      document.title = "Login";
    },
		data () {
			return {
				user: {},
				error: null,
			}
		},
		mounted () {},
		methods: {
			login() {
				axios({
					method: 'post',
					url: '/api/login/',
					data: {
						email : this.user.email,
						password: this.user.password,
					},
				}).then(response => {
					this.$store.commit('setUser', response.data);
					this.$store.commit('setAuthenticated', true)
					this.$router.push('/');
				}).catch(error => this.error = error.response.data);
			},
		},
	}
</script>