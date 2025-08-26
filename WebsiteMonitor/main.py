import asyncio
from monitor import WebsiteMonitor
from config import CHECK_INTERVAL


async def main():

    monitor = WebsiteMonitor()
    print("\nMonitoring in process...\n")

    try:
        while True:
            await monitor.check_all_websites()
            monitor.print_results()

            await asyncio.sleep(CHECK_INTERVAL)

    except (Exception, asyncio.CancelledError) as e:
        print(f"\nMonitoring stopped.\n{str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
