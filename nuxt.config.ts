// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  pages: true,
  plugins: [{src: '~/plugins/openseadragon.js', mode: 'client'}],
})
