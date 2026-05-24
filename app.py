import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Session Bot", layout="wide")
st.title("🎯 نظام الـ 10 صفقات")

if st.button("🚀 استخراج جدول الصفقات"):
    start_time = datetime.now()
    st.write(f"### وقت بدء الجلسة: {start_time.strftime('%H:%M:%S')}")
    
    data = []
    for i in range(1, 11):
        # إضافة 3 دقائق لكل صفقة
        trade_time = start_time + timedelta(minutes=3 * (i - 1))
        data.append([i, trade_time.strftime('%H:%M:%S')])
    
    # تحويل البيانات لجدول
    df = pd.DataFrame(data, columns=["رقم الصفقة", "وقت الدخول المقترح"])
    st.table(df)
    
    st.success("تم استخراج الجدول. التزم بالوقت!")
