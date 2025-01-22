
<template>
<div>
    <header>
        <slot name="header"></slot>
    </header>
    <main>
        <slot></slot>
    </main>
    <footer>
        <slot name="footer"></slot>
    </footer>
</div>
</template>

<script>
export default {
    name: "BaseLayout",
};
</script>

<style scoped>
main {
    background-image: url("./assets/background.png");
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 87vh;
}
</style>
    
