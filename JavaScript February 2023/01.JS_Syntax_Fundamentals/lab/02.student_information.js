function censoredWords(text, word){
    let censored = text.replace(word, repeat(word));

    while (censored.includes(word)){
        censored = censored.replace(word, repeat(word));
    }

    function repeat(word){
        let stars = ''

        for (i=0; i<word.lenght; i++)[
            stars += '*'
        ]
        return stars
    }

    console.log(censored)
}

censoredWords('A small sentence with some words', 'small')