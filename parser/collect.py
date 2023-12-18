import asyncio
import logging
from db_utils import save_to_mongo
from services import dangerous_news_guardian


async def main():
    logging.error('Service initialized')

    while True:
        logging.error('Another cycle started')

        try:
            news = dangerous_news_guardian()

            # await save_to_mongo(news)

            print(news)
        except Exception as e:
            logging.error(f'Failed to save news to mongo, error: {e}')

        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
