from alpaca.data.historical import  CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime
from settings import symbols
from traders.trader import Trader
import multiprocessing
import handler
import sys

while True:
    data = handler.get_data(symbols)

    processes = []
    for s in symbols:
        process = multiprocessing.Process(target=worker.run) # START HERE --- fix multithreaded trade stuff 
