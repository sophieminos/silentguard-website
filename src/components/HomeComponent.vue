<template>
    <div class="container mx-auto py-4 px-6">
        <h1 class="text-midblue-silentguard text-center my-8 font-bold">
            Contrôlez ce que l’on sait de vous sur le web<br/>grâce à l’OSINT
        </h1>
        <div class="relative my-8">
            <input type="text" class="w-full text-center font-light pl-10 pr-4 py-2 border border-gray-300 rounded-md focus:outline-none" placeholder="email, nom d’utilisateur, ...">
            <!-- Icône loupe FontAwesome -->
            <i class="fas fa-search absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500"></i>
        </div>
        <table class="min-w-full border-separate border-spacing-0 rounded-lg overflow-hidden border text-center">
            <thead class="text-white">
                <tr>
                <th class="px-4 py-2 font-normal">information</th>
                <th class="px-4 py-2 font-normal">site internet</th>
                </tr>
            </thead>
            <tbody>
                <tr class="hover:bg-gray-100">
                    <td class="px-4 py-2">pseudo</td>
                    <td class="px-4 py-2">www.site-web.com</td>
                </tr>
                <tr class="hover:bg-gray-100 ">
                    <td class="px-4 py-2">pseudo</td>
                    <td class="px-4 py-2">www.site-web.com</td>
                </tr>
                <tr class="hover:bg-gray-100 ">
                    <td class="px-4 py-2">email</td>
                    <td class="px-4 py-2">www.site-web.com</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>