import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 10000))
connected = set()

async def handler(websocket, path):
    print(f"[+] Client connected: {websocket.remote_address}")
    connected.add(websocket)
    try:
        async for message in websocket:
            # Relay the message to all *other* clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(message)
    except:
        pass
    finally:
        connected.remove(websocket)
        print(f"[-] Client disconnected: {websocket.remote_address}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"WebSocket relay running on port {PORT}")
        await asyncio.Future()  # Run forever

asyncio.run(main())
