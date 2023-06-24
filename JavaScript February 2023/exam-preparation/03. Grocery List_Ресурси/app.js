// window.addEventListener('load', solve);
//
// function solve() {
//     const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';
//     const productInput = document.getElementById('product');
//     const countInput = document.getElementById('count');
//     const priceInput = document.getElementById('price');
//     const addBtn = document.getElementById('add-product'); // type: submit => e.preventDefault()
//     const updateBtn = document.getElementById('update-product');
//     const loadAllBtn = document.getElementById('load-product');
//     const tbody = document.getElementById('tbody');
//
//     loadAllBtn.addEventListener("click", loadProductsHandler);
//     addBtn.addEventListener("click", addProductHandler);
//
//     function loadProductsHandler(e) {
//         if (e) {
//             e.preventDefault();
//         }
//         tbody.innerHTML = '';
//         fetch(BASE_URL)
//             .then((res) => res.json())
//             .then(productsRes => {
//                 const productsData = Object.values(productsRes);
//
//                 for (const {product, price, count, _id} of productsData) {
//                     const tr = document.createElement('tr');
//                     tr.id = _id;
//                     const tdName = document.createElement('td');
//                     const tdCount = document.createElement('td');
//                     const tdPrice = document.createElement('td');
//                     const tdBtn = document.createElement('td');
//                     const updateSmallBtn = document.createElement('button');
//                     const deleteSmallBtn = document.createElement('button');
//                     tdName.textContent = product;
//                     tdCount.textContent = count;
//                     tdPrice.textContent = price;
//                     updateSmallBtn.textContent = 'Update';
//                     deleteSmallBtn.textContent = 'Delete';
//                     tdBtn.appendChild(updateSmallBtn);
//                     tdBtn.appendChild(deleteSmallBtn);
//                     tr.appendChild(tdName);
//                     tr.appendChild(tdCount);
//                     tr.appendChild(tdPrice);
//                     tr.appendChild(tdBtn);
//                     tbody.appendChild(tr);
//
//                     tdBtn.id = _id;
//
//                     updateSmallBtn.addEventListener("click", updateProductHandler);
//                     deleteSmallBtn.addEventListener("click", deleteProductHandler);
//                 }
//             });
//     }
//
//     function addProductHandler(e) {
//         if (e) {
//             e.preventDefault();
//         }
//         tbody.innerHTML = '';
//         const product = productInput.value;
//         const count = countInput.value;
//         const price = priceInput.value;
//
//         const httpHeaders = {
//             method: 'POST',
//             body: JSON.stringify({product, count, price})
//         };
//         fetch(BASE_URL, httpHeaders)
//             .then(() => {
//                 loadProductsHandler(e);
//                 productInput.value = '';
//                 countInput.value = '';
//                 priceInput.value = '';
//             })
//             .catch((err) => {
//                 console.error(err);
//             });
//     }
//
//     function deleteProductHandler(event) {
//         const id = event.currentTarget.parentNode.id;
//         const httpHeaders = {
//             method: 'DELETE',
//         };
//         fetch(`${BASE_URL}${id}`, httpHeaders)
//             .then(() => loadProductsHandler())
//             .catch((err) => {
//                 console.error(err);
//             });
//     }
//
//     function updateProductHandler(event) {
//         updateBtn.disabled = false;
//         addBtn.disabled = true;
//         const parent = event.currentTarget.parentNode.parentNode;
//         const id = parent.id;
//         const [product, count, price] = parent.children;
//         productInput.value = product.textContent;
//         countInput.value = count.textContent;
//         priceInput.value = price.textContent;
//
//         updateBtn.addEventListener("click", submitUpdatedProductHandler);
//
//         function submitUpdatedProductHandler() {
//             const product = productInput.value;
//             const count = countInput.value;
//             const price = priceInput.value;
//
//             const httpHeaders = {
//                 method: 'PATCH',
//                 body: JSON.stringify({product, count, price})
//             };
//             fetch(`${BASE_URL}${id}`, httpHeaders)
//                 .then(() => {
//                     loadProductsHandler();
//                 })
//                 .catch((err) => {
//                     console.error(err);
//                 });
//
//             addBtn.disabled = false;
//             updateBtn.disabled = true;
//             const form = document.querySelector('.list');
//             form.reset();
//         }
//     }
// }
//
//
//


