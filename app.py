import streamlit as st
import pandas as pd
import yfinance as yf

# إعدادات الواجهة
st.set_page_config(page_title="Trading Bot", layout="centered")
st.title("بوت التداول الاحترافي")

# اختيار الزوج
ticker = st.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("تحليل السوق"):
    try:
        # جلب البيانات
        df = yf.download(ticker, period="1d", interval="1m", progress=False)
        
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        if not df.empty and len(df) > 21:
            # حساب المؤشرات
            df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
            df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
            
            # عرض النتيجة
            st.write(f"السعر الحالي: {float(df['Close'].iloc[-1]):.5f}")
            
            if df['EMA9'].iloc[-1] > df['EMA21'].iloc[-1]:
                st.success("اتجاه صاعد (BUY)")
            else:
                st.error("اتجاه هابط (SELL)")
        else:
            st.warning("جاري تحميل البيانات..")
    except Exception as e:
        st.error(f"خطأ: {e}")
