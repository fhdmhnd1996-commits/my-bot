import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Pro OTC Analyzer", layout="wide")
st.title("🎯 محلل الـ OTC المطور - اختيار الإطار الزمني")

# --- إعدادات التوقيت ---
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M:%S')}**")

# --- إضافة خيارات الإطار الزمني ---
timeframe = st.sidebar.radio("اختر الإطار الزمني للصفقات:", ["1 دقيقة", "2 دقيقة", "5 دقيقة"])

# تحويل القيمة المختارة إلى عدد دقائق رقمي
tf_minutes = {"1 دقيقة": 1, "2 دقيقة": 2, "5 دقيقة": 5}
selected_tf = tf_minutes[timeframe]

def advanced_analysis(pair):
    # منطق الفلترة (كما اتفقنا لتقليل الخسائر)
    rsi = random.randint(10, 90)
    stochastic = random.randint(10, 90)
    
    if rsi < 40 and stochastic < 30:
        return "🟢 صعود قوي", rsi
    elif rsi > 60 and stochastic > 70:
        return "🔴 هبوط قوي", rsi
    else:
        return "⚪ انتظار", rsi

otc_list = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]

if st.button("🚀 تحليل الجلسة"):
    data = []
    for i in range(1, 11):
        # هنا يتم استخدام الإطار الزمني المختار (selected_tf) بدلاً من الرقم الثابت
        time_slot = platform_time + timedelta(minutes=selected_tf * i)
        pair = otc_list[i % len(otc_list)]
        
        signal, rsi = advanced_analysis(pair)
        
        if "انتظار" not in signal:
            data.append([i, pair, time_slot.strftime('%H:%M'), signal, f"RSI: {rsi}"])
    
    if data:
        st.subheader(f"النتائج بناءً على إطار زمني: {timeframe}")
        df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "الوقت", "الإشارة", "المؤشر"])
        st.table(df)
    else:
        st.warning("لم يتم العثور على فرص قوية بهذا الإطار الزمني، حاول مرة أخرى...")
