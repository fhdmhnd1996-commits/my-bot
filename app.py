import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- المحرك البرمجي ---
class TradingEngine:
    @staticmethod
    def get_data(ticker):
        df = yf.download(ticker, period="1d", interval="1m", progress=False)
        return df

    @staticmethod
    def apply_strategy(df):
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain / loss)))
        return df

# --- الواجهة ---
st.set_page_config(page_title="Pro Bot", layout="wide")
st.title("نظام التداول الاحترافي")

offset = st.sidebar.slider("ضبط فرق التوقيت:", -5, 5, 0)
ticker = st.sidebar.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("تشغيل التحليل"):
    try:
        engine = TradingEngine()
        df = engine.get_data(ticker)
        if df is not None and not df.empty and len(df) > 21:
            df = engine.apply_strategy(df)
            last = df.iloc[-1]
            st.write(f"السعر الحالي: {last['Close']:.5f}")
            st.write(f"RSI: {last['RSI']:.2f}")
            
            if last['EMA9'] > last['EMA21'] and last['RSI'] < 30:
                st.success("إشارة شراء قوية (BUY)")
            elif last['EMA9'] < last['EMA21'] and last['RSI'] > 70:
                st.error("إشارة بيع قوية (SELL)")
            else:
                st.warning("لا توجد إشارة مطابقة.")
        else:
            st.error("بيانات السوق غير كافية حالياً.")
    except Exception as e:
        st.error(f"خطأ: {e}")

st.write(f"توقيت النظام: {(datetime.now() + timedelta(seconds=offset)).strftime('%H:%M:%S')}")
