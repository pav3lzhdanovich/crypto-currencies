from django.shortcuts import render
from django.http import HttpResponse
from pycoingecko import CoinGeckoAPI
from django.template.defaulttags import register

cg = CoinGeckoAPI()

# needed_coins = 'ripple,ethereum,bitcoin'
coin_list = ['bitcoin', 'ethereum', 'ripple']
coin_list.sort()
api_list = ','.join(coin_list)


def get_coin_data(coins):
    return cg.get_price(ids=coins, vs_currencies='usd', include_market_cap='true')

coin_data = get_coin_data(api_list)
coin_data_keys = list(coin_data.keys())
coin_data_keys.sort()
print(coin_data)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    data = {
        'coin_data_keys': coin_data_keys,
        'response': coin_data,
        'get_item': get_item
    }

    return render(request, 'main/index.html', context=data)

# index()
# print(index)
# Ссылки на страницы
