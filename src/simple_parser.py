from datetime import time

import requests
from src.utils import read_links_txt

links = read_links_txt('../input/images_links.txt')
start = time.perf_counter()
responses = []

for link in links:
    responses = requests.get(link)
    responses.append(responses.status_code)
print(f'Elapsed:{time.perf_counter()-start}')
print("Result: %s" % results)