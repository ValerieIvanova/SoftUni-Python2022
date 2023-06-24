function solve() {
    const searchInput = document.getElementById('searchField');
    document.querySelector('#searchBtn').addEventListener('click', onClick);

    function onClick() {
        const searchedWord = searchInput.value;
        const tableRows = Array.from(document.querySelectorAll('tbody tr'));
        for (const row of tableRows) {
            let trimmedContent = row.textContent.trim();
            if (row.classList.contains('select')) {
                row.classList.remove('select');
            }
            if (trimmedContent.includes(searchedWord)) {
                row.classList.add('select');
            }
        }
        searchInput.value = '';
    }
}