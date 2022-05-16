import bs4
import requests

URL = 'https://coinmarketcap.com/currencies/c20/'

def scrape(site_url):
    res = requests.get(site_url)
    res.raise_for_status
    return res

def scrape_crypto():
        
    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    session = Session()
    session.headers.update(headers)

    try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

def scrape_fund(site_url):
    scrape(site_url)

def scrape_stocks(site_url):
    scrape(site_url)

def scrape_currencies(site_url):


if __name__ == "__main__":
    scrape_crypto(URL)