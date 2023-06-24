function store(stock, orderedStock) {
    let combinedStocks = [...stock, ...orderedStock];
    let storeProvision = {};

    for (let i = 0; i < combinedStocks.length; i++) {
        if (i % 2 === 0) {
            if (!storeProvision.hasOwnProperty(combinedStocks[i])) {
                storeProvision[combinedStocks[i]] = 0;
            }
        } else {
            storeProvision[combinedStocks[i - 1]] += Number(combinedStocks[i]);
        }
    }
    for (const key in storeProvision) {
        console.log(`${key} -> ${storeProvision[key]}`);
    }
}

store([
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
);