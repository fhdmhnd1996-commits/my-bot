import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Pro Scanner", layout="wide")
st.title("🤖 ماسح OTC مع نظام التهدئة (3 دقائق)")

# تهيئة الذاكرة المؤقتة للوقت
if 'last_signal_time' not in st.session_state:
    st.session_state.last_signal_time = datetime.min

otc_tickers = {"EURUSD OTC": "EURUSD=X", "GBPUSD OTC": "GBPUSD=X", "USDJPY OTC": "USDJPY=X"}

if st.button("🚀 فحص السوق"):
    current_time = datetime.now()
    time_since_last = current_time - st.session_state.last_signal_time
    
    # التحقق من فارق الـ 3 دقائق
    if time_since_last < timedelta(minutes=3):
        wait_time = 3 - int(time_since_last.total_seconds() / 60)
        st.warning(f"⚠️ يرجى الانتظار! آخر صفقة كانت قبل قليل. يرجى الانتظار {wait_time} دقائق.")
    else:
        # هنا يتم تنفيذ الفحص
        st.write("✅ جاري تحليل الفرص..")
        
        # ... (نفس منطق التحليل السابق) ...
        
        # عند إعطاء الإشارة، قم بتحديث وقت آخر إشارة
        st.session_state.last_signal_time = datetime.now()
        st.success("إشارة جديدة تم رصدها!")
