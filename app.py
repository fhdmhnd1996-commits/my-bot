import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Scanner OTC Pro + spot-0079", layout="wide")

# قائمة الـ 20 زوج OTC
PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def get_entry_data():
    """حساب وقت الدخول بدقة (بداية الدقيقة القادمة :00)"""
    now = datetime.now()
    entry_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    return entry_time.strftime("%H:%M:%S"), expiry_time.strftime("%H:%M:%S")

def get_signal_with_spot0079():
    """محاكاة منطق المؤشرات + فلتر spot-0079"""
    # محاكاة المؤشرات الأساسية
    rsi = np.random.uniform(0, 100)
    # حالة مؤشر spot-0079 (محاكاة لحالته الفنية)
    spot_0079 = np.random.choice(["Active", "Inactive"])
    
    # المنطق: لا إشارة صعود أو هبوط إلا إذا كان spot-0079 فعالاً
    if spot_0079 == "Active":
        if rsi < 30:
            return "🟢 صعود (شراء)", "Active"
        elif rsi > 70:
            return "🔴 هبوط (بيع)", "Active"
    
    return "⚪ انتظار", spot_0079

st.title("🛡️ ماسح الـ 20 زوج OTC (نظام spot-0079)")

if st.button("🚀 فحص الأسواق بنظام spot-0079"):
    entry, expiry = get_entry_data()
    results = []
    
    for pair in PAIRS:
        signal, spot_status = get_signal_with_spot0079()
        results.append({
            "الزوج": pair,
            "القرار": signal,
            "حالة spot-0079": spot_status,
            "وقت الدخول": entry,
            "وقت الانتهاء": expiry
        })
    
    df = pd.DataFrame(results)
    
    # عرض الفرص المتاحة (التي تحقق الشروط)
    signals = df[(df['القرار'] != "⚪ انتظار") & (df['حالة spot-0079'] == "Active")]
    
    if not signals.empty:
        st.subheader(f"📊 فرص دخول مؤكدة بـ spot-0079 عند الساعة {entry}")
        st.dataframe(signals, use_container_width=True)
    else:
        st.warning("لم يتم تأكيد أي صفقة بواسطة مؤشر spot-0079 حالياً.")

    with st.expander("📋 عرض حالة جميع الأسواق (20 زوج)"):
        st.table(df)

st.sidebar.markdown("### 🕒 نظام التوقيت")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
