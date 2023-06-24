function meetings(input) {
    let schedule = {}
    for (const line of input) {
        let [ day, name ] = line.split(' ')
        if (!schedule.hasOwnProperty(day)){
            schedule[day] = name
            console.log(`Scheduled for ${day}`);
        }else {
            console.log(`Conflict on ${day}!`);
        }
    }
    for (const key in schedule) {
        console.log(`${key} -> ${schedule[key]}`);
    }
}

meetings(['Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim']
)