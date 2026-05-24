import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="OTC Pro Scanner", layout="wide")
st.title("🤖 ماسح أزواج السوق الموازي (OTC Pro)")

# قائمة الأزواج (تم ربطها بالرموز العالمية المقابلة)
otc_tickers = {
    "EURUSD OTC": "EURUSD=X", "GBPUSD OTC": "GBPUSD=X", "USDJPY OTC": "USDJPY=X", 
    "AUDUSD OTC": "AUDUSD=X", "USDCAD OTC": "USDCAD=X", "USDCHF OTC": "USDCHF=X",
    "EURGBP OTC": "EURGBP=X", "EURJPY OTC": "EURJPY=X", "GBPJPY OTC": "GBPJPY=X", 
    "AUDJPY OTC": "AUDJPY=X", "NZDUSD OTC": "NZDUSD=X", "EURCAD OTC": "EURCAD=X", 
    "EURCHF OTC": "EURCHF=X", "CADJPY OTC": "CADJPY=X", "CHFJPY OTC": "CHFJPY=X", 
    "GBPCAD OTC": "GBPCAD=X", "EURAUD OTC": "EURAUD=X", "GBPAUD OTC": "GBPAUD=X", 
    "NZDJPY OTC": "NZDJPY=X", "AUDCAD OTC": "AUDCAD=X"
}

if st.button("🚀 فحص السوق (إغلاق الشمعة)"):
    results = []
    for name, symbol in otc_tickers.items():
        try:
            df = yf.download(symbol, period="1d", interval="1m", progress=False)
            if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
            
            if len(df) > 21:
                # حساب المؤشرات
                df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
                df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
                
                delta = df['Close'].diff()
                gain = delta.clip(lower=0).rolling(window=14).mean()
                loss = (-delta.clip(upper=0)).rolling(window=14).mean()
                rsi = 100 - (100 / (1 + (gain / loss)))
                
                # الاعتماد على الشمعة التي أغلقت (iloc[-2])
                last_closed = df.iloc[-2]
                last_rsi = rsi.iloc[-2]
                close_time = df.index[-2].strftime('%H:%M:%S')
                
                if last_closed['EMA9'] > last_closed['EMA21'] and last_rsi < 35:
                    results.append(f"🟢 **{name}**: دخول شراء عند {close_time}")
                elif last_closed['EMA9'] < last_closed['EMA21'] and last_rsi > 65:
                    results.append(f"🔴 **{name}**: دخول بيع عند {close_time}")
        except: continue
            
    if results:
        for res in results: st.markdown(res)
    else:
        st.warning("لا توجد إشارات عند إغلاق الشمعة الحالية. انتظر دقيقة.")
