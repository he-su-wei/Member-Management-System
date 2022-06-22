import json as JSON
import asyncio
import websockets
import sendMail
import json

async def echo(websocket):
    async for message in websocket:
        await websocket.send("server : " + JSON.dumps(message))
        print("client : " + message)

        data = json.loads(message)
        mail = data["userEmail"]
        randomNum = data["randonNum"]
        sendMail.mail(mail, randomNum)

async def main():
    async with websockets.serve(echo, "localhost", 5268):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())