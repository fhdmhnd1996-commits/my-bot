import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="OTC Scanner", layout="wide")
st.title("🤖 ماسح أزواج السوق الموازي (OTC Mode)")

# هذه الرموز هي المقابل العالمي لأزواج OTC الأكثر تداولاً
otc_tickers = {
    "EURUSD OTC": "EURUSD=X", "GBPUSD OTC": "GBPUSD=X", 
    "USDJPY OTC": "USDJPY=X", "AUDUSD OTC": "AUDUSD=X", 
    "USDCAD OTC": "USDCAD=X", "USDCHF OTC": "USDCHF=X",
    "EURGBP OTC": "EURGBP=X", "EURJPY OTC": "EURJPY=X", 
    "GBPJPY OTC": "GBPJPY=X", "AUDJPY OTC": "AUDJPY=X",
    "NZDUSD OTC": "NZDUSD=X", "EURCAD OTC": "EURCAD=X", 
    "EURCHF OTC": "EURCHF=X", "CADJPY OTC": "CADJPY=X", 
    "CHFJPY OTC": "CHFJPY=X", "GBPCAD OTC": "GBPCAD=X", 
    "EURAUD OTC": "EURAUD=X", "GBPAUD OTC": "GBPAUD=X", 
    "NZDJPY OTC": "NZDJPY=X", "AUDCAD OTC": "AUDCAD=X"
}

if st.button("🚀 فحص أزواج OTC الآن"):
    results = []
    progress_bar = st.progress(0)
    
    for i, (name, symbol) in enumerate(otc_tickers.items()):
        try:
            df = yf.download(symbol, period="1d", interval="1m", progress=False)
            if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
            
            if not df.empty and len(df) > 21:
                df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
                df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
                
                # إشارة التداول
                if df['EMA9'].iloc[-1] > df['EMA21'].iloc[-1]:
                    results.append(f"🟢 {name}: إشارة شراء (Buy Trend)")
                else:
                    results.append(f"🔴 {name}: إشارة بيع (Sell Trend)")
        except: continue
        progress_bar.progress((i + 1) / len(otc_tickers))
            
    for res in results: st.write(res)
