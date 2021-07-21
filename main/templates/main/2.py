# from pycoingecko import CoinGeckoAPI
#
# cg = CoinGeckoAPI()
#
# coin_markets = cg.get_coins_markets('USD')
# coin_list = cg.get_coins_list()
#
# top_10_coins = coin_markets[0:10]
#
#
# coin_market_cap = []
# coin_id = []
#
# for top_coin in top_10_coins:
#     coin_market_cap.append(top_coin['market_cap'])
# for top_coin in top_10_coins:
#     coin_id.append(top_coin['id'])
#
#
# result = dict(zip(coin_id, coin_market_cap))
#
# # result = top_10_coins['id']['market_cap']
# print(result)
#
#
# print(top_10_coins)


a = 96123456789




print('{:,}'.format(a).replace(',', '.'))