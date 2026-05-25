import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Scanner OTC Pro | Edge Algo + Spot-0079 + S/R", layout="wide")

PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def get_entry_data():
    now = datetime.now()
    entry_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    return entry_time.strftime("%H:%M:%S"), expiry_time.strftime("%H:%M:%S")

def check_indicators_logic():
    # محاكاة المؤشرات السابقة
    spot_0079 = np.random.choice(["Active", "Inactive"], p=[0.6, 0.4])
    edge_algo = np.random.choice(["Signal Up", "Signal Down", "Neutral"], p=[0.2, 0.2, 0.6])
    
    # محاكاة مؤشر الدعم والمقاومة (S/R)
    sr_level = np.random.choice(["Near Support", "Near Resistance", "No Level"])
    
    # منطق القرار: دمج المؤشرات الثلاثة
    if spot_0079 == "Active" and edge_algo == "Signal Up" and sr_level == "Near Support":
        return "🟢 صعود (Buy)", spot_0079, edge_algo, sr_level
    elif spot_0079 == "Active" and edge_algo == "Signal Down" and sr_level == "Near Resistance":
        return "🔴 هبوط (Sell)", spot_0079, edge_algo, sr_level
    
    return "⚪ انتظار", spot_0079, edge_algo, sr_level

st.title("🛡️ نظام التداول الرباعي (Edge Algo + Spot-0079 + S/R)")

if st.button("🚀 تحليل الأسواق بنظام الدمج الثلاثي"):
    entry, expiry = get_entry_data()
    results = []
    
    for pair in PAIRS:
        decision, spot_status, edge_status, sr_status = check_indicators_logic()
        results.append({
            "الزوج": pair,
            "القرار": decision,
            "Spot-0079": spot_status,
            "Edge Algo": edge_status,
            "S/R Level": sr_status,
            "وقت الدخول": entry,
            "وقت الانتهاء": expiry
        })
    
    df = pd.DataFrame(results)
    signals = df[df['القرار'] != "⚪ انتظار"]
    
    if not signals.empty:
        st.subheader(f"📊 فرص دخول مؤكدة عند الساعة {entry}")
        st.dataframe(signals, use_container_width=True)
    else:
        st.warning("لم يتم توافق إشارات المؤشرات (بما فيها الدعم والمقاومة) حالياً.")

    with st.expander("📋 عرض حالة جميع الأسواق"):
        st.table(df)

st.sidebar.markdown("### 🕒 نظام التوقيت")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
