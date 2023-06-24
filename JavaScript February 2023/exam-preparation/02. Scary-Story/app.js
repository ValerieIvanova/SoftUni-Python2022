// window.addEventListener("load", solve);
//
// function solve() {
//     const storyState = {
//         firstName: null,
//         lastName: null,
//         age: null,
//         title: null,
//         genre: null,
//         story: null
//     };
//     const inputDOMSelectors = {
//         firstName: document.getElementById('first-name'),
//         lastName: document.getElementById('last-name'),
//         age: document.getElementById('age'),
//         title: document.getElementById('story-title'),
//         genre: document.getElementById('genre'),
//         story: document.getElementById('story')
//     };
//
//     const otherDOMSelectors = {
//         publishBtn: document.getElementById('form-btn'),
//         previewList: document.getElementById('preview-list'),
//         mainContainer: document.getElementById('main')
//     };
//
//     otherDOMSelectors.publishBtn.addEventListener("click", publishStoryHandler);
//
//     function publishStoryHandler(event) {
//         const allFieldsHaveValue = Object.values(inputDOMSelectors)
//             .every((input) => input.value !== '');
//
//         if (!allFieldsHaveValue) {
//             return;
//         }
//
//         const {firstName, lastName, age, title, genre, story} = inputDOMSelectors;
//         const li = createElement('li', otherDOMSelectors.previewList, null, ['story-info']);
//         const article = createElement('article', li);
//         createElement('h4', article, `Name: ${firstName.value} ${lastName.value}`);
//         createElement('p', article, `Age: ${age.value}`);
//         createElement('p', article, `Title: ${title.value}`);
//         createElement('p', article, `Genre: ${genre.value}`);
//         createElement('p', article, story.value);
//         const saveBtn = createElement('button', li, 'Save Story', ['save-btn']);
//         const editBtn = createElement('button', li, 'Edit Story', ['edit-btn']);
//         const deleteBtn = createElement('button', li, 'Delete Story', ['delete-btn']);
//
//         editBtn.addEventListener('click', editStoryHandler)
//         deleteBtn.addEventListener('click', deleteStoryHandler)
//         saveBtn.addEventListener('click', saveStoryHandler)
//
//         for (const key in inputDOMSelectors) {
//             storyState[key] = inputDOMSelectors[key].value;
//         }
//
//         clearAllInputs()
//         otherDOMSelectors.publishBtn.setAttribute('disabled', true)
//     }
//
//     function saveStoryHandler() {
//         otherDOMSelectors.mainContainer.innerHTML = ''
//         createElement('h1', otherDOMSelectors.mainContainer, 'Your scary story is saved!')
//     }
//     function editStoryHandler() {
//         for (const key in inputDOMSelectors) {
//             inputDOMSelectors[key].value = storyState[key];
//         }
//
//         otherDOMSelectors.publishBtn.removeAttribute('disabled')
//         otherDOMSelectors.previewList.innerHTML = '';
//         createElement('h3', otherDOMSelectors.previewList, 'Preview');
//
//     }
//
//     function deleteStoryHandler(event){
//         const liItem = event.currentTarget.parentNode
//         liItem.remove()
//         otherDOMSelectors.publishBtn.removeAttribute('disabled')
//     }
//     function clearAllInputs() {
//         Object.values(inputDOMSelectors)
//             .forEach((input) => {
//                 input.value = '';
//             });
//     }
//     function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
//         const htmlElement = document.createElement(type);
//
//         if (content && useInnerHtml) {
//             htmlElement.innerHTML = content;
//         } else {
//             if (content && type !== 'input') {
//                 htmlElement.textContent = content;
//             }
//
//             if (content && type === 'input') {
//                 htmlElement.value = content;
//             }
//         }
//
//         if (content && type !== 'input') {
//             htmlElement.textContent = content;
//         }
//
//         if (content && type === 'input') {
//             htmlElement.value = content;
//         }
//
//         if (id) {
//             htmlElement.id = id;
//         }
//
//         // ['list', 'item']
//         if (classes) {
//             htmlElement.classList.add(...classes);
//         }
//
//         if (attributes) {
//             for (const key in attributes) {
//                 htmlElement.setAttribute(key, attributes[key]);
//             }
//         }
//
//         if (parentNode) {
//             parentNode.appendChild(htmlElement);
//         }
//
//         return htmlElement;
//     }
// }


window.addEventListener("load", solve);

function solve() {
    const inputFields = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        age: document.getElementById('age'),
        genre: document.getElementById('genre'),
        storyTitle: document.getElementById("story-title"),
        storyText: document.getElementById('story')
    };

    let publishBtn = document.getElementById('form-btn');
    let previewList = document.getElementById('preview-list');
    let form = document.querySelector("#main > div.form-wrapper > form");

    const values = {
        firstName: null,
        lastName: null,
        age: null,
        genre: null,
        storyTitle: null,
        storyText: null
    };

    publishBtn.addEventListener("click", publishHandler);

    function publishHandler() {
        if (!inputFields.firstName.value || !inputFields.lastName.value || !inputFields.age.value || !inputFields.storyTitle.value || !inputFields.storyText.value) {
            return;
        }

        const li = createElements('li', previewList, '', ['story-info'], '', '', '');
        const article = createElements('article', li, '', '', '', '', '');
        createElements('h4', article, `Name: ${inputFields.firstName.value} ${inputFields.lastName.value}`, '', '', '', '');
        createElements('p', article, `Age: ${inputFields.age.value}`, '', '', '', '');
        createElements('p', article, `Title: ${inputFields.storyTitle.value}`, '', '', '', '');
        createElements('p', article, `Genre: ${inputFields.genre.value}`, '', '', '', '');
        createElements('p', article, `${inputFields.storyText.value}`, '', '', '', '');

        for (const key in values) {
            values[key] = inputFields[key].value;
        }

        const saveBtn = createElements('button', li, 'Save Story', ['save-btn'], '', '', '');
        const editBtn = createElements('button', li, 'Edit Story', ['edit-btn'], '', '', '');
        const deleteBtn = createElements('button', li, 'Delete Story', ['delete-btn'], '', '', '');

        publishBtn.disabled = true;
        saveBtn.disabled = false;
        editBtn.disabled = false;
        deleteBtn.disabled = false;
        form.reset();

        saveBtn.addEventListener('click', saveStoryHandler);
        editBtn.addEventListener('click', () => {
            saveBtn.disabled = true;
            editBtn.disabled = true;
            deleteBtn.disabled = true;
            publishBtn.disabled = false;
            li.remove();
            editStoryHandler();
        });
        deleteBtn.addEventListener('click', () => {
            li.remove();
            publishBtn.disabled = false;
        });
    }

    function saveStoryHandler() {
        const mainDivContainer = document.getElementById('main');
        mainDivContainer.innerHTML = '';
        createElements('h1', mainDivContainer, 'Your scary story is saved!', '', '', '', '');
    }

    function editStoryHandler() {
        for (const key in inputFields) {
            inputFields[key].value = values[key];
        }
    }

    function createElements(type, parentNode, content, classes, id, attributes, useInnerHtml) {
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