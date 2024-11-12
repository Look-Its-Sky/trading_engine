from settings import config, symbol_opts
import pandas as pd 
import numpy as np
import pandas_ta as ta
import requests, json
from datetime import datetime

class Trader:
    '''
    Handle class wide parameters here
    '''
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.long_entry = False
        self.short_entry = False
        self.use_tp_pct = False
        self.df = df

        # Params
        if symbol not in symbol_opts.keys():
            print('Symbol not found in opts file!')
            exit()

        # Config here refers to symbol_opts for respective symbol
    
    '''
    Fill in indicators here

    Returns populated df with indicators
    '''
    def populate_indicators(self) -> None: 
        df = self.df
        is_all = lambda x: x.all()
        is_any = lambda x: x.any()

        return df
    
    '''
    For conditional exits (optional)

    Returns: bool
    '''
    def should_exit(self, positions: list, df: pd.DataFrame) -> bool:
        return False
        
    '''
    Defining stoploss and take profit (optional, on a technical level)

    Returns dict of stoploss and tp
    '''
    def tp_sl(self, df: pd.DataFrame) -> dict: 
        return None 
