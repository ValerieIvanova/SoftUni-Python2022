function oddAndEvenSum(number){
    let evenSum = 0
    let oddSum = 0

    number = number.toString().split('');

    for (let i = 0; i < number.length; i++) {
        if (number[i] % 2 === 0){
            evenSum += Number(number[i])
        }else{
            oddSum += Number(number[i])
        }
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}

console.log(oddAndEvenSum(1000435));
