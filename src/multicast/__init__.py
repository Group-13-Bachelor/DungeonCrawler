import asyncio

from multicast.reciever import Reciever


async def networking():
    reciever = Reciever()
    await reciever.start_server()
    print("test")
    await asyncio.sleep(3600)   # Wait 1 hour


if __name__ == '__main__':
    asyncio.run(networking())
