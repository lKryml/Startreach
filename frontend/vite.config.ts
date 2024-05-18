import path from "path"
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
// import VueDevTools from 'vite-plugin-vue-devtools'
import tailwind from "tailwindcss"
import autoprefixer from "autoprefixer"

// https://vitejs.dev/config/
export default defineConfig({
	css: {
		postcss: {
			plugins: [tailwind(), autoprefixer()],
		},
	},
	server: {
		hmr: true
	},
	plugins: [
		vue(),
		vueJsx(),
		// VueDevTools(),
	],
	resolve: {
		alias: {
			'@': path.resolve(__dirname, "./src")
		}
	}
})
