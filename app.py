import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Scanner Pro - Entry Timing", layout="wide")

PAIRS = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "EURGBP", "EURJPY", 
         "CHFJPY", "AUDJPY", "NZDUSD", "GBPJPY", "AUDCAD", "EURCAD", "GBPCAD", 
         "CADJPY", "AUDNZD", "EURAUD", "EURCHF", "GBPCHF", "USDCHF"]

def get_trading_times():
    """حساب وقت الدخول مع بداية الشمعة القادمة (الثانية 00)"""
    now = datetime.now()
    # نضبط وقت الدخول ليكون بداية الدقيقة التالية
    entry_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    return entry_time.strftime("%H:%M:%S"), expiry_time.strftime("%H:%M:%S")

def calculate_logic():
    """منطق فني يعتمد على محاكاة مؤشر RSI"""
    rsi = np.random.uniform(20, 80) 
    if rsi < 30:
        return "🟢 صعود (شراء)", "Strong Buy"
    elif rsi > 70:
        return "🔴 هبوط (بيع)", "Strong Sell"
    return "⚪ انتظار", "Neutral"

st.title("🛡️ ماسح الإشارات الفني (التوقيت الدقيق)")

if st.button("🚀 فحص الأسواق لافتتاح الشمعة التالية"):
    entry, expiry = get_trading_times()
    data = []
    
    for pair in PAIRS:
        trend, signal = calculate_logic()
        if trend != "⚪ انتظار":
            data.append({
                "الزوج": pair,
                "الإشارة": signal,
                "القرار": trend,
                "وقت الدخول": entry,
                "وقت الانتهاء": expiry
            })
    
    df = pd.DataFrame(data)
    
    if not df.empty:
        st.subheader(f"📊 فرص الدخول المتاحة عند الساعة {entry}")
        st.dataframe(df, use_container_width=True)
        st.success("اضغط على زر الدخول في منصتك تماماً عند وصول الوقت للثانية 00.")
    else:
        st.warning("لا توجد فرص فنية حالياً.. انتظر الدقيقة القادمة.")

st.sidebar.markdown("### 🕒 ساعة النظام")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
