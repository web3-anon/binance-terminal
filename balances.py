from binance.spot import Spot 

def balances(x):

    if x == '':

        print("")

    else:

        client = Spot(key='<your key>', secret='<your secret>')

        print()
