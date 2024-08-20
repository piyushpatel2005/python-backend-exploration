# name: str = "FastAPI"
# name = False

import asyncio

async def wait():
    print("waiting...")
    return

print('hello')
asyncio.run(wait())
print('world')
