<template>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Analyse avancée
        </h1>
        <div class="relative my-8">
            <input type="text" class="w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="email, nom d’utilisateur, ...">
            <!-- Icône loupe FontAwesome -->
            <i id="advanced-search-button" class="fas fa-search absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
        </div>
    </div>
    <ResultsComponent :results="results"/>
</template>
<script>
import ResultsComponent from '@/components/ResultsComponent.vue';
import $ from 'jquery';

export default {
    components: {
        ResultsComponent,
    },
    data() {
        return {
            results: [],
        };
    },
    mounted() {
        const res = {
            "prénom": "Melon",
            "nom": "Husk",
            "email": "melon.husk@gamil.com",
            "addresse": "11 rue des petits pois, 12345 Paradis",
            "tel": "+33 123456578"
        }
        $('#advanced-search-button').on('click', () => {
            this.results=res;
            console.log('Button clicked!');
        });
    },
};
</script>