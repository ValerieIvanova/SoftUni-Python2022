// TODO:
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const loadBtn = document.getElementById('load-board-btn');
    const addTaskBtn = document.getElementById('create-task-btn');
    const toDoContainer = document.querySelector("#todo-section > ul");
    const inProgressContainer = document.querySelector("#in-progress-section > ul");
    const codeReviewContainer = document.querySelector("#code-review-section > ul");
    const doneContainer = document.querySelector("#done-section > ul");
    const inputFields = {
        title: document.getElementById('title'),
        description: document.getElementById('description')
    };
    loadBtn.addEventListener("click", loadTasksHandler);
    addTaskBtn.addEventListener("click", addTaskHandler);
    function addTaskHandler() {
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({
                title: inputFields.title.value,
                description: inputFields.description.value,
                status: 'ToDo'
            })
        };

        fetch(BASE_URL, httpHeaders)
            .then(() => {
                loadTasksHandler();
                inputFields.title.value = '';
                inputFields.description.value = '';
            })
            .catch((err) => {
                console.error(err);
            });

    }

    function loadTasksHandler(e) {
        if (e){
            e.preventDefault()
        }
        toDoContainer.innerHTML = '';
        inProgressContainer.innerHTML = '';
        codeReviewContainer.innerHTML = '';
        doneContainer.innerHTML = '';

        fetch(BASE_URL)
            .then((res) => res.json())
            .then((taskRes) => {
                const tasks = Object.values(taskRes);

                for (let {title, description, status, _id} of tasks) {
                    console.log(title, description,status,_id);
                    let parent = null;
                    if (status === 'ToDo') {
                        parent = toDoContainer;
                    } else if (status === 'In Progress') {
                        parent = inProgressContainer;
                    } else if (status === 'Code Review') {
                        parent = codeReviewContainer;
                    } else if (status === 'Done') {
                        parent = doneContainer;
                    }

                    const li = createElement('li', parent, null, ['task'], null, null, null);
                    createElement('h3', li, title, null, null, null, null);
                    createElement('p', li, description, null, null, null, null);
                    if (status === 'ToDo') {
                        const moveToInProgressBtn = createElement('button', li, 'Move to In Progress', null, null, null, null);
                        moveToInProgressBtn.addEventListener('click', moveToInProgressHandler);

                    } else if (status === 'In Progress') {
                        const moveToCodeReviewBtn = createElement('button', li, 'Move to Code Review', null, null, null, null);
                        moveToCodeReviewBtn.addEventListener('click', moveToCodeReviewHandler);

                    } else if (status === 'Code Review') {
                        const moveToDoneBtn = createElement('button', li, 'Move to Done', null, null, null, null);
                        moveToDoneBtn.addEventListener('click', moveToDoneHandler);

                    } else if (status === 'Done') {
                        const closeBtn = createElement('button', li, 'Close', null, null, null, null);
                        closeBtn.addEventListener('click', closeTaskHandler);
                    }
                }

                function moveToInProgressHandler(e) {
                    const id = e.currentTarget.parentNode.id;

                    const httpHeaders = {
                        method: 'PATCH',
                        body: JSON.stringify({status: 'In Progress'})
                    };

                    fetch(`${BASE_URL}${id}`, httpHeaders)
                        .then(() => loadTasksHandler(e))
                        .catch((err) => {
                            console.error(err);
                        });
                }

                function closeTaskHandler(e) {
                    const id = e.currentTarget.parentNode.id;
                    const httpHeaders = {
                        method: 'DELETE'
                    };

                    fetch(`${BASE_URL}${id}`, httpHeaders)
                        .then(() => loadTasksHandler(e))
                        .catch((err) => {
                            console.error(err);
                        });
                }

                function moveToCodeReviewHandler(e) {
                    const id = e.currentTarget.parentNode.id;
                    const httpHeaders = {
                        method: 'PATCH',
                        body: JSON.stringify({status: 'Code Review'})
                    };
                    fetch(`${BASE_URL}${id}`, httpHeaders)
                        .then(() => loadTasksHandler(e))
                        .catch((err) => {
                            console.error(err);
                        });
                }

                function moveToDoneHandler(e) {
                    const id = e.currentTarget.parentNode.id;
                    const httpHeaders = {
                        method: 'PATCH',
                        body: JSON.stringify({status: 'Done'})
                    };

                    fetch(`${BASE_URL}${id}`, httpHeaders)
                        .then(() => loadTasksHandler(e))
                        .catch((err) => {
                            console.error(err);
                        });
                }

            });

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
}

attachEvents();