function solve() {
    const listOfMails = document.getElementById('list')
    const sentList = document.querySelector('.sent-list')
    const deletedMails = document.querySelector('.delete-list')

    const inputFields = {
        recipient: document.getElementById('recipientName'),
        title: document.getElementById('title'),
        message: document.getElementById('message')
    }

    const addBtn = document.getElementById('add')
    const resetBtn = document.getElementById('reset')

    addBtn.addEventListener("click", addMail)
    resetBtn.addEventListener("click", resetForm)

    function addMail(e){
        e.preventDefault()

        if (!inputFields.recipient.value || !inputFields.title.value || !inputFields.message.value){
            return
        }

        const liParent = createElement('li', listOfMails, '', '', '', '', '')
        const title = createElement('h4', liParent, `Title: ${inputFields.title.value}`)
        const recipient = createElement('h4', liParent, `Recipient Name: ${inputFields.recipient.value}`)
        createElement('span', liParent, `${inputFields.message.value}`)
        const buttonsParent = createElement('div', liParent, '', '', 'list-action')
        const sendBtn = createElement('button', buttonsParent, 'Send', '','send', '', '')
        sendBtn.type = 'submit'
        sendBtn.addEventListener('click', sendHandler)

        resetForm(e)

        const deleteBtn = createElement('button', buttonsParent, 'Delete', '', 'delete', '', '')
        deleteBtn.type = 'submit'
        deleteBtn.addEventListener('click', () => {
            liParent.remove()
            deleteMails()
        })

        function sendHandler(e) {
            e.preventDefault()
            liParent.remove()
            const li = createElement('li', sentList, null, null, null, null, null)
            createElement('span', li, `To: ${recipient.textContent.split(': ')[1]}`)
            createElement('span', li, `Title: ${title.textContent.split(': ')[1]}`)
            const div = createElement('div', li, null,['btn'], null, null,null)
            const deleteButton = createElement('button', div, 'Delete', ['delete'], null,{ type: 'submit' }, null)

            deleteButton.addEventListener('click', () => {
                li.remove()
                deleteMails()
            })
        }

        function deleteMails(e){
            if (e){
                e.preventDefault()
            }

            const li = createElement('li', deletedMails, null, null, null, null, null)
            createElement('span', li, `To: ${recipient.textContent.split(': ')[1]}`)
            createElement('span', li, `Title: ${title.textContent.split(': ')[1]}`)
        }
    }

    function resetForm(e){
        e.preventDefault()
        inputFields.recipient.value = ''
        inputFields.title.value = ''
        inputFields.message.value = ''
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
solve()