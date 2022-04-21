<template>
  <header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <span class="ml-3 text-xl hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link to="/">Todo & Note</router-link>
        </span>
      </a>
      <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
        <a class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link to="/category">Category</router-link>
        </a>
        <a class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link to="/todo">Todo</router-link>
        </a>
        <a class="mr-5 hover:text-gray-900 hover:bg-gray-100 border-0 py-1 px-3 rounded">
          <router-link to="/note">Note</router-link>
        </a>
      </nav>
      <button class="inline-flex items-center text-gray-700 hover:text-gray-100 bg-gray-100 hover:bg-gray-500 border-0 py-1 px-3 focus:outline-none rounded text-base mt-4 md:mt-0">Logout
        <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
          <path d="M5 12h14M12 5l7 7-7 7"></path>
        </svg>
      </button>
    </div>
  </header>
  <router-view/>
</template>
