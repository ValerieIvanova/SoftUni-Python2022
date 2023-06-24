function charactersInRange(char1, char2){
    let maxNum = Math.max(char1.charCodeAt(0), char2.charCodeAt(0))
    let minNum = Math.min((char1.charCodeAt(0)), char2.charCodeAt(0))
    let output = ''
    for (let i = minNum+1; i < maxNum; i++) {
        output += String.fromCharCode(i) + ' '
    }

    console.log(output);
}

charactersInRange('a',
    'd'
)