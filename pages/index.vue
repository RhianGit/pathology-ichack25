<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
      <h1 class="text-5xl font-bold text-gray-700 mb-8">Path-o-gen</h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-lg">
        <nuxt-link to="/patient/17229" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 1
        </nuxt-link>
        <nuxt-link to="/patient/17230" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 2
        </nuxt-link>
        <nuxt-link to="/patient/17231" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 3
        </nuxt-link>
        <nuxt-link to="/patient/17232" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 4
        </nuxt-link>
        <nuxt-link to="/patient/17233" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 5
        </nuxt-link>
        <nuxt-link to="/patient/17234" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
          Case 6
        </nuxt-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'IndexPage'
  }
  </script>