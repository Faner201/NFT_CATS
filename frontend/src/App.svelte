<script>
    import { Router, Route } from "svelte-routing";
    import RegPage from "./pages/RegPage.svelte";
    import AuthPage from "./pages/AuthPage.svelte";
    import StorePage from "./pages/StorePage.svelte";
    import UploadPage from "./pages/UploadPage.svelte";
    import ProductPage from "./pages/ProductPage.svelte";
    import ProfilePage from "./pages/ProfilePage.svelte";
    import Header from "./components/Header.svelte";
    import Footer from "./components/Footer.svelte";
</script>


<Router>
    <Header/>
    <main>
        <!-- <Route path="/" component={ProfilePage} /> -->
        <Route path="/" component={StorePage} />
        <Route path="/reg" component={RegPage} />
        <Route path="/auth" component={AuthPage} />
        <Route path="/upload" component={UploadPage} />
        <Route path="/profile/:id" component={ProfilePage} />
        <Route path="/store/:id" component={ProductPage} />
    </main>
    <Footer/>
</Router>


<style>
    main {
        max-width: 1280px;
        margin: 0px auto;
    }
</style>