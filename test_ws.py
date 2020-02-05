import uvloop
import asyncio
import websockets


async def main():
    uri = [
        # 'ws://0.0.0.0:8080/ws',
        "wss://stream.binance.com/stream?streams=btcusdt@kline_1m",
        # "wss://stream.binance.com/stream?streams=ethbtc@kline_1m",
        # "wss://stream.binance.com/stream?streams=bnbbtc@kline_1m"
    ]
    ws = await websockets.connect(uri[0])
    try:
        while True:
            await ws.send('')
            greeting = await ws.recv()
            print(f"< {greeting}")
    except KeyboardInterrupt:
        print('Close by user')
    finally:
        await ws.close()


uvloop.install()
asyncio.run(main())
