import yaml, requests
from yaml.loader import SafeLoader

with open('config.yaml') as f:
    config = yaml.load(f, Loader=SafeLoader)
    # print(config)

trade_mode = config['trade_mode']
base_currency = config['base_currency']
buy_currency = config['buy_currency']

if trade_mode == 'test':

    fixer_api_key = config['fixer_api_key']

    payload = {}
    headers= {
    "apikey": fixer_api_key
    }
    
    def current_price():
        url = "https://api.apilayer.com/fixer/latest?symbols={}&base={}".format(buy_currency, base_currency)

        # response = requests.request("GET", url, headers=headers, data = payload)

        # status_code = response.status_code
        # result = response.text

        result = {
            "success": 'true',
            "timestamp": 1659871804,
            "base": "GBP",
            "date": "2022-08-07",
            "rates": {
                "USD": 1.20725
            }
        }

        print(result['rates'][buy_currency])
        return result['rates'][buy_currency]

    def 

# current_price()
