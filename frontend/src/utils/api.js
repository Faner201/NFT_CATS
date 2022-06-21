export const API_HOST = "http://127.0.0.1:5000";

export function getProductData(id) {
    return fetch(`${API_HOST}/store/page=${id}`).json();
}

export function getProductsCount() {
    const { answer } = fetch(`${API_HOST}/store/count`).json();
    return answer;
}