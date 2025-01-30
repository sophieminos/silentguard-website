import { createRouter, createWebHashHistory } from 'vue-router';

// Importer vos composants
import HomeComponent from './pages/HomePage.vue';
import SearchPage from './pages/SearchPage.vue';
import DocOrganisationsPage from './pages/DocOrganisationsPage.vue';
import DocIndividualsPage from './pages/DocIndividualsPage.vue';

// Définir les routes
const routes = [
  {
    path: '/',
    name: 'Accueil',
    component: HomeComponent,
  },
  {
    path: '/search',
    name: 'Recherche rapide',
    component: SearchPage,
  },
  {
    path: '/doc-organisations',
    name: 'Conseils pour les organisations',
    component: DocOrganisationsPage,
  },
  {
    path: '/doc-individuals',
    name: 'Conseils pour les particuliers',
    component: DocIndividualsPage,
  },
];

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
});
router.beforeEach((to, from, next) => {
    next();
});

export default router;
