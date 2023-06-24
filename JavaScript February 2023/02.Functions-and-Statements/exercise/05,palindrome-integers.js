function checkPalindromes(numbers) {
    for (let i = 0; i < numbers.length; i++) {
        let number = numbers[i];
        let reversedNumber = Number(number.toString().split('').reverse().join(''));
        if (number === reversedNumber) {
            console.log("true");
        } else {
            console.log("false");
        }
    }
}

checkPalindromes([123,323,421,121])