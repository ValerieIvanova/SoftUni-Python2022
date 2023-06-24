function checkSameDigits(number) {
  // Convert the number to a string to access each digit individually
  const numberStr = number.toString();

  // Check if all digits are the same
  const firstDigit = numberStr[0];
  const allSameDigits = numberStr
    .split("")
    .every((digit) => digit === firstDigit);

  // Compute the sum of all digits
  const digitSum = numberStr
    .split("")
    .reduce((acc, digit) => acc + Number(digit), 0);

  // Print the results on the console
  console.log(allSameDigits);
  console.log(digitSum);
}

checkSameDigits(2222222);
