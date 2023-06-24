function focused() {
    const inputFields = document.querySelectorAll('input');

    for (const input of inputFields) {
        input.addEventListener('focus', function () {
            let parentDiv = this.parentNode;
            while (parentDiv && parentDiv.tagName !== 'DIV') {
                parentDiv = parentDiv.parentNode;
            }
            if (parentDiv) {
                parentDiv.classList.add('focused');
            }
        });

        input.addEventListener('blur', function () {
            let parentDiv = this.parentNode;
            while (parentDiv && parentDiv.tagName !== 'DIV') {
                parentDiv = parentDiv.parentNode;
            }
            if (parentDiv) {
                parentDiv.classList.remove('focused');
            }
        });
    }
}