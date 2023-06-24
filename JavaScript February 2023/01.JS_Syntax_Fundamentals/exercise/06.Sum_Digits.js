function sumDigits(number) {
    let sum = 0;
    number = Array.from(number.toString()).map(Number);
    for (digit of number) {
        sum += digit
    }

    console.log(sum)
}


sumDigits(245678);