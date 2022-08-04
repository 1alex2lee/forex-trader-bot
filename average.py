import datetime, time
import get_historic as get
import test as trade

trade_mode = 'average'
# options : 'average'

average_period = 5
# in days

currency = 'USD'
# using GBP, options : 'USD','EUR'

if trade_mode = 'average':
    while True:

        avg = get.average(average_period)
        now = get.now(currency)

        if now > avg*1.05:
            trade.sell(currency)
        elif now < avg*1.05:
            trade.buy(currency)
        
    