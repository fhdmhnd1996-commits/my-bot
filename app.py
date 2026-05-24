import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Sync Bot", layout="wide")
st.title("🤖 ماسح أزواج OTC مع مزامنة التوقيت")

# 1. إعدادات تصحيح التوقيت (أضف فارق الساعات بين السيرفر ومنصتك)
time_offset = st.sidebar.number_input("فارق التوقيت بالدقائق (Offset):", value=0)

otc_tickers = {
    "EURUSD OTC": "EURUSD=X", "GBPUSD OTC": "GBPUSD=X", "USDJPY OTC": "USDJPY=X", 
    "AUDUSD OTC": "AUDUSD=X", "USDCAD OTC": "USDCAD=X", "USDCHF OTC": "USDCHF=X"
}

if st.button("🚀 فحص السوق مع مزامنة التوقيت"):
    results = []
    # عرض التوقيت الحالي
    server_time = datetime.now()
    st.write(f"⏰ توقيت السيرفر الحالي: {server_time.strftime('%H:%M:%S')}")
    
    for name, symbol in otc_tickers.items():
        try:
            df = yf.download(symbol, period="1d", interval="1m", progress=False)
            if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
            
            # حساب المؤشرات
            df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
            df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
            
            # توقيت إغلاق الشمعة الحقيقي مع تصحيح المستخدم
            last_candle_time = df.index[-2] + timedelta(minutes=time_offset)
            sync_time = last_candle_time.strftime('%H:%M:%S')
            
            # منطق الدخول
            if df['EMA9'].iloc[-2] > df['EMA21'].iloc[-2]:
                results.append(f"🟢 **{name}**: شراء - إغلاق الشمعة {sync_time}")
            else:
                results.append(f"🔴 **{name}**: بيع - إغلاق الشمعة {sync_time}")
        except: continue
            
    for res in results: st.markdown(res)
