import get, datetime, time, yaml, trade
from yaml.loader import SafeLoader

with open('config.yaml') as f:
    config = yaml.load(f, Loader=SafeLoader)
    # print(config)

base_currency = config['base_currency']
buy_currency = config['buy_currency']
buy_precentage = 0.01*config['buy_percentage']
time_after_check = 60*config('time_after_check')

def run ():
    while True:
        past_average = get.average()
        current_price = get.current_price()
        if current_price < (1-buy_precentage)*past_average:
            trade.buy()
        elif current_price > (1+buy_precentage)*past_average:
            trade.sell()
        else:
            time.sleep(time_after_check)