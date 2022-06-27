<script>
    import Button from "../components/Button.svelte";
    import { navigate } from "svelte-routing";
    import { uploadProduct } from "../utils/api.js";
    import { account } from "../stores/stores.js";

    let form = {};
    let files = [];
    let error = "";
    const maxlength = 30;

    $: fileName = files[0] == undefined 
        ? "Select a image" 
        : files[0].name;

    let upload = async () => {
        form.image = files[0];
        form.author = $account;
        let formData = new FormData();
        for (let property in form) 
            formData.append(property, form[property]);

        const responce = await uploadProduct(formData)
        const { answer } = await responce.json();
        if (answer === "nameError") {
            error = "Wrong name!";
        } else if (answer === "priceError") {
            error = "Wrong price!";
        } else if (answer === "imageError") {
            error = "Wrong image!";
        } else if (answer === "done") {
            navigate("/account");
        }
    };
</script>


<div class="container">
    <div class="block">
        <div class="error">{error}</div>
        <form>
            <input type="text" placeholder="Name" {maxlength} bind:value={form.name}>
            <textarea rows="18" placeholder="Description" maxlength="600" bind:value={form.description} />
            <input type="number" placeholder="Price" {maxlength} bind:value={form.price}>
            <label for="file">
                {fileName}
                <input id="file" type="file" accept="image/jpeg,image/png" bind:files={files} />
            </label>
        </form>
        <Button type="accent" size="big" text="Login" action={upload} />
    </div>
</div>


<style>
    .container {
        /* height: 90vh; */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .block {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 30px 0px;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-bottom: 20px;
    }

    input, textarea, label {
        width: 300px;
        font-size: 14px;
        padding: 12px 18px;
        border-radius: 8px;
        border: 2px solid var(--color-neutral-2);
        margin: 6px;
        resize: none;
    }

    input:focus {
        border: 2px solid var(--color-primary);
    }

    .error {
        margin: 10px;
        color: var(--color-error);
        font-size: 16px;
        font-weight: 500;
    }

    label {
        cursor: pointer;
    }

    #file {
        display: none;
    }    
</style>