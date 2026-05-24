import streamlit as st
import pandas as pd
import random
from datetime import datetime
import time

st.set_page_config(page_title="Pro Entry Scanner", layout="wide")
st.title("⏱️ ماسح الصفقات (دخول عند الثانية 59)")

if st.button("🚀 بدء المسح اللحظي"):
    otc_pairs = ["EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC"]
    data = []
    
    # محاكاة الانتظار للثانية 59
    current_sec = datetime.now().second
    st.write(f"الثانية الحالية: {current_sec} - جاري الانتظار للثانية 59...")
    
    # محاكاة منطق التحليل
    for pair in otc_pairs:
        # إشارة عشوائية للتوضيح
        signal = random.choice(["🟢 شراء", "🔴 بيع"])
        
        # وقت الدخول المخطط له (في الثانية 59)
        entry_time = datetime.now().replace(second=59).strftime("%H:%M:%S")
        
        data.append({
            "الزوج": pair, 
            "الإشارة": signal, 
            "موعد الدخول": f"{entry_time} (ثانية 59)"
        })
    
    st.table(pd.DataFrame(data))
    st.success("✅ جاهز! انتظر وصول التوقيت للثانية 59 واضغط في المنصة.")
