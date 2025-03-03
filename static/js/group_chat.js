document.addEventListener('DOMContentLoaded', (event) => {
    const chatLog = document.getElementById('chat-log');
    const chatMessageInput = document.getElementById('chat-message-input');
    const chatMessageSubmit = document.getElementById('chat-message-submit');

    const chatSocket = new WebSocket('ws://localhost:8765/');

    chatSocket.onopen = function(e) {
        console.log('WebSocket connection opened');
    };

    chatSocket.onmessage = function(e) {
        try {
            const data = JSON.parse(e.data);
            const message = `${data.sender}: ${data.content}\n`;
            chatLog.innerText += message;
        } catch (error) {
            console.error('Error parsing message:', error);
        }
    };

    chatSocket.onerror = function(e) {
        console.error('WebSocket error:', e);
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly:', e);
    };

    chatMessageSubmit.onclick = function(e) {
        const message = chatMessageInput.value;
        const chatId = 'some_chat_id'; // Замените на реальный chat_id
        const sender = 'some_sender'; // Замените на реального отправителя

        if (chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({
                'chat_id': chatId,
                'content': message,
                'sender': sender
            }));
            chatMessageInput.value = '';
        } else {
            console.error('WebSocket is not open. ReadyState:', chatSocket.readyState);
        }
    };
});