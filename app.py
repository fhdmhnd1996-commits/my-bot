import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Session", layout="wide")
st.title("🎯 نظام الصفقات المجدولة (OTC Pro)")

# عرض الوقت الحالي
st.metric("⏰ وقت السيرفر الحالي", datetime.now().strftime("%H:%M:%S"))

# قائمة الـ 20 زوجاً
otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

if st.button("🚀 استخراج جدول الـ 10 صفقات القادمة"):
    # يبدأ من الوقت الحالي بالضبط
    start_time = datetime.now()
    
    data = []
    for i in range(1, 11):
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[(i-1) % len(otc_list)]
        data.append([i, pair, trade_time.strftime('%H:%M:%S')])
    
    df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "وقت الدخول"])
    st.table(df)
    st.success("تم تحديد المواعيد بدقة. ابدأ الجلسة الآن!")

# زر تحديث يدوي لتحديث الساعة
if st.button("🔄 تحديث الوقت"):
    st.rerun()
