from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
from django.template.defaulttags import register

cg = CoinGeckoAPI()


def get_background_image(link):
    return f'background-image: url({link})'


def modify_percentage_change(digit):
    arr = list(str(round(digit, 2)))
    if arr[0] == "-":
        arr[0] = "▼"
    else:
        arr.insert(0, "▲")
    return {
        "digit": digit,
        "string": "".join(arr),
    }


def get_market_prices(
    base,
    all_tickers,
    exchanges_id_array,
):
    result = {}
    # vs_currencies = ['USD', 'USDT', 'EUR', 'BTC']
    vs_currencies = ['USDT']
    for exchange in exchanges_id_array:
        for ticker in all_tickers:
            for currency in vs_currencies:
                if ticker["target"] == currency and ticker["target"] != base:
                    if exchange == ticker["market"]["identifier"]:
                        if exchange in result:
                            result[exchange][ticker["target"]] = ticker["last"]
                        else:
                            result[exchange] = {}
                            result[exchange][ticker["target"]] = ticker["last"]
    return result


def get_all_coins():
    result = []
    for coin in cg.get_coins_list():
        result.append(coin["id"])
    print(result)
    return result


needed_coins = ['bitcoin', 'ethereum', 'ripple', 'cardano',
                'polkadot']


def get_coin_info(coin_list):
    result_coin_data = []
    for coin in coin_list:
        coin_full_info = cg.get_coin_by_id(coin)
        coin_dict = {
            "id":
            coin_full_info["id"],
            "symbol":
            coin_full_info["symbol"],
            "name": {
                "en": coin_full_info["localization"]["en"],
                "ru": coin_full_info["localization"]["ru"],
            },
            "current_usd_price":
            round(coin_full_info["market_data"]["current_price"]["usd"], 4),
            "markets":
            get_market_prices(coin_full_info["symbol"].upper(), coin_full_info["tickers"], ['binance']),
             "image":
            coin_full_info["image"],
            "price_change_percentage_1h":
            modify_percentage_change(
                coin_full_info["market_data"]["price_change_percentage_1h_in_currency"]["usd"]),
            "market_cap":
            '{:,}'.format(coin_full_info['market_data']['market_cap']['usd']).replace(',','.')
        }
        result_coin_data.append(coin_dict)
    return result_coin_data

# get_coin_market_cap
# def get_coin_market_cap(quant):
#     coin_markets = cg.get_coins_markets('USD')
#     # coin_list = cg.get_coins_list()
#
#     top_10_coins = coin_markets[0:quant]
#
#     coin_market_cap = []
#     coin_id = []
#
#     for top_coin in top_10_coins:
#         coin_market_cap.append(top_coin['market_cap'])
#     for top_coin in top_10_coins:
#         coin_id.append(top_coin['id'])
#
#     return dict(zip(coin_id, coin_market_cap))




coin_info = get_coin_info(needed_coins)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_keys(dictionary):
    return list(dictionary.keys())


def index(request):
    data = {
        "coins": coin_info,
        "get_item": get_item,
        "get_keys": get_keys,
        "background_image": get_background_image,

    }

    return render(request, 'main/index.html', context=data)


# index()
# print(index)
# Ссылки на страницы
