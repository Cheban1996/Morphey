import store from './store'

let socket = new WebSocket("ws://0.0.0.0:5000/ws");

console.log('Start listen websocket');

socket.onopen = function (e) {
    console.log("[open] Connect to websocket");
    socket.send("connect");
};

socket.onmessage = function (event) {
    store.commit('loadKlines', JSON.parse(event.data));
};

socket.onclose = function (event) {
    if (event.wasClean) {
        alert(`[close] Connection close, code=${event.code} reason=${event.reason}`);
    } else {
        // maybe code event.code 1006
        alert('[close] Connection close');
    }
};

socket.onerror = function (error) {
    alert(`[error] Close ${error.message}`);
};

