<template>
    <div class="container mx-auto py-4 px-6">
        <table class="min-w-full border-separate border-spacing-0 rounded-md overflow-hidden border text-center">
            <thead class="text-white">
                <tr>
                <th class="px-4 py-2 w-48 font-normal">champ</th>
                <th class="px-4 py-2 font-normal">valeur trouvée</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="results.length === 0">
                    <td colspan="2" class="text-center x-4 py-2">Aucune information</td>
                </tr>

                <tr v-for="(item, index) in results" :key="index" class="hover:bg-gray-100">
                    <td class="px-4 py-2">{{ index }}</td>
                    <td class="px-4 py-2">{{ item }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
export default {
  props: {
    results: {
      type: Array,
      default: () => [] // Initialise results comme tableau vide par défaut
    },
  },
};
</script>