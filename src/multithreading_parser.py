# from concurrent import futures
import time
# import requests
# from src.utils import read_links_txt
#
# links = read_links_txt('../input/images_links.txt')
# start = time.perf_counter()
# with futures.ThreadPoolExecutor(max_workers=4) as executor:
#     futures = [
#         executor.submit(
#             lambda: requests.get(link))
#         for link in links
#     ]
# results = [
#     f.result().status_code
#     for f in futures
# ]
# print(f'Elapsed:{time.perf_counter()-start}')
# print("Results: %s" % results)

import os
import pathlib
from concurrent import futures
import requests
from src.utils import read_links_txt, get_file_name_from_url

links = read_links_txt('../input/images_links.txt')
img_dir = '../img/threads'

pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)


def download(link):
    with open(os.path.join(img_dir, get_file_name_from_url(link)), 'wb') as f:
        f.write(requests.get(link).content)

start = time.perf_counter()
with futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [
        executor.submit(download(link)) for link in links
    ]
print(f'Elapsed:{time.perf_counter()-start}')

