import asyncio
import time


async def cook(name, cooking_time, waiting_time, finishing_time):
    print(f"{name} started cooking")
    await asyncio.sleep(cooking_time)
    print(f"{name} is waiting")
    await asyncio.sleep(waiting_time)
    print(f"{name} is finishing")
    await asyncio.sleep(finishing_time)

    print(f"{name} has finished")
    return f"{name} has successfully finished cooking"


async def async_kitchen():
    start = time.time()

    coroutine1 = cook("Повар 1", 1, 2, 1)
    coroutine2 = cook("Повар 2", 1, 3, 1)
    coroutine3 = cook("Повар 3", 2, 1, 1)

    print("Coroutines created, but not yet activated")
    results = await asyncio.gather(coroutine1, coroutine2, coroutine3, return_exceptions=True)
    end = time.time()
    print(f"[{end-start:.2f}]\nResults: {results}")

asyncio.run(async_kitchen())
