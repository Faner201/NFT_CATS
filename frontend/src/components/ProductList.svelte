<script>
    import { onMount, onDestroy } from "svelte/internal";
    import { getProductsCount } from "../utils/api";
    import ProductCard from "./ProductCard.svelte";

    let listElement;
    $: products = [];
    let maxCount = 0;

    function addCardWithScroll() {
        const offset = 1400;
        let scrollY = listElement.offsetTop + listElement.clientHeight;
        if (scrollY < window.scrollY + offset && products.length < maxCount) {
            products = [...products, products.length + 1];
        }
    }

    function addCards() {
        for (let i = 0; i < 6; i++)
        {
            if (products.length < maxCount) {
                products = [...products, products.length + 1];
            }
        }
    }

    onMount(async () => {
        getProductsCount()
            .then(response => response.json())
            .then(json => maxCount = json.count)
            .catch(() => maxCount = 6); 
        await addCards()
        
        window.addEventListener("scroll", addCardWithScroll);
    });

    onDestroy(() => {
        window.removeEventListener("scroll", addCardWithScroll);
    });
</script>


<div bind:this={listElement}>
    {#each products as index}
        <ProductCard id={index} />
    {/each}
</div>


<style>
    div {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
    }
</style>