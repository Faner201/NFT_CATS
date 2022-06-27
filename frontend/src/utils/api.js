const API_HOST = "https://mysterious-basin-29452.herokuapp.com/";

export function getProductData(id) {
    return fetch(`${API_HOST}/store/id=${id}`);
}

export function getProductsCount() {
    return fetch(`${API_HOST}/store/count`);
}

export function getProfileData(id) {
    return fetch(`${API_HOST}/profile/id=${id}`);
}

export function getImage(path) {
    return API_HOST + path;
}

export function buyProduct(id, profile) {
    return fetch(`${API_HOST}/buy`, {
        method: 'POST', 
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify({
            id: id,
            profile: profile
        })
    });
}

export function regProfile(form) {
    return fetch(`${API_HOST}/registration`, {
        method: 'POST', 
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify(form)
    });
}

export function authProfile(form) {
    return fetch(`${API_HOST}/auth`, {
        method: 'POST', 
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify(form)
    });
}

export function uploadProduct(form) {
    return fetch(`${API_HOST}/upload`, {
        method: 'POST', 
        body: form
    });
}