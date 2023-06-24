// function attachEvents() {
//     const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
//     const titleInput = document.getElementById('title');
//     const loadBtn = document.getElementById('load-button');
//     const addBtn = document.getElementById('add-button');
//     const todoListContainer = document.getElementById('todo-list');
//
//     loadBtn.addEventListener("click", loadTasksHandler);
//     addBtn.addEventListener("click", addTaskHandler);
//
//     function loadTasksHandler(event) {
//         if (event) {
//             event.preventDefault();
//         }
//
//         todoListContainer.innerHTML = '';
//         fetch(BASE_URL)
//             .then((data) => data.json())
//             .then((tasksRes) => {
//                 const tasks = Object.values(tasksRes);
//
//                 for (const {_id, name} of tasks) {
//                     const li = document.createElement('li');
//                     const span = document.createElement('span');
//                     const removeBtn = document.createElement('button');
//                     const editBtn = document.createElement('button');
//
//                     li.id = _id;
//                     span.textContent = name;
//                     removeBtn.textContent = 'Remove';
//                     editBtn.textContent = 'Edit';
//
//                     editBtn.addEventListener("click", loadEditFormHandler);
//                     removeBtn.addEventListener("click", removeTaskHandler);
//
//                     li.append(span, removeBtn, editBtn);
//                     todoListContainer.appendChild(li);
//                 }
//             })
//             .catch((err) => {
//                 console.error(err);
//             });
//     }
//
//     function loadEditFormHandler(event) {
//         const liParent = event.currentTarget.parentNode;
//         const [span, _removeBtn, editBtn] = Array.from(liParent.children);
//         const editInput = document.createElement('input');
//         editInput.value = span.textContent;
//         liParent.prepend(editInput);
//         const submitBtn = document.createElement('button');
//         submitBtn.textContent = 'Submit';
//         submitBtn.addEventListener("click", submitTaskHandler);
//         liParent.appendChild(submitBtn);
//         span.remove();
//         editBtn.remove();
//     }
//
//     function submitTaskHandler(event) {
//         const liParent = event.currentTarget.parentNode;
//         const id = liParent.id;
//         const [input] = Array.from(liParent.children);
//         const httpHeaders = {
//             method: 'PATCH',
//             body: JSON.stringify({name: input.value})
//         };
//
//         fetch(`${BASE_URL}${id}`, httpHeaders)
//             .then(() => loadTasksHandler())
//             .catch((err) => {
//                 console.error(err);
//             });
//     }
//
//     function addTaskHandler(event) {
//         event.preventDefault();
//         const name = titleInput.value;
//         const httpHeaders = {
//             method: 'POST',
//             body: JSON.stringify({name})
//         };
//         fetch(BASE_URL, httpHeaders)
//             .then(() => {
//                 loadTasksHandler();
//                 titleInput.value = '';
//             })
//             .catch((err) => {
//                 console.error(err);
//             });
//
//     }
//
//     function removeTaskHandler(event) {
//         const id = event.currentTarget.parentNode.id;
//         const httpHeaders = {
//             method: 'DELETE',
//         };
//         fetch(`${BASE_URL}${id}`, httpHeaders)
//             .then(() => loadTasksHandler())
//             .catch((err) => {
//                 console.error(err);
//             });
//     }
// }
//
//
// attachEvents();


function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const toDoListContainer = document.getElementById('todo-list');
    const taskName = document.getElementById('title');
    const loadAllBtn = document.getElementById('load-button');
    const addTaskBtn = document.getElementById('add-button');

    loadAllBtn.addEventListener("click", loadAllHandler);
    addTaskBtn.addEventListener("click", addTaskHandler);

    function loadAllHandler(e) {
        if (e) {
            e.preventDefault();
        }

        toDoListContainer.innerHTML = ''
        fetch(BASE_URL)
            .then((data) => data.json())
            .then((taskRes) => {
                const tasks = Object.values(taskRes);

                for (const {name, _id} of tasks) {
                    const li = createElement('li', toDoListContainer, '', '', `${_id}`, '', '');
                    const span = createElement('span', li, `${name}`, '', '', '', '');
                    const removeBtn = createElement('button', li, 'Remove', '', '', '', '');
                    const editBtn = createElement('button', li, 'Edit', '', '', '', '');

                    removeBtn.addEventListener('click', removeTaskHandler)
                    editBtn.addEventListener('click', editTaskHandler)
                }
            })
            .catch((err) => {
                console.error(err);
            });
    }

    function addTaskHandler(e) {
        if (e){
            e.preventDefault();
        }
        const name = taskName.value;
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({name})
        };

        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadAllHandler();
                taskName.value = '';
            })
            .catch((err) => {
                console.error(err);
            });
    }

    function removeTaskHandler(e) {
        const taskId = e.currentTarget.parentNode.id

        const httpHeaders = {
            method: 'DELETE'
        }

        fetch(`${BASE_URL}${taskId}`, httpHeaders)
            .then(() => {
                loadAllHandler()
            })
            .catch((err) => {
                console.error(err);
            })
    }

    function editTaskHandler(e) {
        const liItem = e.currentTarget.parentNode
        const id = liItem.id
        const spanItem = liItem.children[0]
        const inpField = createElement('input', '', `${spanItem.textContent}`, '', '', '', '')
        const editBtn = liItem.children[2]
        liItem.prepend(inpField)
        const edited = liItem.children[0]

        const submitBtn = createElement('button', liItem, 'Submit', '', '', '', '')
        submitBtn.addEventListener('click', () => {
            const httpHeaders = {
                method: 'PATCH',
                body: JSON.stringify({name: edited.value})
            }

            fetch(`${BASE_URL}${id}`, httpHeaders)
                .then(() => {
                    loadAllHandler()
                })
                .catch((err) => {
                    console.error(err);
                })
        })

        spanItem.remove()
        editBtn.remove()
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

attachEvents();