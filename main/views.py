from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
from django.template.defaulttags import register

cg = CoinGeckoAPI()

def get_prices(
    base,
    all_tickers,
    exchanges_id_array,
):
    result = {}
    vs_currencies = ['USD', 'USDT', 'EUR', 'BTC']
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


needed_coins = ['bitcoin', 'ethereum', 'ripple']


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
            "price":
            get_prices(coin_full_info["symbol"].upper(),
                       coin_full_info["tickers"],
                       ['kucoin', 'binance', 'gate', 'kraken', 'currency']),
            "image":
            coin_full_info["image"],
            "price_change_percentage_24h_usd":
            coin_full_info["market_data"]
            ["price_change_percentage_24h_in_currency"]["usd"]
        }
        result_coin_data.append(coin_dict)
    return result_coin_data


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
    }

    return render(request, 'main/index.html', context=data)


# index()
# print(index)
# Ссылки на страницы
