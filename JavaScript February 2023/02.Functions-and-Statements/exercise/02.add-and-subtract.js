function addAndSubtract(...numbers) {
    const sum = (a, b) => a + b;
    const subtract = (a, b, c) => sum(a, b) - c;

    return subtract(...numbers)
}

console.log(addAndSubtract(23,6,10));