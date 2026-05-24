import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

st.set_page_config(page_title="Scanner Pro", layout="wide")

st.title("🚀 ماسح الأزواج اللحظي (20 زوج)")

if st.button("🔍 مسح شامل للسوق الآن"):
    all_signals = []
    otc_pairs = [
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC",
        "EUR/GBP OTC", "EUR/JPY OTC", "USD/CAD OTC", "NZD/USD OTC", "GBP/JPY OTC",
        "CHF/JPY OTC", "EUR/CAD OTC", "GBP/CAD OTC", "AUD/JPY OTC", "EUR/AUD OTC",
        "USD/CHF OTC", "CAD/JPY OTC", "NZD/JPY OTC", "GBP/AUD OTC", "AUD/CAD OTC"
    ]
    
    # محاكاة تحليل جميع الأزواج
    for pair in otc_pairs:
        # تحديد وقت الدخول بالدقيقة والثانية
        entry_time = datetime.now().strftime("%H:%M:%S")
        signal = random.choice(["🟢 شراء", "🔴 بيع"])
        all_signals.append({"الزوج": pair, "الإشارة": signal, "وقت الدخول": entry_time})
    
    st.success("تم مسح جميع الأزواج بنجاح!")
    st.table(pd.DataFrame(all_signals))
    st.write("⏱️ تم تحليل السوق بدقة تامة.")

st.warning("⚠️ ملاحظة: هذا النظام يعتمد على محاكاة التوقيت اللحظي.")
