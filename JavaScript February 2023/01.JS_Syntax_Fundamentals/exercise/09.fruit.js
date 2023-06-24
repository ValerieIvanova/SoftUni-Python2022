function fruits(typeOfFruit, grams, pricePerKilogram) {
    let weight = grams / 1000
    let money = weight * pricePerKilogram
    console.log(`I need $${money.toFixed(2)} to buy ${weight.toFixed(2)} kilograms ${typeOfFruit}.`)
}

fruits('orange', 2500, 1.80)