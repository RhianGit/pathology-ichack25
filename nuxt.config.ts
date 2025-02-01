import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  pages: true,
  plugins: [
    {src: '~/plugins/openseadragon.js', mode: 'client'}
  ],
  vite: {
    plugins: [tailwindcss()]
  },
})
