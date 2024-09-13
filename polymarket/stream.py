import json
import asyncio
import websockets
import datetime

url = 'wss://ws-subscriptions-clob.polymarket.com/ws/market'
last_time_pong = datetime.datetime.now()
msgs = []

kamala_trump_yes_token = "21742633143463906290569050155826241533067272736897614950488156847949938836455"



async def connect_and_listen():
    async with websockets.connect(url) as websocket:
        # Send initial subscription request
        await websocket.send(
            json.dumps({"assets_ids": [kamala_trump_yes_token], "type": "market"}))

        while True:
            m = await websocket.recv()

            if m != "PONG":
                last_time_pong = datetime.datetime.now()
            d = json.loads(m)
            print(d)

            if last_time_pong + datetime.timedelta(seconds=10) < datetime.datetime.now():
                await websocket.send("PING")
            else:
                msgs.append(d)


# The entry point for running the asyncio event loop
if __name__ == "__main__":
    asyncio.run(connect_and_listen())
