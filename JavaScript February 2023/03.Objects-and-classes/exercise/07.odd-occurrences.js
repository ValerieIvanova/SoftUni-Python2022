function solve(string) {
    const arr = string.split(' ')
    const odds = {}

    for (const word of arr) {
        let wordLowered = word.toLowerCase()
        if (!odds[wordLowered]){
            odds[wordLowered] = 0
        }
        odds[wordLowered] ++
    }

    let result = []
    let sorted = Object.entries(odds).sort((a, b) => b[1] - a[1])
    for (const [key, value] of sorted) {
        if (value % 2 !== 0){
            result.push(key);
        }
    }

    console.log(result.join(' '));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')
// solve('Cake IS SWEET is Soft CAKE sweet Food')