# filename: bitcoin_price.py

import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Получаем данные о цене Bitcoin за последние 7 дней
url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=7"
response = requests.get(url)
data = response.json()

# Проверяем, есть ли ключ 'Data' в данных
if 'Data' in data and 'Data' in data['Data']:
    # Создаем график
    dates = [datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d') for item in data['Data']['Data']]
    prices = [item['close'] for item in data['Data']['Data']]
    plt.plot(dates, prices)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bitcoin price in the last 7 days')
    plt.savefig('bitcoin_graph.png')
else:
    print("No 'Data' key in data. Please check the API.")