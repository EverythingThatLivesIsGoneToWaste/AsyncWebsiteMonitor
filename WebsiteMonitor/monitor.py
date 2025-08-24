import asyncio
import aiohttp
from checker import check_site
from config import WEBSITES


class WebsiteMonitor:
    def __init__(self):
        self.results = []

    async def check_all_websites(self):
        """Проверяет все вебсайты из списка в конфиге"""
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in WEBSITES:
                task = asyncio.create_task(check_site(session, url))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            self.results = results
            return results

    def print_results(self):
        """Выводит результаты в консоль"""
        print(f"\nComplete: {self.results[0]['timestamp']}")
        print(f"{'=' * 50}")

        for result in self.results:
            if result['success']:
                status = "✅ OK" if result['status'] == 200 else "⚠️ WARN"
                print(f"{status} {result['url']} - {result['status']} ({result['response_time']}s)")
            else:
                print(f"❌ FAIL {result['url']} - {result['error']}")
