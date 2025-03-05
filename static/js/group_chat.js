const socket = new WebSocket('ws://localhost:8000/group_chat/');

socket.onopen = function(event) {
    console.log('Соединение установлено');
    socket.send('Привет, сервер!');
};

socket.onmessage = function(event) {
    console.log('Принято сообщение:', event.data);
    displayMessage(event.data);
};

socket.onerror = function(event) {
    console.log('Ошибка:', event);
};

socket.onclose = function(event) {
    console.log('Соединение закрыто');
};

document.querySelector('#chat-message-submit').addEventListener('click', function(event) {
    const messageInput = document.querySelector('#chat-message-input');
    const message = messageInput.value;
    socket.send(message);
    messageInput.value = '';
});

function displayMessage(message) {
    const chatLog = document.querySelector('#chat-log');
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatLog.appendChild(messageElement);
}