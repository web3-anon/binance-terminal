from binance.spot import Spot 
from chooseCoin import *
from lastWithdrawals import *
from tickers import *
import time
from binanceLiquidity import *
import requests

#put binance keys in here
client = Spot(key='<your key here>', secret='<your secret here>')

while (1):

    print("###################################################\n")

    print("\nWhat would you like to do?\n")

    print("###################################################\n")

    print("BINANCE\n")

    print("\n0. Real-time BTC/ETH/BNB value")
    print("\n1. Get current prices.")
    print("\n2. Get balances.")
    print("\n3. Get withdrawal history")
    print("\n4. Post an order")
    print("\n5. View past orders")
    print("\n7. Get past trades of a pair")
    print("\n8. Get futures' account snapshot")
    print("\n9. Get margin account snapshot")
    print("\n10. Get current bids")

    num = input('\nWhat would you like to do?\n')

    if num == '1':

        tickers()

    elif num == '2':

        print(client.account())

    elif num == '3':

        z = client.withdraw_history()

        displayWithdrawals(z)

    elif num == '4':

        symbol = input('\nWhich pair would you like to trade?\n')

        side = input("Would you like to 'SELL' or 'BUY'?")

        quantity = input("Quantity in decimal?")

        price = input("Price that you'd like to set?")

        params = {
            'symbol': symbol,
            'side': side,
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': quantity,
            'price': price
        }

        response = client.new_order(**params)
        print(response)


    elif num == '5':

        pair = input("Which pair would you like to see the history of?")
        response = client.my_trades(pair)
        print(response)

    elif num == '6':
        print("---------------\n")

    elif num == '7':        

        symbolTrades = input('\nWhich pair would you like to get history of?\n')

        if (len(client.my_trades(symbolTrades)) < 10):
            print("No trades done of this pair")
        else:
            print(client.my_trades(symbolTrades))

    elif num == '8':        

        print(client.account_snapshot("FUTURES"))

    elif num == '9':        

        print(client.account_snapshot("MARGIN"))

    elif num == '10':        

        seeBinanceLiquidity()

    else:

        starttime = time.time()
        while True:
            btc = client.ticker_price("BTCUSDT")
            eth = client.ticker_price("ETHUSDT")
            bnb = client.ticker_price("BNBUSDT")
            doge = client.ticker_price("DOGEUSDT")

            btcPrice = float(btc['price'])
            print("BTC: ", btcPrice)
            ethPrice = float(eth['price'])
            print("ETH: ", ethPrice)
            bnbPrice = float(bnb['price'])
            print("BNB: ", bnbPrice)
            dogePrice = float(doge['price'])
            print("DOGE: ", dogePrice)
            print("\n-------------------\n")
            time.sleep(5.0 - ((time.time() - starttime) % 5.0))

    print("\n###################################################")
