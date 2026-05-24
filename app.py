import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="OTC Session", layout="wide")
st.title("🎯 جدول صفقات الـ OTC (جلسة 04:52)")

# قائمة الـ 20 زوجاً كاملة
otc_list = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC", 
    "USDCHF OTC", "EURGBP OTC", "EURJPY OTC", "GBPJPY OTC", "AUDJPY OTC",
    "NZDUSD OTC", "EURCAD OTC", "EURCHF OTC", "CADJPY OTC", "CHFJPY OTC", 
    "GBPCAD OTC", "EURAUD OTC", "GBPAUD OTC", "NZDJPY OTC", "AUDCAD OTC"
]

if st.button("🚀 عرض جدول الـ 10 صفقات"):
    # تحديد الوقت ليبدأ من 16:52 (04:52 مساءً)
    start_time = datetime.now().replace(hour=16, minute=52, second=0, microsecond=0)
    
    st.write(f"### وقت بدء الجلسة المجدول: {start_time.strftime('%H:%M:%S')}")
    
    data = []
    for i in range(1, 11):
        # إضافة 3 دقائق لكل صفقة
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        # اختيار الزوج بالترتيب
        pair = otc_list[(i-1) % len(otc_list)]
        data.append([i, pair, trade_time.strftime('%H:%M:%S')])
    
    # عرض الجدول
    df = pd.DataFrame(data, columns=["رقم الصفقة", "الزوج", "وقت الدخول"])
    st.table(df)
    
    st.success("الجدول جاهز! التزم بالدخول في الوقت المحدد.")
