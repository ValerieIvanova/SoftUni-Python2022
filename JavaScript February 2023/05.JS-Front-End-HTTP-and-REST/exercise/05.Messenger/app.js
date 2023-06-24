function attachEvents() {
    const sendButton = document.getElementById('submit')
    const refreshButton = document.getElementById('refresh')
    const [author, content] = Array.from(document.querySelectorAll('#controls > div > input'))
    const messages = document.getElementById('messages')
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger'

    sendButton.addEventListener('click', async () => {
        const authorName = author.value
        const contentValue = content.value

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({
                "author": authorName,
                "content": contentValue,
            })
        }
        const response = await fetch(BASE_URL, httpHeaders)

        author.value = ''
        content.value = ''
    })

    refreshButton.addEventListener('click', async () => {
        const response = await fetch(BASE_URL)
        const data = await response.json()

        let result = []

        for (const msg of Object.values(data)) {
            result.push(`${msg.author}: ${msg.content}`)
        }

        messages.textContent = result.join('\n')
    })
}

attachEvents();