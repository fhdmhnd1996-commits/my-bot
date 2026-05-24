import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Session", layout="wide")
st.title("🎯 جدول الصفقات (توقيت إغلاق الشمعة)")

# عرض الوقت الحالي بدون ثواني
st.metric("⏰ الوقت الحالي", datetime.now().strftime("%H:%M"))

otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

if st.button("🚀 استخراج جدول الصفقات (بدون ثواني)"):
    # نبدأ من الوقت الحالي بالدقيقة (تجاهل الثواني)
    start_time = datetime.now().replace(second=0, microsecond=0)
    
    data = []
    for i in range(1, 11):
        # إضافة 3 دقائق لكل صفقة
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        pair = otc_list[(i-1) % len(otc_list)]
        
        # تنسيق الوقت بدون ثواني (%H:%M)
        data.append([i, pair, trade_time.strftime('%H:%M')])
    
    df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "وقت الدخول"])
    st.table(df)
    st.success("تم ضبط الجدول على توقيت إغلاق الشمعة.")

if st.button("🔄 تحديث الوقت"):
    st.rerun()
