import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- المحرك البرمجي ---
class TradingEngine:
    @staticmethod
    def get_data(ticker):
        # تحميل بيانات اليوم بفاصل زمني دقيقة
        df = yf.download(ticker, period="1d", interval="1m", progress=False)
        return df

    @staticmethod
    def apply_strategy(df):
        # حساب المؤشرات
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        
        delta = df['Close'].diff()
        gain = delta.clip(lower=0).rolling(window=14).mean()
        loss = (-delta.clip(upper=0)).rolling(window=14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain / loss)))
        return df

# --- الواجهة ---
st.set_page_config(page_title="Pro Trading Bot", layout="wide")
st.title("نظام التداول الاحترافي")

offset = st.sidebar.slider("ضبط فرق التوقيت (ثانية):", -10, 10, 0)
ticker = st.sidebar.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("تشغيل التحليل"):
    try:
        engine = TradingEngine()
        df = engine.get_data(ticker)
        
        if df is not None and not df.empty and len(df) > 21:
            df = engine.apply_strategy(df)
            # أخذ آخر صف فقط كقيمة مفردة (سلسلة)
            last = df.iloc[-1]
            
            # تحويل القيم إلى أرقام عادية لتجنب أخطاء التنسيق
            price = float(last['Close'])
            rsi = float(last['RSI'])
            
            st.write(f"السعر الحالي: {price:.5f}")
            st.write(f"مؤشر RSI: {rsi:.2f}")
            
            if last['EMA9'] > last['EMA21'] and rsi < 30:
                st.success("إشارة شراء قوية (BUY)")
            elif last['EMA9'] < last['EMA21'] and rsi > 70:
                st.error("إشارة بيع قوية (SELL)")
            else:
                st.warning("لا توجد إشارة مطابقة للمعايير حالياً.")
        else:
            st.error("بيانات السوق غير متوفرة حالياً.")
    except Exception as e:
        st.error(f"خطأ تقني: {e}")

st.write(f"توقيت النظام: {(datetime.now() + timedelta(seconds=offset)).strftime('%H:%M:%S')}")
