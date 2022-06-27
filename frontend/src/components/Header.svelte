<script>
    import { navigate } from "svelte-routing";
    import { account, profile } from "../stores/stores.js";
    import SearchLine from "./SearchLine.svelte";
    import Button from "./Button.svelte";

    let uploadAction = () => {
        navigate($account != undefined ? "/upload" : "/auth");
    };

    let accountAction = () => {
        if ($account != undefined) {
            $profile = $account
            navigate(`/profile/id=${$profile}`)
        } else {
            navigate(`/auth`);
        }
    };
</script>


<header>
    <div class="container">
        <button class="logo" on:click={() => navigate("/")}>NFT Сats</button>
        <div class="right">
            <SearchLine/>
            <Button type="accent" size="medium" text="Upload" action={uploadAction} />
            <Button type="light" size="medium" text="Account" action={accountAction} />
        </div>
    </div>
</header>


<style> 
    header {
        border-bottom: 1px solid var(--color-neutral-2);
    }

    .container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        max-width: 1280px;
        margin: 0 auto;
        padding: 14px 0px;
    }
    
    .right {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 16px;
    }
    
    .logo {
        justify-self: flex-start;
        font-size: 28px;
        font-weight: 700;
        color: var(--color-neutral-6);
    }
</style>