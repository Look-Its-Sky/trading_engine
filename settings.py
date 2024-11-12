import json

with open('config.json') as f:
    config = json.load(f)
    
with open('symbol_opts.json') as f:
    symbol_options = json.load(f)

symbols = symbol_options.keys()
