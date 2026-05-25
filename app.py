import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- المحرك البرمجي المحسن ---
class TradingEngine:
    @staticmethod
    def get_data(ticker):
        df = yf.download(ticker, period="1d", interval="1m", progress=False)
        # معالجة MultiIndex إذا وجد في البيانات
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df.dropna()

    @staticmethod
    def apply_strategy(df):
        # حساب المؤشرات بدقة
        df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
        df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
        
        delta = df['Close'].diff()
        gain = (delta.clip(lower=0)).rolling(window=14).mean()
        loss = (-delta.clip(upper=0)).rolling(window=14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain / loss)))
        return df

# --- الواجهة (Interface) ---
st.set_page_config(page_title="Pro Trading Bot", layout="wide")
st.title("🛡️ نظام التداول الاحترافي (توقيت الدقيقة)")

ticker = st.sidebar.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("🚀 تشغيل المحرك والتحليل"):
    try:
        engine = TradingEngine()
        df = engine.get_data(ticker)
        
        if df is not None and not df.empty and len(df) > 21:
            df = engine.apply_strategy(df)
            last = df.iloc[-1]
            
            # العرض بالدقيقة فقط
            st.subheader(f"تحليل زوج: {ticker}")
            st.metric("السعر الحالي", f"{float(last['Close']):.5f}")
            st.metric("مؤشر RSI", f"{float(last['RSI']):.2f}")
            
            # تحديد دقيقة الدخول التالية
            next_minute = (datetime.now() + timedelta(minutes=1)).strftime("%H:%M")
            
            # منطق الدخول الصارم
            if last['EMA9'] > last['EMA21'] and last['RSI'] < 30:
                st.success(f"🟢 إشارة شراء قوية (BUY) - تنفيذ في دقيقة: {next_minute}")
            elif last['EMA9'] < last['EMA21'] and last['RSI'] > 70:
                st.error(f"🔴 إشارة بيع قوية (SELL) - تنفيذ في دقيقة: {next_minute}")
            else:
                st.warning("⚪ لا توجد إشارة مطابقة للمعايير حالياً.")
        else:
            st.error("⚠️ بيانات السوق غير كافية أو غير متاحة حالياً.")
    except Exception as e:
        st.error(f"خطأ تقني: {e}")

# عرض الوقت بالدقيقة
st.sidebar.markdown("---")
st.sidebar.write(f"🕒 توقيت النظام: **{datetime.now().strftime('%H:%M')}**")
