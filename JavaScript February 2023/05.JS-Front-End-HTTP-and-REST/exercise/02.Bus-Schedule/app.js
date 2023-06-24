function solve() {
    const departBtn = document.getElementById('depart');
    const arriveBtn = document.getElementById('arrive');
    const busStopInfo = document.querySelector('#info > .info');
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/';

    let busStopId = 'depot';
    let busStopName = null;

    async function depart() {
        try {
            const response = await fetch(`${BASE_URL}${busStopId}`);
            const data = await response.json();
            busStopName = data.name;
            busStopInfo.textContent = `Next stop ${busStopName}`;
            busStopId = data.next;
            arriveBtn.disabled = false;
            departBtn.disabled = true;
        } catch (e) {
            busStopInfo.textContent = 'Error';
            arriveBtn.disabled = true;
            departBtn.disabled = true;
        }
    }

    async function arrive() {
        arriveBtn.disabled = true;
        departBtn.disabled = false;
        busStopInfo.textContent = `Arriving at ${busStopName}`;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();