import { createRouter, createWebHashHistory } from 'vue-router';

// Importer vos composants
import HomeComponent from './pages/HomePage.vue';
import AdvancedSearchPage from './pages/AdvancedSearchPage.vue';
import FastSearchPage from './pages/FastSearchPage.vue';
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
    path: '/fast-search',
    name: 'Recherche rapide',
    component: FastSearchPage,
  },
  {
    path: '/advanced-search',
    name: 'Recherche avancée',
    component: AdvancedSearchPage,
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
