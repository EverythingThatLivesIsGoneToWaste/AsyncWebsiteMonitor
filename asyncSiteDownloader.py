import asyncio
import time
import httpx
from typing import List

WEBSITES = [
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/xml",
    "https://httpbin.org/robots.txt",
]


async def download_site(url: str, client: httpx.AsyncClient) -> str:
    print(f"Начинаем скачивание: {url}")

    try:
        response = await client.get(url)
        size = len(response.text)
        print(f"Завершено: {url} ({size} символов)")
        return f"{url}: {size} символов"

    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")
        return f"{url}: ошибка"


async def download_all_sites_async(sites: List[str]) -> List[str]:

    async with httpx.AsyncClient() as client:
        tasks = []
        for site in sites:
            task = asyncio.create_task(download_site(site, client))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        return results


async def main():
    print(f"Скачиваем {len(WEBSITES)} сайтов...")

    start_time = time.time()
    async_results = await download_all_sites_async(WEBSITES)
    async_time = time.time() - start_time

    print(f"\nВремя: {async_time:.2f} секунд")

    # Вывод скачанных данных
    print(f"\nСкачанные данные:")
    for result in async_results:
        print(f"  {result}")

if __name__ == "__main__":
    asyncio.run(main())
