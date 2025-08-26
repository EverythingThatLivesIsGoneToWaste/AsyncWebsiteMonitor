from datetime import datetime
from config import TIMEOUT


async def check_site(session, url):
    """
    Проверяет доступность одного сайта
    """

    start_time = datetime.now()

    try:
        async with session.get(url, timeout=TIMEOUT) as response:
            end_time = datetime.now()
            response_time = (end_time - start_time).total_seconds()

            return {
                'url': url,
                'status': response.status,
                'response_time': round(response_time, 2),
                'start_time': start_time,
                'end_time': end_time,
                'success': True
            }

    except Exception as e:
        return {
            'url': url,
            'status': 'ERROR',
            'error': str(e),
            'start_time': start_time,
            'end_time': datetime.now(),
            'success': False
        }
