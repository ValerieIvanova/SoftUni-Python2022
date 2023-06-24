function modernTimes(text) {
  let words = text.split(" ");
  let result = [];
  for (const word of words) {
    if (word.startsWith("#") && word.length > 1 && checkIfWordIsValid(word)) {
      result.push(word.slice(1));
    }
  }

  console.log(result.join("\n"));

  function checkIfWordIsValid(myWord) {
    let myWordLowercase = myWord.toLowerCase().slice(1);
    let isValid = true;

    for (const symbol of myWordLowercase) {
      let asciicode = symbol.charCodeAt(0);
      if (!(asciicode >= 97 && asciicode <= 122)) {
        isValid = false;
        break;
      }
    }
    return isValid;
  }
}

modernTimes("Nowadays everyone uses # to tag a #special word in #socialMedia");
