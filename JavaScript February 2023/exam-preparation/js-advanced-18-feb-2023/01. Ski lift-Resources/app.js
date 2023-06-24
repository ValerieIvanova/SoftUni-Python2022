window.addEventListener('load', solve);

function solve() {
    const inputFields = {
        firstName: document.getElementById('first-name'),
        lastName: document.getElementById('last-name'),
        numberOfPeople: document.getElementById('people-count'),
        fromDate: document.getElementById('from-date'),
        numberOfDays: document.getElementById('days-count')
    };
    const form = document.querySelector("#append-ticket > div > div > form");
    const nextStepBtn = document.getElementById('next-btn');
    const ticketInfoList = document.querySelector('.ticket-info-list')
    const confirmTicketList = document.querySelector('.confirm-ticket')

    nextStepBtn.addEventListener("click", getInfoHandler)

    function getInfoHandler(e){
        e.preventDefault()
        if (!inputFields.firstName.value || !inputFields.lastName.value || !inputFields.numberOfPeople.value || !inputFields.fromDate.value || !inputFields.numberOfDays.value) {
            return;
        }

        const liParent = createElement('li', ticketInfoList, null, ['ticket'], null, null,null)
        const article = createElement('article', liParent, null,null,null,null,null)
        const name = createElement('h3', article, `Name: ${inputFields.firstName.value} ${inputFields.lastName.value}`, null,null,null,null)
        const fromDate = createElement('p', article, `From date: ${inputFields.fromDate.value}`, null,null,null,null)
        const numberOfDays = createElement('p', article, `For ${inputFields.numberOfDays.value} days`, null,null,null,null)
        const numberOfPeople = createElement('p', article, `For ${inputFields.numberOfPeople.value} people`, null,null,null,null)
        const editBtn = createElement('button', liParent, 'Edit', ['edit-btn'], null,null,null)
        const continueBtn = createElement('button', liParent, 'Continue', ['continue-btn'], null,null,null)

        form.reset()
        nextStepBtn.disabled = true
        editBtn.disabled = false
        continueBtn.disabled = false

        editBtn.addEventListener('click', editHandler)
        continueBtn.addEventListener('click', continueHandler)

        function editHandler(){
            nextStepBtn.disabled = false
            inputFields.firstName.value = name.textContent.split(': ')[1].split(" ")[0]
            inputFields.lastName.value = name.textContent.split(': ')[1].split(' ')[1]
            inputFields.numberOfPeople.value = numberOfPeople.textContent.split(' ')[1]
            inputFields.fromDate.value = fromDate.textContent.split(': ')[1]
            inputFields.numberOfDays.value = numberOfDays.textContent.split(' ')[1]
            liParent.remove()
        }

        function continueHandler(){
            liParent.className = 'ticket-content'
            editBtn.remove()
            continueBtn.remove()
            const confirmBtn = createElement('button', liParent, 'Confirm', ['confirm-btn'], null,null,null)
            const cancelBtn = createElement('button', liParent, 'Cancel', ['cancel-btn'], null,null,null)
            confirmTicketList.appendChild(liParent)

            confirmBtn.addEventListener('click', confirmHandler)
            cancelBtn.addEventListener('click', cancelHandler)

            function cancelHandler(){
                liParent.remove()
                nextStepBtn.disabled = false
            }
            function confirmHandler(){
                const divElement = document.getElementById('main')
                const bodyElement = document.getElementById('body')
                divElement.remove()
                createElement('h1', bodyElement, 'Thank you, have a nice day!', null,'thank-you,')
                const backBtn = createElement('button',bodyElement, 'Back', null, 'back-btn', null, null)
                backBtn.addEventListener('click', () => {
                    location.reload()
                })

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


    
    
