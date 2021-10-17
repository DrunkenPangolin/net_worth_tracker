from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from personal_data import CoinMarketCap_API


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
'start': '1',
'limit': '1',
'convert': 'GBP',

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CoinMarketCap_API,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data['data'][0]['symbol'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)