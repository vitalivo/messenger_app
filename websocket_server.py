import asyncio
import websockets
import json

connected_clients = {}

async def handler(websocket):
    try:
        print("New client connected")
        async for message in websocket:
            try:
                print("Received message:", message)
                data = json.loads(message)
                chat_id = data.get('chat_id')
                content = data.get('content')
                sender = data.get('sender')

                if chat_id not in connected_clients:
                    connected_clients[chat_id] = set()

                connected_clients[chat_id].add(websocket)

                # Отправка сообщения всем клиентам в чате
                for client in connected_clients[chat_id]:
                    if client != websocket:
                        await client.send(json.dumps({
                            'chat_id': chat_id,
                            'content': content,
                            'sender': sender
                        }))
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
            except Exception as e:
                print(f"Error processing message: {e}")
    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Client disconnected")
        for chat_id in connected_clients:
            connected_clients[chat_id].discard(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Бесконечный цикл

asyncio.run(main())