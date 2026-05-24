import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="Pro Bot", layout="wide")
st.title("نظام التداول الاحترافي")

ticker = st.sidebar.selectbox("اختر الزوج:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("تشغيل التحليل"):
    try:
        # تحميل البيانات
        data = yf.download(ticker, period="1d", interval="1m", progress=False)
        
        # --- خطوة الحل الجذري ---
        # إذا كانت الأعمدة متعددة المستويات، نجعلها مستوى واحد
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
            
        if not data.empty:
            # حساب المؤشرات
            data['EMA9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA21'] = data['Close'].ewm(span=21, adjust=False).mean()
            
            # حساب RSI بسيط
            delta = data['Close'].diff()
            gain = delta.clip(lower=0).rolling(window=14).mean()
            loss = (-delta.clip(upper=0)).rolling(window=14).mean()
            data['RSI'] = 100 - (100 / (1 + (gain / loss)))
            
            # الحصول على آخر قيمة
            last = data.iloc[-1]
            st.write(f"السعر الحالي: {float(last['Close']):.5f}")
            st.write(f"مؤشر RSI: {float(last['RSI']):.2f}")
            
            # منطق الإشارة
            if float(last['EMA9']) > float(last['EMA21']) and float(last['RSI']) < 30:
                st.success("إشارة شراء قوية (BUY)")
            elif float(last['EMA9']) < float(last['EMA21']) and float(last['RSI']) > 70:
                st.error("إشارة بيع قوية (SELL)")
            else:
                st.warning("لا توجد إشارة.")
        else:
            st.error("البيانات فارغة من المصدر.")
            
    except Exception as e:
        st.error(f"خطأ برمجـي: {str(e)}")
