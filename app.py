import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Scanner OTC Pro", layout="wide")

# قائمة الـ 20 زوج OTC
PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def get_entry_data():
    """حساب وقت الدخول مع بداية الشمعة القادمة (الثانية 00)"""
    now = datetime.now()
    # الدخول سيكون دائماً عند بداية الدقيقة القادمة
    entry_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    return entry_time.strftime("%H:%M:%S"), expiry_time.strftime("%H:%M:%S")

def get_signal():
    """محاكاة منطق فني (RSI)"""
    val = np.random.uniform(0, 100)
    if val < 30:
        return "🟢 صعود (شراء)"
    elif val > 70:
        return "🔴 هبوط (بيع)"
    return "⚪ انتظار"

st.title("🛡️ ماسح الـ 20 زوج OTC (توقيت الشمعة الثانية)")

if st.button("🚀 فحص جميع الأزواج الآن"):
    entry, expiry = get_entry_data()
    results = []
    
    for pair in PAIRS:
        signal = get_signal()
        results.append({
            "الزوج": pair,
            "القرار": signal,
            "وقت الدخول": entry,
            "وقت الانتهاء": expiry
        })
    
    df = pd.DataFrame(results)
    
    # عرض الفرص المتاحة فقط في الأعلى
    signals = df[df['القرار'] != "⚪ انتظار"]
    
    if not signals.empty:
        st.subheader(f"📊 الفرص المتاحة عند الساعة {entry}")
        st.dataframe(signals, use_container_width=True)
    else:
        st.warning("لا توجد فرص مطابقة حالياً.. جرب التحديث مرة أخرى.")

    with st.expander("📋 عرض حالة جميع الـ 20 زوج"):
        st.table(df)

st.sidebar.markdown("### 🕒 توقيت النظام")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
