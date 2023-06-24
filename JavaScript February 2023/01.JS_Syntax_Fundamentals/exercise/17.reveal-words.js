function replaceWords(str, template) {
    let words = str.split(", ");
    let templateWords = template.split(" ");

    for (const word of words) {
        for (const tword of templateWords) {
            if (tword.includes("*") && tword.length === word.length) {
                template = template.replace(tword, word);
            }
        }
    }

    console.log(template);
}

replaceWords(
    "great, learning",
    "softuni is ***** place for ******** new programming languages"
);
