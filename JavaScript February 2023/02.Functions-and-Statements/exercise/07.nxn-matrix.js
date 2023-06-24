// const matrix = (n) => new Array(n).fill(new Array(n).fill(n)).forEach(row => console.log(row.join(' ')))
// console.log(matrix(3));


function matrix(number){
    let matrixOutput = []
    for (let i = 0; i < number; i++) {
        matrixOutput.push([])
        for (let j = 0; j < number; j++) {
            matrixOutput[i].push(number)
        }
    }

    for (let row = 0; row < number; row++)
        console.log(matrixOutput[row].join(' '));
}