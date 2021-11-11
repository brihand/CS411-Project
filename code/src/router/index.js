import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		redirect: '/home'
	},
	{
		path: '/home',
		name: 'home',
		component: Home,
		children: [
			{
				path: '',
				name: 'index',
				component: () =>
					import('../views/Index.vue')
			},
			{
				path: '/search',
				name: 'Search',
				component: () =>
					import('../views/Search.vue')
			}
		]
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
