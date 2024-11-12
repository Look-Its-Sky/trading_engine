from alpaca.data.historical import  CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime
from trader import Trader
import multiprocessing
import sys

while True:
    data = handler.get_data(symbols)

    processes = []
    for s in symbols:
        process = multiprocessing.Process(target=worker.run)
