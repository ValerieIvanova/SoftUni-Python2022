function orders(item, quantity){
    let prices = {
        'water': 1,
        'coffee': 1.5,
        'coke': 1.4,
        'snacks': 2
    }

    console.log((prices[item] * quantity).toFixed(2));
}

orders('water', 5)
orders('coffee', 2)