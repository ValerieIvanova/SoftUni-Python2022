function roadRadar(speed, area) {
    let areaLimits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20
    }

    if (speed <= areaLimits[area]) {
        console.log(`Driving ${speed} km/h in a ${areaLimits[area]} zone`)
    } else {
        let status = '';
        let difference = speed - areaLimits[area];
        
        if (difference <= 20){
            status = 'speeding'
        } else if (difference <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${areaLimits[area]} - ${status}`)
    }
}

roadRadar(40, 'city')
roadRadar(21, 'residential')