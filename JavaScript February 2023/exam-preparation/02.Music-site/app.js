// window.addEventListener('load', solve);
//
// function solve() {
//     const genreInputField = document.getElementById('genre');
//     const nameInputField = document.getElementById('name');
//     const authorInputField = document.getElementById('author');
//     const dateInputField = document.getElementById('date');
//     const addBtn = document.getElementById('add-btn');
//     const songsCollection = document.querySelector('#all-hits > div');
//
//     addBtn.addEventListener("click", addSongHandler);
//
//     function addSongHandler(e) {
//         e.preventDefault();
//         if (genreInputField.value && nameInputField.value && authorInputField.value && dateInputField.value) {
//             const divContainer = document.createElement('div');
//             divContainer.className = 'hits-info';
//             divContainer.innerHTML = `<img src="./static/img/img.png">
//                                 <h2>Genre: ${genreInputField.value}</h2>
//                                 <h2>Name: ${nameInputField.value}</h2>
//                                 <h2>Author: ${authorInputField.value}</h2>
//                                 <h3>Date: ${dateInputField.value}</h3>
//                                 <button class="save-btn">Save song</button>
//                                 <button class="like-btn">Like song</button>
//                                 <button class="delete-btn">Delete</button>`;
//
//             songsCollection.appendChild(divContainer);
//
//             genreInputField.value = '';
//             nameInputField.value = '';
//             authorInputField.value = '';
//             dateInputField.value = '';
//
//             let saveBtn = divContainer.querySelector('.save-btn');
//             let likeBtn = divContainer.querySelector('.like-btn');
//             let deleteBtn = divContainer.querySelector('.delete-btn');
//
//             saveBtn.addEventListener('click', saveSongHandler);
//             likeBtn.addEventListener('click', likeSongHandler);
//             deleteBtn.addEventListener('click', deleteSongHandler);
//
//             function likeSongHandler(e) {
//                 e.target.disabled = true;
//                 let totalLikes = document.querySelector('#total-likes > .likes > p');
//                 let likesNum = Number(totalLikes.textContent.split(': ')[1]);
//                 likesNum += 1;
//                 totalLikes.textContent = `Total Likes: ${likesNum}`;
//             }
//
//             function saveSongHandler() {
//                 let savedSongsContainer = document.querySelector('.saved-container');
//                 likeBtn.remove();
//                 saveBtn.remove();
//                 savedSongsContainer.appendChild(divContainer);
//             }
//
//             function deleteSongHandler() {
//                 divContainer.remove();
//             }
//         }
//     }
// }


window.addEventListener("load", solve)
function solve() {
    const addBtn = document.getElementById('add-btn')
    const allHitsDivContainer = document.querySelector('.all-hits-container')
    const savedContainer = document.querySelector('#saved-hits > .saved-container')
    const form = document.querySelector("#append-song > div > div > form")
    const inputFields = {
        genre: document.getElementById('genre'),
        name: document.getElementById('name'),
        author: document.getElementById('author'),
        date: document.getElementById('date')
    }

    addBtn.addEventListener("click", addSongHandler)

    function addSongHandler(e) {
        e.preventDefault()
        if (!inputFields.genre.value || !inputFields.name.value || !inputFields.author.value || !inputFields.date.value){
            return
        }

        const hitsInfoContainer = createElement('div', allHitsDivContainer, '', ['hits-info'], '', '', '')
        const img = createElement('img', hitsInfoContainer, '', '', '', {src: "./static/img/img.png"}, '')
        createElement('h2', hitsInfoContainer, `Genre: ${inputFields.genre.value}`, '', '', '', '')
        createElement('h2', hitsInfoContainer, `Name: ${inputFields.name.value}`, '', '', '', '')
        createElement('h2', hitsInfoContainer, `Author: ${inputFields.author.value}`, '', '', '', '')
        createElement('h3', hitsInfoContainer, `Date: ${inputFields.date.value}`, '', '', '', '')
        const saveBtn = createElement('button', hitsInfoContainer, 'Save song', ['save-btn'], '', '', '')
        const likeBtn = createElement('button', hitsInfoContainer, 'Like song', ['like-btn'], '', '', '')
        const deleteBtn = createElement('button', hitsInfoContainer, 'Delete', ['delete-btn'], '', '', '')

        saveBtn.addEventListener('click', () => {
            saveBtn.remove()
            likeBtn.remove()
            savedContainer.appendChild(hitsInfoContainer)
        })

        likeBtn.addEventListener('click', likeSongHandler)
        deleteBtn.addEventListener('click', () => {hitsInfoContainer.remove()})

        form.reset()
    }

    function likeSongHandler(){
        const totalLikesParagraph = document.querySelector("#total-likes > .likes > p")
        let totalLikes = Number(totalLikesParagraph.textContent.split(': ')[1])
        totalLikes += 1
        totalLikesParagraph.textContent = `Total Likes: ${totalLikes}`
        this.disabled = true
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