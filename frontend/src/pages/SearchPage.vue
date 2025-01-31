<template>
    <LoaderComponent/>
    <PopupAgreementComponent/>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Analyse
        </h1>
        <form id="search-form">
            <div class="w-full flex flex-wrap w-100 my-3 relative">
                <div class="w-full flex flex-wrap">
                    <div class="lg:w-5/6 md:w-5/6 sm:w-full">
                        <input type="text" class="w-full lg:w-1/4 md:w-1/4 sm:w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="prénom" name="first_name">
                        <input type="text" class="w-full lg:w-1/4 md:w-1/4 sm:w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="nom" name="last_name">
                        <input type="text" class="w-full lg:w-1/4 md:w-1/4 sm:w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="pseudo" name="pseudo">
                        <input type="text" class="w-full lg:w-1/4 md:w-1/4 sm:w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="email" name="email">
                    </div>
                    <!---->
                    <a id="search-button" style="" class="w-full lg:w-1/6 md:w-1/6 sm:w-full cursor-pointer text-center bg-gradient-silentguard text-white px-2 py-2 rounded hover:text-gray-400 transition">
                        Continuer
                    </a>
                </div>
            </div>
        </form>
    </div>
    <ResultsComponent :results="results"/>
</template>
<script>
import ResultsComponent from '@/components/ResultsComponent.vue';
import LoaderComponent from '@/components/LoaderComponent.vue';
import $ from 'jquery';
import PopupAgreementComponent from '@/components/PopupAgreementComponent.vue';

export default {
    components: {
        ResultsComponent,
        LoaderComponent,
        PopupAgreementComponent
    },
    data() {
        return {
            results: []
        };
    },
    mounted() {
        $('#loader').hide();
        
        const search = () => { 
            $('#loader').show();
            this.results = [];
            /*
            this.results = [
                ["lien avec pseudo 7", "https://archive.org/details/@sophie_mi22"],
                ["lien avec pseudo 7", "https://archive.org/details/@sophie_mi22"],
                ["lien avec pseudo 7", "https://archive.org/details/@sophie_mi22"],
            ];
            console.log(this.results);
            */
            console.log($('#search-form').serialize());
            $.ajax({
                url: 'https://silent-guard.fr/api/search/',
                method: 'GET',
                data: $('#search-form').serialize(), 
                success: (response) => {
                    $('#loader').hide();
                    this.results = Object.entries(response.search_result);
                    console.log('Success:', response, this.results);
                },
                error: function(xhr, status, error) {
                    $('#loader').hide();
                    console.error('Error:', error);
                }
            });
        }
        $('#search-button').on('click', (e) => {
            e.stopPropagation();
            e.preventDefault()
            $('.overlay').show();
        });

        $('.close').on('click', () => {
            $('.overlay').hide();
        });

        $('#formAgreement').on('submit', (e) => {
            e.stopPropagation();
            e.preventDefault()
            if($('#formAgreement #checkboxAgreement').prop("checked")){
                search();
            }
            $('.overlay').hide();
        });


        



        
    },
};
</script>
<style>

</style>