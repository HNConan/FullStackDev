import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/admin',
      name: 'Administration',
      component: () => import('../views/Admin.vue')
    },
    {
      path: '/question/:id/edit',
      name: 'QuestionEdition',
      component: () => import('../views/QuestionEdition.vue')
    },
    {
      path: '/NewQuizPage',
      name: 'NewQuizPage',
      component: () => import('../views/NewQuizPage.vue')
    },
    {
      path: '/QuestionManager',
      name: 'QuestionManager',
      component: () => import('../views/QuestionManager.vue')
    },
    {
      path:'/Leaderboard',
      name : 'Leaderboard',
      component: () => import('../views/Leaderboard.vue')

    }
  ]
})

export default router
