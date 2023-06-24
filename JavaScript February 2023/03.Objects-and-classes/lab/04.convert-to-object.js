function convertToObj(jsonString){
    let data = JSON.parse(jsonString)

    for (key in data) {
        console.log(`${key}: ${data[key]}`);
    }
}

convertToObj('{"name": "George", "age": 40, "town": "Sofia"}')