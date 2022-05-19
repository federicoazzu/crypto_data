import api
from collections import namedtuple


def main():
    coins = api.get_crypto_data()

    for coin in coins:
        #if coin.symbol in['btc', 'eth', 'xrp', 'doge']:
            print(f"{coin.name} ({coin.symbol}): {coin.current_price}€ (24h: {coin.price_change_24h}%, 7d: {coin.price_change_7d}%)")


if __name__ == '__main__':
    main()
