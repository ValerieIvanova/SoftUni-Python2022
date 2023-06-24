function loadingBar(num) {
    const percent = num / 10;
    const bar = '[' + '%'.repeat(percent) + '.'.repeat(10 - percent) + ']';
    return `${num}% ${bar}\nStill loading...`;
}

console.log(loadingBar(30));