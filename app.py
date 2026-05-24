import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Pro Session Table", layout="wide")
st.title("🎯 جدول صفقات الـ OTC (جلسة 4:52)")

# قائمة الـ 20 زوجاً
otc_list = [
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", 
    "USDCHF", "EURGBP", "EURJPY", "GBPJPY", "AUDJPY",
    "NZDUSD", "EURCAD", "EURCHF", "CADJPY", "CHFJPY", 
    "GBPCAD", "EURAUD", "GBPAUD", "NZDJPY", "AUDCAD"
]

if st.button("🚀 عرض جدول الجلسة"):
    # ضبط الوقت ليبدأ من 4:52 اليوم
    today = datetime.now().date()
    start_time = datetime.combine(today, datetime.strptime("16:52", "%H:%M").time())
    
    st.write(f"### وقت بدء الجلسة المجدول: {start_time.strftime('%H:%M:%S')}")
    
    data = []
    for i in range(1, 11):
        # إضافة 3 دقائق لكل صفقة
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        # اختيار زوج من القائمة (دائري)
        pair = otc_list[(i-1) % len(otc_list)]
        data.append([i, pair, trade_time.strftime('%H:%M:%S')])
    
    # عرض الجدول
    df = pd.DataFrame(data, columns=["رقم الصفقة", "الزوج", "وقت الدخول"])
    st.table(df)
    
    st.success("الجدول جاهز! التزم بالدخول في الوقت المحدد.")
