from binance.spot import Spot 
from chooseCoin import *
from lastWithdrawals import *
from tickers import *
from uniswap import Uniswap



def seeBinanceLiquidity():

    client = Spot(key='zk9qCvCQAEmRYaUVKrAFebIQVYCPZ2rPYXTPHdjV1OJu1Jkdv4WXgIwF31oEC7zW', secret='v6YbRdTt0UM5JDxHzgmOysGQQnxSNoXEEMDdeUpghTEsDlNYcYRMXB6OsEN6fgNO')

    bids = (client.depth("BTCUSDT")['bids'])

    minimumBid = float(bids[99][0])

    maximumBid = float(bids[0][0])

    difference = float(maximumBid - minimumBid)

    print("\nTotal difference = ", minimumBid - maximumBid)

    totalBids = float(0)

    count = 0

    while (count < 100):   
        totalBids = float(totalBids) + float(bids[count][1])
        count = count + 1

    print("\nTotal BTC =", totalBids)

    print("\n")

    print("Dumping", int(totalBids), "BTC would lead to the price decline of", int(difference), "USD")
    #z = Uniswap.estimate_price_impact("Uniswap", "0x0000000000000000000000000000000000000000", "0x6B175474E89094C44Da98b954EedeAC495271d0F", "200")

    #print("\n", z)
