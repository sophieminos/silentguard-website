<template>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Retrouvez vos données personnelles
        </h1>
        <div class="flex justify-center gap-4">
            <router-link to="/fast-search" class="w-full border sm:w-1/2 md:w-1/3 lg:w-1/3 text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2">
                Analyse rapide
            </router-link>
            <router-link to="/advanced-search" class="w-full border sm:w-1/2 md:w-1/3 lg:w-1/3 text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2">
                Analyse avancée
            </router-link>
        </div>
    </div>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Et les faire disparaître
        </h1>
        <div class="flex justify-center gap-4">
            <router-link to="/doc-individuals" class="w-full border sm:w-1/2 md:w-1/3 lg:w-1/3 text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2">
                Pour les particuliers
            </router-link>
            <router-link to="/doc-organisations" class="w-full border sm:w-1/2 md:w-1/3 lg:w-1/3 text-center bg-midblue-silentguard text-white rounded hover:bg-darkblue-silentguard transition px-2 py-2">
                Pour les organisations
            </router-link>
        </div>
    </div>
</template>