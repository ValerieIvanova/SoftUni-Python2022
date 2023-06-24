function shoppingList(input) {
    let groceriesArr = input.shift().split('!');
    const commandsDict = {
        'Urgent': urgent,
        'Unnecessary': unnecessary,
        'Correct': correct,
        'Rearrange': rearrange
    };

    function urgent(item) {
        if (!groceriesArr.includes(item)) {
            groceriesArr.unshift(item);
        }
    }

    function unnecessary(item) {
        if (groceriesArr.includes(item)) {
            let idx = groceriesArr.indexOf(item)
            groceriesArr.splice(idx, 1);
        }
    }

    function correct(oldItem, newItem) {
        if (groceriesArr.includes(oldItem)) {
            let oldItemIdx = groceriesArr.indexOf(oldItem);
            groceriesArr[oldItemIdx] = newItem;
        }
    }

    function rearrange(item) {
        if (groceriesArr.includes(item)) {
            let idx = groceriesArr.indexOf(item)
            groceriesArr.splice(idx, 1)
            groceriesArr.push(item);
        }
    }

    for (let commandData of input) {
        if (commandData === 'Go Shopping!') {
            console.log(groceriesArr.join(', '));
            break;
        }

        commandData = commandData.split(' ')
        let command = commandData.shift();
        commandsDict[command](...commandData);
    }
}


shoppingList((["Tomatoes!Potatoes!Bread",
    "Unnecessary Milk",
    "Urgent Tomatoes",
    "Go Shopping!"])
);



shoppingList((["Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Unnecessary Grapes",
    "Correct Pepper Onion",
    "Rearrange Grapes",
    "Correct Tomatoes Potatoes",
    "Go Shopping!"])
);


