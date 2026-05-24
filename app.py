import pandas as pd
import numpy as np

class StrategyEngine:
    @staticmethod
    def calculate_indicators(df):
        # EMA 9 و 21 للاتجاه
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        
        # RSI للتأكيد
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        return df

    @staticmethod
    def generate_signal(df):
        last = df.iloc[-1]
        if last['EMA9'] > last['EMA21'] and last['RSI'] < 30:
            return "🟢 BUY"
        elif last['EMA9'] < last['EMA21'] and last['RSI'] > 70:
            return "🔴 SELL"
        return None
