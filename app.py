import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- المحرك البرمجي (Engine) ---
class TradingEngine:
    @staticmethod
    def get_data(ticker):
        # تحميل بيانات حقيقية
        df = yf.download(ticker, period="1d", interval="1m", progress=False)
        return df

    @staticmethod
    def apply_strategy(df):
        # حساب المؤشرات
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        # حساب RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain / loss)))
        return df

# --- الواجهة (Interface) ---
st.set_page_config(page_title="Professional Trading Bot", layout="wide")
st.title("🚀 نظام التداول الاحترافي المتكامل")

# ضبط التوقيت
offset = st.sidebar.slider("فرق التوقيت (ثانية):", -5, 5, 0)
ticker = st.sidebar.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("🚀 تشغيل المحرك والتحليل"):
    try:
        engine = TradingEngine()
        df = engine.get_data(ticker)
        df = engine.apply_strategy(df)
        
        last = df.iloc[-1]
        st.write(f"### السعر الحالي: {last['Close']:.5f}")
        st.write(f"### RSI: {last['RSI']:.2f}")
        
        # منطق الدخول
        if last['EMA9'] > last['EMA21'] and last['RSI'] < 30:
            st.success("🟢 إشارة شراء قوية (Buy)")
        elif last['EMA9'] < last['EMA21'] and last['RSI'] > 70:
            st.error("🔴 إشارة بيع قوية (Sell)")
        else:
            st.warning("⚪ لا توجد إشارة مطابقة للمعايير.")
            
    except Exception as e:
        st.error(f"خطأ في تحميل البيانات: {e}")

st.write(f"⏱️ توقيت النظام: {(datetime.now() + timedelta(seconds=offset)).strftime('%H:%M:%S')}")
