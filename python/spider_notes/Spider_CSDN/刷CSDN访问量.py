from bs4 import BeautifulSoup
import requests
import time

urls = 'https://blog.csdn.net/xiligey1/article/details/112387598'

headers = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    },
    {
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
]
for i in range(10000):
    time.sleep(10)
    req = requests.get(urls, headers=headers[0])
    soup = BeautifulSoup(req.text, 'lxml')
    text = soup.select('#content_views')

    print(text)
    print(i)
