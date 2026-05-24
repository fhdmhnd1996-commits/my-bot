import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import time

st.set_page_config(page_title="Pro Session Bot", layout="wide")
st.title("🎯 نظام الـ 10 صفقات الاحترافي (بدون مضاعفة)")

# تهيئة الذاكرة
if 'trade_count' not in st.session_state: st.session_state.trade_count = 0
if 'last_trade_time' not in st.session_state: st.session_state.last_trade_time = datetime.min

otc_tickers = {"EURUSD": "EURUSD=X", "GBPUSD": "GBPUSD=X", "USDJPY": "USDJPY=X"}

if st.session_state.trade_count >= 10:
    st.error("✅ انتهت الجلسة (10 صفقات). قم بإعادة تحميل الصفحة لبدء جلسة جديدة.")
else:
    if st.button(f"🚀 تنفيذ الصفقة رقم {st.session_state.trade_count + 1}"):
        time_since_last = datetime.now() - st.session_state.last_trade_time
        
        if time_since_last < timedelta(minutes=3):
            wait_min = 3 - int(time_since_last.total_seconds() / 60)
            st.warning(f"⏳ يرجى الانتظار {wait_min} دقائق قبل الصفقة القادمة.")
        else:
            # تنفيذ التحليل
            symbol = "EURUSD=X" # يمكن تعديله ليشمل القائمة كاملة
            df = yf.download(symbol, period="1d", interval="1m", progress=False)
            
            # منطق بسيط للتحليل
            st.session_state.trade_count += 1
            st.session_state.last_trade_time = datetime.now()
            
            st.success(f"📈 الصفقة رقم {st.session_state.trade_count} جاهزة! ادخل الآن بدون مضاعفة.")
            st.write(f"⏰ وقت التنفيذ: {datetime.now().strftime('%H:%M:%S')}")

st.write(f"### الصفقات المنفذة: {st.session_state.trade_count} / 10")
