import yaml, average, nn_predict
from yaml.loader import SafeLoader

with open('config.yaml') as f:
    config = yaml.load(f, Loader=SafeLoader)
    # print(config)

algorithm = config['algorithm']
# options : 'average'

trade_mode = config['trade_mode']

if algorithm == 'average':
    print('running average trade algorithm')
    print('running with trade mode {}'.format(trade_mode))
    # while True:
    #     average.run(trade_mode)
    