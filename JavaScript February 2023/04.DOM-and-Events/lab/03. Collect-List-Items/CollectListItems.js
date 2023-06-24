function extractText() {
    const lists = Array.from(document.querySelectorAll('#items > li'));
    const textArea = document.getElementById('result')
    lists
        .forEach((li) => {
        textArea.textContent += li.textContent + '\n';
    })
}