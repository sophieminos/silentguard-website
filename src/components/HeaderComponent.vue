<template>
    <div class="bg-gradient-silentguard text-white">
        <div class="container mx-auto flex items-center justify-between py-4 px-6">
            <!-- Logo/Brand -->
            <div class="text-lg font-bold">
                <a href="#" class="hover:text-gray-400">SilentGuard</a>
            </div>
            <!-- Navigation Menu -->
            <nav class="hidden sm:flex space-x-6 ml-auto">
                <a href="#" class="hover:text-gray-400">Conseils</a>
            </nav>
            <!-- Button -->
            <div class="hidden sm:block ml-4">
                <a
                    href="#"
                    class="border border-white text-white px-2 py-2 rounded hover:bg-white hover:text-black transition"
                >
                    Traquer des données
                </a>
            </div>

            <!-- Mobile Menu Toggle -->
            <button
                class="md:hidden text-gray-300 focus:outline-none"
                @click="toggleMenu"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h16m-7 6h7"
                    />
                </svg>
            </button>
        </div>
        
        <div
            id="mobileMenu"
            :class="{'hidden': !isMobileMenuVisible, 'block': isMobileMenuVisible}"
            class="md:hidden bg-gray-700 text-white space-y-2 pt-4 pb-8 px-6 bg-gradient-silentguard"
        >
            <a href="#" class="block hover:text-gray-400 mb-4">Conseils</a>
            <a
            href="#"
            class="border border-white text-white px-2 py-2 my-4 rounded hover:bg-white hover:text-black transition"
            >
            Traquer des données
            </a>
        </div>
    </div>
</template>
<script>
    export default {
    data() {
        return {
            isMobileMenuVisible: false, // État du menu mobile
        };
    },
    methods: {
        toggleMenu() {
            this.isMobileMenuVisible = !this.isMobileMenuVisible;
        },
    },
    };
</script>
<style>
    
</style>