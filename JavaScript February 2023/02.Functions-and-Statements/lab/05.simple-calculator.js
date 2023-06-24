function calculator(num1, num2, operator) {
    const multiply = (a,b) => a * b
    const divide = (a,b) => a / b
    const add = (a,b) => a + b
    const subtract = (a,b) => a - b

    const operations = {
        add,
        subtract,
        divide,
        multiply
    }

    console.log(operations[operator](num1,num2));
}

calculator(5, 5, 'multiply');
calculator(40, 8, 'divide');
calculator(12, 19, 'add');
calculator(50, 13, 'subtract');


