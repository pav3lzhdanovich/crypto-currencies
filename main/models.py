from django.db import models
from pycoingecko import CoinGeckoAPI
import time

cg = CoinGeckoAPI()

def check_currency_btc(coin):
    return cg.get_price(ids=coin, vs_currencies='usd')

check_currency_btc('bitcoin')

btc_price = check_currency_btc('bitcoin')

print(btc_price['bitcoin']['usd'])