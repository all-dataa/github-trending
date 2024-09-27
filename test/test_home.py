import requests

trend = 'https://github.com/trending'

res = requests.get(trend)

with open('trend.html', 'w', encoding='utf-8') as f:
    f.write(res.text)