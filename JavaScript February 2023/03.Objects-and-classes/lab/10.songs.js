function solve(inputData) {
    let songs = [];
    const n = inputData.shift();
    const sortingType = inputData.pop();

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    for (let i = 0; i < n; i++) {
        let [type, name, time] = inputData[i].split('_');
        songs.push(new Song(type, name, time));
    }

    if (sortingType === 'all') {
        for (const song of songs) {
            console.log(song.name);
        }
    } else {
        for (const song of songs) {
            if (song.typeList === sortingType) {
                console.log(song.name);
            }
        }
    }

}

solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']);