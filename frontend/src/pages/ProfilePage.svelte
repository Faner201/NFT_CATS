<script>
    import { onMount } from "svelte/internal";
    import { account } from "../stores/stores";
    import { getProfileData, getImage } from "../utils/api";
    import ProductCard from "../components/ProductCard.svelte";

    let user = {
        nfts: []
    };

    onMount(async () => {
        getProfileData($account)
            .then(response => response.json())
            .then(json => user = json);
    });
</script>


<div class="container">
    <div class="info-block">
        <img src={getImage(user.image)} alt="">
        <div class="name">{user.name}</div>
    </div>
    <div class="product-list">
        {#each user.nfts as id}
            <ProductCard id={id} />
        {/each}
    </div>
</div>


<style>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .info-block {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 20px;
    }

    .name {
        color: var(--color-neutral-6);
        font-size: 32px;
        font-weight: 700;
    }

    img {
        height: 80px;
        width: 80px;
    }

    .product-list {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
    }
</style>