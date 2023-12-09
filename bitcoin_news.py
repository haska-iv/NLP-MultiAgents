# filename: bitcoin_news.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Получаем новости о Bitcoin за последние 7 дней
url = "https://news.google.com/rss/search?q=Bitcoin&hl=en-US&sort=date&gl=US&num=100&output=rss"
response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml")
items = soup.findAll('item')

# Сохраняем новости в файл
with open('bitcoin_news.txt', 'w') as f:
    for item in items:
        pubDate = datetime.strptime(item.pubDate.text, '%a, %d %b %Y %H:%M:%S %Z')
        if pubDate > datetime.now() - timedelta(days=7):
            f.write(item.title.text + '\n')
            f.write(item.link.text + '\n')
            f.write(item.pubDate.text + '\n\n')