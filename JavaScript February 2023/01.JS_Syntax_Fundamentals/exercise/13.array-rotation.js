function arrayRotation(arr, rotations) {
    for (let i = 0; i < rotations; i++) {
        arr.push(arr.shift())
    }
    console.log(arr.join(' '))
}


arrayRotation([51, 47, 32, 61, 21], 2)
arrayRotation([32, 21, 61, 1], 4)