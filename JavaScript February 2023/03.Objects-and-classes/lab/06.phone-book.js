function phoneBook(info) {
    let phonebook = {};
    for (const line of info) {
        let [ name, phoneNumber ] = line.split(' ');
        if (!phonebook.hasOwnProperty(name)){
            phonebook[name] = phoneNumber
        }
    }

    for (const key in phonebook) {
        console.log(`${key} -> ${phonebook[key]}`);
    }
}

phoneBook(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
);