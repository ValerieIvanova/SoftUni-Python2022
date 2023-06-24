function attachEvents() {
    const loadBooks = document.getElementById('loadBooks');
    const booksContainer = document.querySelector('table > tbody');
    const [titleInput, authorInput] = Array.from(document.querySelectorAll('#form > input'));
    const submitBtn = document.querySelector('#form > button');
    const formHeader = document.querySelector('#form > h3')
    let allBooks = {};
    let editBookId = null;
    const BASE_URL = 'http://localhost:3030/jsonstore/collections/books';

    loadBooks.addEventListener('click', loadAllBooksHandler);
    submitBtn.addEventListener('click', submitFormHandler);


    async function loadAllBooksHandler() {
        booksContainer.innerHTML = '';
        const booksRes = await fetch(BASE_URL);
        const booksData = await booksRes.json();
        allBooks = booksData;
        for (const bookId in booksData) {
            const {author, title} = booksData[bookId];
            const tableRow = document.createElement('tr');
            const titleColumn = document.createElement('td');
            const authorColumn = document.createElement('td');
            const buttonsColumn = document.createElement('td');
            const editBtn = document.createElement('button');
            const deleteBtn = document.createElement('button');
            titleColumn.textContent = title;
            authorColumn.textContent = author;
            editBtn.textContent = 'Edit';
            deleteBtn.textContent = 'Delete';
            deleteBtn.id = bookId

            editBtn.addEventListener('click', () => {
                editBookId = bookId
                formHeader.textContent = 'Edit Form'
                submitBtn.textContent = 'Save'
                titleInput.value = title
                authorInput.value = author
            })

            deleteBtn.addEventListener('click', deleteBookHandler)

            tableRow.appendChild(titleColumn);
            tableRow.appendChild(authorColumn);
            buttonsColumn.appendChild(editBtn);
            buttonsColumn.appendChild(deleteBtn);
            tableRow.appendChild(buttonsColumn);
            booksContainer.appendChild(tableRow);
        }
    }

    async function submitFormHandler(event) {
        // Ако елемента с id form е form елемент,
        // при опит да се добави книга щеше да рефрешва страницата и нямаше да работи
        // решението е да се добави .preventDefault =>
        // event.preventDefault() - премахва дефолтното рефрешване
        // в случая елемента е div и нямаме този проблем

        const title = titleInput.value;
        const author = authorInput.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({title, author})
        };
        let url = BASE_URL

        if (formHeader.textContent === 'Edit FORM'){
            httpHeaders.method = 'PUT'
            url += editBookId
        }

        const resData = await fetch(url, httpHeaders);
        loadAllBooksHandler();
        if (formHeader.textContent === 'Edit FORM'){
            formHeader.textContent = 'FORM'
            submitBtn.textContent = 'Submit'
        }
        titleInput.value = '';
        authorInput.value = '';
    }

    async function deleteBookHandler() {
        const id = this.id
        const httpHeaders = {
            method: 'DELETE',
        }
        await fetch(BASE_URL + id, httpHeaders)
        loadAllBooksHandler()
    }

}

attachEvents();