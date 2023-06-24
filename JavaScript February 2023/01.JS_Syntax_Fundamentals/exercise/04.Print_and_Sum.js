function printAndSum(start, end){
    let sum = 0;
    let output = [];
    for (let i = start; i <= end; i++) {
        output.push(i)
        sum += i
    }

    console.log(`${output.join(' ')}`);
    console.log(`Sum: ${sum}`);
}

printAndSum(5, 10)