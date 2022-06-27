<script>
    import { onMount } from "svelte/internal";
    import { navigate } from "svelte-routing";
    import { account, profile } from "../stores/stores";
    import { getProductData, getImage, buyProduct } from "../utils/api";
    import Button from "../components/Button.svelte";

    export let id = 1;
    let product = {};

    onMount(async () => {
        getProductData(id)
            .then(response => response.json())
            .then(json => product = json);
    });

    let buy = async () => {
        buyProduct(id, $account);
        $profile = product.authorId
        navigate(`/profile/id=${$profile}`);
    };
</script>


<div class="container">
    <img src={getImage(product.image)} alt="" class="image" />
    <div class="block">
        <div class="name">{product.name}</div>
        <button class="author" on:click={() => navigate(`/users/id=${product.authorId}`)}>
            <img src={getImage(product.authorImage)} alt="" class="author-image">
            <div class="author-name">{product.authorName}</div>
        </button>
        <p class="description">{product.description}</p>
        <div class="end">
            <div class="price">{product.price + " ETH"}</div>
            <Button type="light" size="big" text="Buy" action={buy} />
        </div>
    </div>
</div>


<style>
    .container {
        display: flex;
        flex-direction: row;
        justify-content: stretch;
        border: 2px solid var(--color-neutral-2);
        border-radius: 20px;
        margin: 60px auto;
        max-width: 1000px;
        padding: 30px;
        gap: 20px;
    }

    .block {
        display: flex;
        flex-direction: column;
        align-items: center;
        flex-grow: 1;
    }

    .image {
        height: 400px;
        width: 400px;
    }
    
    .name {
        color: var(--color-neutral-6);
        font-size: 24px;
        font-weight: 700;
    }

    .author {
        display: flex;
        flex-direction: row;
        align-items: center;
        color: var(--color-neutral-6);
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 16px;
        align-self: flex-start;
        gap: 12px;
    }

    .author-image {
        height: 30px;
        width: 30px;
    }

    .author-name {
        color: var(--color-neutral-6);
        font-size: 18px;
        font-weight: 500;
    }

    .description {
        color: var(--color-neutral-5);
        font-size: 16px;
        font-weight: 400;
        white-space: pre-line;
        align-self: flex-start;
    }

    .end {
        margin: auto;
        margin-bottom: 0px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .price {
        font-size: 16px;
        font-weight: 700;
        color: var(--color-success);
        border-radius: 4px; 
        padding: 4px 6px;
        border: 3px solid var(--color-success);
        margin-bottom: 10px;
    }
</style>