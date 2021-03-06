# import time
#
# import aiohttp
# import asyncio
# from src.utils import read_links_txt
#
# links = read_links_txt('../input/images_links.txt')
#
# start = time.perf_counter()
#
# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url,
#                                ssl=False
#                                ) as response:
#             return response.status
#
# loop = asyncio.get_event_loop()
#
# tasks = [get(link) for link in links]
# results = loop.run_until_complete(asyncio.gather(*tasks))
# print(f'Elapsed:{time.perf_counter()-start}')
# print("Results: %s" % results)

import os
import pathlib
import time
import aiohttp
import aiofiles
import asyncio

from bs4 import BeautifulSoup

from src.utils import read_links_txt, get_file_name_from_url

# links = read_links_txt('../input/images_links.txt')\

img_dir = '../img/async'

pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)


async def links_scraper(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as resp:
            soup = BeautifulSoup(await resp.text(), "html.parser")
            image = soup.findAll("img")
            d = [i['src'] for i in image]
            link = []
            for i in d:
                if (i[-4:]) == '.jpg':
                    link.append(i)
            yield link


start = time.perf_counter()


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            f = await aiofiles.open(os.path.join(img_dir, get_file_name_from_url(url)), mode='wb')
            await f.write(await response.read())
            await f.close()


async def app_main():
    async for i in  links_scraper('https://wallpaperscraft.ru/'):
        for g in i:
            await download(g)


loop = asyncio.get_event_loop()
# tasks = [download(link) async for link in links_scraper("https://www.pinterest.com")]
# loop.run_until_complete(asyncio.gather(*tasks))
loop.run_until_complete(app_main())
print(f'Elapsed:{time.perf_counter() - start}')
