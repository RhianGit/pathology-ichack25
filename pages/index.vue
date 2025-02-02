<style>
bag-col {
    background-color: #F2F2EB;
}
</style>
<template>
    <div class="flex flex-col bag-col items-center justify-center min-h-screen p-6">
        <h1 class="text-5xl font-bold text-gray-700 mb-[100px]">Path-o-gen</h1>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-lg">
            <nuxt-link to="/patient/17239"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 1: Jim
            </nuxt-link>
            <nuxt-link to="/patient/17230"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 2: Jam
            </nuxt-link>
            <nuxt-link to="/patient/17229"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 3: Tim
            </nuxt-link>
            <nuxt-link to="/patient/17232"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 4: Tam
            </nuxt-link>
            <nuxt-link to="/patient/17233"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 5: Sim
            </nuxt-link>
            <nuxt-link to="/patient/17234"
                class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-200 text-center">
                Patient 6: Sam
            </nuxt-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'IndexPage'
}
</script>
