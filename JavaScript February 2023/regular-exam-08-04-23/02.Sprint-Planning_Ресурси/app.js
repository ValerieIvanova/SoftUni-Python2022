window.addEventListener('load', solve);

function solve() {
    const inputFields = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        estimationPoints: document.getElementById('points'),
        assignee: document.getElementById('assignee')
    };
    let taskId = 0;
    const form = document.getElementById('create-task-form');
    const createTaskBtn = document.getElementById('create-task-btn');
    const deleteTaskBtn = document.getElementById('delete-task-btn');
    const tasksSection = document.getElementById('tasks-section');
    const totalPointsP = document.getElementById('total-sprint-points')
    let points = 0
    deleteTaskBtn.disabled = true;

    createTaskBtn.addEventListener("click", createHandler);

    function createHandler(e) {
        if (e) {
            e.preventDefault();
        }

        if (!inputFields.title.value || !inputFields.description.value || !inputFields.label.value || !inputFields.estimationPoints.value || !inputFields.assignee.value) {
            return;
        }
        taskId += 1;
        const iconObj = {
            'Feature': '&#8865',
            'Low Priority Bug': '&#9737',
            'High Priority Bug': '&#9888'
        };

        const newArticle = createElement('article', tasksSection, null, ['task-card'], `task-${taskId}`, null, null);

        if (inputFields.label.value === 'Feature') {
            newArticle.innerHTML = `<div class="task-card-label feature">${inputFields.label.value} ${iconObj[inputFields.label.value]}</div>`;
        } else if (inputFields.label.value === 'Low Priority Bug') {
            newArticle.innerHTML = `<div class="task-card-label low-priority">${inputFields.label.value} ${iconObj[inputFields.label.value]}</div>`;
        } else if (inputFields.label.value === 'High Priority Bug') {
            newArticle.innerHTML = `<div class="task-card-label high-priority">${inputFields.label.value} ${iconObj[inputFields.label.value]}</div>`;
        }

        const title = createElement('h3', newArticle, `${inputFields.title.value}`, ['task-card-title'], null, null, null);
        const description = createElement('p', newArticle, `${inputFields.description.value}`, ['task-card-description'], null, null, null);
        const estimated = createElement('div', newArticle, `Estimated at ${inputFields.estimationPoints.value} pts`, ['task-card-points'], null, null, null);
        const assigned = createElement('div', newArticle, `Assigned to: ${inputFields.assignee.value}`, ['task-card-assignee'], null, null, null);
        const actionsBtnDiv = createElement('div', newArticle, null, ['task-card-actions'], null, null, null);
        const deleteBtn = createElement('button', actionsBtnDiv, 'Delete', null, null, null, null);
        const label = inputFields.label.value;

        points += Number(inputFields.estimationPoints.value)
        totalPointsP.textContent = `Total Points ${points}pts`


        form.reset();
        deleteBtn.addEventListener('click', deleteTask);

        function deleteTask() {
            inputFields.title.value = title.textContent;
            inputFields.description.value = description.textContent;
            inputFields.label.value = label;
            inputFields.estimationPoints.value = estimated.textContent.split(' ')[2];
            inputFields.assignee.value = assigned.textContent.split(': ')[1];

            deleteTaskBtn.disabled = false;
            createTaskBtn.disabled = true;

            inputFields.title.disabled = true;
            inputFields.description.disabled = true;
            inputFields.label.disabled = true;
            inputFields.estimationPoints.disabled = true;
            inputFields.assignee.disabled = true;

            deleteTaskBtn.addEventListener("click", deleteHandler);

            function deleteHandler() {
                points -= Number(inputFields.estimationPoints.value)
                totalPointsP.textContent = `Total Points ${points}pts`
                newArticle.remove();
                form.reset();
                inputFields.title.disabled = false;
                inputFields.description.disabled = false;
                inputFields.label.disabled = false;
                inputFields.estimationPoints.disabled = false;
                inputFields.assignee.disabled = false;

                createTaskBtn.disabled = false;
                deleteTaskBtn.disabled = true;
            }

        }

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
