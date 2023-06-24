function isPerfect(number) {
    let divisors = []

    for (let i = 1; i < number; i++){
        if (number % i === 0){
            divisors.push(i)
        }
    }
    let divisorsSum = divisors.reduce((previousValue, currentValue) => {
        return previousValue + currentValue
    }, 0)

    if (divisorsSum === number) {
        console.log('We have a perfect number!');
    }else {
        console.log("It's not so perfect.");
    }
}

isPerfect(6)
isPerfect(28)
isPerfect(1236498)