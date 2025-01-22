<template>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Analyse rapide
        </h1>
        <div class="flex justify-center gap-4">
            <span>Vous souhaitez une analyse plus approfondie ?</span>
            <router-link to="/advanced-search" class="text-lightblue-silentguard text-center underline">
                ⇒ Recherche avancée
            </router-link>
        </div>
        <div class="relative my-8">
            <input id="fast-search-input" type="text" class="w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="email, nom d’utilisateur, ...">
            <!-- Icône loupe FontAwesome -->
            <i id="fast-search-button" class="fas fa-search absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
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
        const search = () => { 
            /*this.results = [
                ["addresse", "11 rue des petits pois, 12345 Paradis"],
                ["email", "melon.husk@gamil.com"],
                ["nom", "Husk"],
                ["prénom", "Melon"],
                ["tel", "+33 123456578"]
            ];
            console.log(this.results);*/
            $.ajax({
                url: 'https://silent-guard.fr/api/fast-search/',
                method: 'GET',
                data: { }, 
                success: (response) => {
                    this.results = Object.entries(response.search_result);
                    console.log('Success:', response, this.results);
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        }
        $('#fast-search-button').on('click', () => {
            console.log('Button clicked!');
            search();
        });
        $('#fast-search-input').on('keydown', (e) => {
            if (e.key === "Enter" || e.keyCode === 13) {
                search();
            }
        });
    },
};
</script>