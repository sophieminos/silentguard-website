<template>
    <div id="loader" class="w-full h-full flex justify-center items-center absolute">
        <span></span>
    </div>
</template>
<style>
#loader {
    background-color: rgba(209, 209, 209, 0.4);
    z-index: 999999;
}
#loader span {
    width: 48px;
    height: 48px;
    border: 5px solid rgba(29,62,73,1);
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: rotation 1s linear infinite;
}

@keyframes rotation {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
} 
</style>