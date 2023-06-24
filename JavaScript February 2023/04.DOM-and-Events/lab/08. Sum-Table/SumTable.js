function sumTable() {
    const table = document.querySelector('table');
    const rows = table.rows;
    let total = 0;

    for (let i = 1; i < rows.length - 1; i++) {
        const cell = rows[i].cells[1];
        const value = Number(cell.textContent);
        total += value;
    }

    const sumElement = document.getElementById('sum');
    sumElement.textContent = total.toFixed(2);
}