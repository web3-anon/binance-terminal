from binance.spot import Spot 

def tickers():

    client = Spot(key='<your key here>', secret='<your secret here>')

    print("\nGENERAL:\n")
    print(client.ticker_price("BTCUSDT"))
    print(client.ticker_price("ETHUSDT"))
    print(client.ticker_price("ZECUSDT"))
    print(client.ticker_price("BNBUSDT"))
    print(client.ticker_price("ADAUSDT"))
    print(client.ticker_price("AVAXUSDT"))
    print(client.ticker_price("XMRUSDT"))
    print(client.ticker_price("ETCUSDT"))

    print("\nDEFI:\n")

    print(client.ticker_price("AAVEUSDT"))
    print(client.ticker_price("UNIUSDT"))
    print(client.ticker_price("SUSHIUSDT"))
    print(client.ticker_price("1INCHUSDT"))
    print(client.ticker_price("LINKUSDT"))
    print(client.ticker_price("YFIUSDT"))
    print(client.ticker_price("CAKEUSDT"))

    print("\nCHANGES VERSUS BITCOIN:\n")

    if (client.ticker_24hr("ETHBTC")['priceChangePercent'] > '0'):
        print("ETH/BTC =   +" + client.ticker_24hr("ETHBTC")['priceChangePercent'] + "%")
    else:
        print("ETH/BTC =   " + client.ticker_24hr("ETHBTC")['priceChangePercent'] + "%")

    if (client.ticker_24hr("ZECBTC")['priceChangePercent'] > '0'):
        print("ZEC/BTC =   +" + client.ticker_24hr("ZECBTC")['priceChangePercent'] + "%")
    else:
        print("ZEC/BTC =   " + client.ticker_24hr("ZECBTC")['priceChangePercent'] + "%")

    if (client.ticker_24hr("AAVEBTC")['priceChangePercent'] > '0'):
        print("AAVE/BTC =  +" + client.ticker_24hr("AAVEBTC")['priceChangePercent'] + "%")
    else:
        print("AAVE/BTC =  " + client.ticker_24hr("AAVEBTC")['priceChangePercent'] + "%")

    if (client.ticker_24hr("BNBBTC")['priceChangePercent'] > '0'):
        print("BNB/BTC =  +" + client.ticker_24hr("BNBBTC")['priceChangePercent'] + "%")
    else:
        print("BNB/BTC =  " + client.ticker_24hr("BNBBTC")['priceChangePercent'] + "%")
