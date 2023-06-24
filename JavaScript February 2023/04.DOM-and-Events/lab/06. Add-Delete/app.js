function addItem() {
    const ul = document.getElementById('items');
    const input = document.getElementById('newItemText');
    const newLi = document.createElement('li');
    const newAnchor = document.createElement('a')
    newLi.textContent = input.value;
    newAnchor.textContent = '[Delete]';
    newAnchor.href = '#'
    newAnchor.addEventListener('click', deleteHandler)
    newLi.appendChild(newAnchor);
    ul.appendChild(newLi);
    input.value = '';

    function deleteHandler(e) {
        const liItem = e.currentTarget.parentElement;
        liItem.remove()
    }
}