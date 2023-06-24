function pianoPieces(input) {
    let pieces = {}
    let n = Number(input.shift())
    let commandsRef = {
        'Add': add,
        'Remove': remove,
        'ChangeKey': changeKey
    }

    for (let i = 0; i < input.length; i++) {
        if (i < n) {
            let [piece, composer, key] = input[i].split("|")
            pieces[piece] = {composer, key}
        } else {
            if (input[i] === 'Stop'){
                break
            }

            let commandData = input[i].split("|")
            let command = commandData.shift()
            commandsRef[command](...commandData)
        }

    }

    function add(piece, composer, key){
        if (pieces.hasOwnProperty(piece)){
            console.log(`${piece} is already in the collection!`);
        } else {
            pieces[piece] = {composer, key}
            console.log(`${piece} by ${composer} in ${key} added to the collection!`);
        }
    }

    function remove(piece){
        if (pieces.hasOwnProperty(piece)){
            delete pieces[piece]
            console.log(`Successfully removed ${piece}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        }
    }

    function changeKey(piece, newKey){
        if (pieces.hasOwnProperty(piece)){
            pieces[piece].key = newKey
            console.log(`Changed the key of ${piece} to ${newKey}!`);
        } else {
            console.log(`Invalid operation! ${piece} does not exist in the collection.`);
        }
    }

    for (const piece in pieces) {
        console.log(`${piece} -> Composer: ${pieces[piece].composer}, Key: ${pieces[piece].key}`);
    }
}

pianoPieces([
        '3',
        'Fur Elise|Beethoven|A Minor',
        'Moonlight Sonata|Beethoven|C# Minor',
        'Clair de Lune|Debussy|C# Minor',
        'Add|Sonata No.2|Chopin|B Minor',
        'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
        'Add|Fur Elise|Beethoven|C# Minor',
        'Remove|Clair de Lune',
        'ChangeKey|Moonlight Sonata|C# Major',
        'Stop'
    ]
)