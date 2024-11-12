from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime, timedelta
from trader import Trader
from settings import symbols
import pandas as pd
import numpy as np
import sys

client = CryptoHistoricalDataClient()

# Get and split data with one api call
def get_data(days_needed: int = 1, tf=TimeFrame.Minute) -> dict:
    request_params = CryptoBarsRequest(
        symbol_or_symbols=symbols,
        timeframe=TimeFrame.Minute,
        start=datetime.now() - timedelta(days=days_needed),
        end=datetime.now()
    )
    bars = client.get_crypto_bars(request_params)
    df = bars.df

    df.reset_index(inplace=True)
    df.set_index('timestamp', inplace=True)

    groups = df.groupby('symbol')
    dfs = {symbol: group for symbol, group in groups}

    for symbol in dfs.keys():
        dfs[symbol].drop(columns=['symbol'], inplace=True)

    return dfs

# NOTE: this is pretty shit fix later
def handle(s: str, df: pd.DataFrame) -> None:
    trader = Trader(s)
