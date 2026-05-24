import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="Live OTC Session", layout="wide")
st.title("🎯 نظام الجلسة المباشر (OTC Pro)")

# 1. عرض الوقت المباشر (متحرك)
placeholder = st.empty()

# قائمة الـ 20 زوجاً
otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

# تحديث الساعة بشكل مستمر
while True:
    now = datetime.now()
    placeholder.metric("⏰ التوقيت الحالي للسيرفر", now.strftime("%H:%M:%S"))
    
    # منطق جدول الـ 10 صفقات
    if st.button("🚀 عرض جدول الصفقات بناءً على الوقت الحالي"):
        start_time = now.replace(second=0, microsecond=0)
        data = []
        for i in range(1, 11):
            trade_time = start_time + pd.Timedelta(minutes=3 * (i - 1))
            pair = otc_list[(i-1) % len(otc_list)]
            data.append([i, pair, trade_time.strftime('%H:%M:%S')])
        
        df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "وقت الدخول"])
        st.table(df)
        break # الخروج من اللوب بعد عرض الجدول
    
    time.sleep(1) # تحديث كل ثانية