window.addEventListener('load', solve);

function solve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/grocery/'
    const inputFields = {
        product: document.getElementById('product'),
        count: document.getElementById('count'),
        price: document.getElementById('price')
    }
    const form = document.querySelector('.list')
    const loadBtn = document.getElementById('load-product')
    const addBtn = document.getElementById('add-product')
    const updateBigBtn = document.getElementById('update-product')
    const tbody = document.getElementById('tbody')

    loadBtn.addEventListener("click", loadAllHandler)
    addBtn.addEventListener("click", addHandler)
    function loadAllHandler(e){
        if (e){
            e.preventDefault()
        }

        tbody.innerHTML = ''

        fetch(BASE_URL)
            .then((res) => res.json())
            .then(productRes => {
                const productData = Object.values(productRes)

                for (const { product, count, price, _id} of productData) {
                    const trParent = createElement('tr', tbody, null, null,_id,null,null)
                    createElement('td', trParent, `${product}`, ['name'], null, null,null)
                    createElement('td', trParent, `${count}`, ['count-product'], null, null,null)
                    createElement('td', trParent, `${price}`, ['product-price'], null, null,null)
                    const buttonsTd = createElement('td', trParent, null, ['btn'], _id, null,null)
                    const updateBtn = createElement('button', buttonsTd, 'Update', ['update'], null,null,null)
                    const deleteBtn = createElement('button', buttonsTd, 'Delete', ['delete'], null,null,null)

                    deleteBtn.addEventListener('click', deleteHandler)
                    updateBtn.addEventListener('click', updateHandler)
                }
                function deleteHandler(e){
                    const httpHeaders = {
                        method: 'DELETE'
                    }
                    const id = e.currentTarget.parentNode.parentNode.id

                    fetch(`${BASE_URL}${id}`, httpHeaders)
                        .then(() => loadAllHandler())
                        .catch((err) => {
                            console.error(err);
                        })
                }
                function updateHandler(e){
                    updateBigBtn.disabled = false
                    addBtn.disabled = true
                    const parent = e.currentTarget.parentNode.parentNode
                    const id = parent.id
                    const [product, count, price] = parent.children
                    inputFields.product.value = product.textContent
                    inputFields.count.value = count.textContent
                    inputFields.price.value = price.textContent

                    updateBigBtn.addEventListener("click", submitUpdatedProductHandler)

                    function submitUpdatedProductHandler(){
                        const product = inputFields.product.value
                        const count = inputFields.count.value
                        const price = inputFields.price.value

                        const httpHeaders = {
                            method: 'PATCH',
                            body: JSON.stringify({ product, count, price})
                        }
                        fetch(`${BASE_URL}${id}`, httpHeaders)
                            .then(() => loadAllHandler())
                            .catch((err) => {
                                console.error(err);
                            })

                        updateBigBtn.disabled = true
                        addBtn.disabled = false
                        form.reset()
                    }
                }
            })
    }

    function addHandler(e) {
        if (e){
            e.preventDefault()
        }
        tbody.innerHTML = ''
        const product = inputFields.product.value
        const count = inputFields.count.value
        const price = inputFields.price.value

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({product, count, price})
        }

        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadAllHandler()
                form.reset()
            })
            .catch((err) => {
                console.error(err);
            })
    }

    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);

        if (content && useInnerHtml) {
            htmlElement.innerHTML = content;
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content;
            }

            if (content && type === 'input') {
                htmlElement.value = content;
            }
        }

        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }

        if (content && type === 'input') {
            htmlElement.value = content;
        }

        if (id) {
            htmlElement.id = id;
        }

        // ['list', 'item']
        if (classes) {
            htmlElement.classList.add(...classes);
        }

        // { src: './static/img/img.png' }
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key]);
            }
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;
    }
}