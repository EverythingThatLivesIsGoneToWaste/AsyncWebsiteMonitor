import asyncio
import aiohttp
from checker import check_site
from config import WEBSITES, MAX_CONCURRENT_REQUESTS


class WebsiteMonitor:
    def __init__(self):
        self.results = []

    async def check_all_websites(self):
        """Проверяет все вебсайты из списка в конфиге"""
        connector = aiohttp.TCPConnector(
            limit=MAX_CONCURRENT_REQUESTS,
            limit_per_host=5,
            ttl_dns_cache=300,
            enable_cleanup_closed=True)

        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for url in WEBSITES:
                task = asyncio.create_task(check_site(session, url))
                tasks.append(task)

            results = await asyncio.gather(*tasks)
            self.results = results
            return results

    def print_results(self):
        """Выводит результаты в консоль"""
        if not self.results:
            print("No results")
            return

        start_times = [result['start_time'] for result in self.results]
        end_times = [result['end_time'] for result in self.results]

        overall_start = min(start_times)
        overall_end = max(end_times)
        total_duration = (overall_end - overall_start).total_seconds()

        print(f"Start:   {overall_start}")
        print(f"End:     {overall_end}")
        print(f"Overall: {total_duration:.2f} seconds")
        print(f"{'=' * 50}")

        max_url_length = max(len(result['url']) for result in self.results)

        for result in self.results:
            if result['success']:
                status = "✅ OK  " if result['status'] == 200 else "⚠️ WARN"
                print(f"{status} {result['url'].ljust(max_url_length)} - {result['status']} ({result['response_time']}s)")
            else:
                print(f"❌ FAIL {result['url'].ljust(max_url_length)} - {result['error']}")
        print()
