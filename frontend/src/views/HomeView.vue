<template>
  <section class="text-gray-600 body-font">
    <div class="container mx-auto flex px-5 items-center justify-center flex-col">
      <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" alt="hero" src="../assets/image.jpg">
      <div class="text-center lg:w-2/3 w-full">
        <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Todo & Note</h1>
        <p class="mb-8 leading-relaxed">Made by me and Just for me hehehe</p>
        <div v-if="$store.state.authenticated==true" class="flex justify-center">
          <router-link tag="button" to="/category" class="inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Category
          </router-link>
          <router-link tag="button" to="/todo" class="ml-4 inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Todo
          </router-link>
          <router-link tag="button" to="/note" class="ml-4 inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Note
          </router-link>
        </div>
        <div v-else class="flex justify-center">
          <router-link tag="button" to="/" class="inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Category
          </router-link>
          <router-link tag="button" to="/" class="ml-4 inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Todo
          </router-link>
          <router-link tag="button" to="/" class="ml-4 inline-flex hover:text-blue-50 hover:bg-blue-500 bg-blue-50 text-blue-500 border-0 py-2 px-6 focus:outline-none rounded text-lg">
            Note
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: 'HomeView',
    created () {
      document.title = "Todo&Note";
    },
  }
</script>