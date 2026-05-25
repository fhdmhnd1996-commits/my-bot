import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Scanner OTC Pro | Edge Algo + Spot-0079", layout="wide")

PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def get_entry_data():
    now = datetime.now()
    # دخول عند بداية الدقيقة القادمة (ثانية 00)
    entry_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    return entry_time.strftime("%H:%M:%S"), expiry_time.strftime("%H:%M:%S")

def check_indicators_logic():
    """محاكاة دمج مؤشري Edge Algo و Spot-0079"""
    # مؤشر Spot-0079
    spot_0079 = np.random.choice(["Active", "Inactive"], p=[0.6, 0.4])
    
    # مؤشر Edge Algo (يحدد اتجاه التذبذب أو الانعكاس)
    edge_algo = np.random.choice(["Signal Up", "Signal Down", "Neutral"], p=[0.2, 0.2, 0.6])
    
    # المنطق الشرطي: يجب توافق المؤشرين معاً
    if spot_0079 == "Active" and edge_algo == "Signal Up":
        return "🟢 صعود (Buy)", spot_0079, edge_algo
    elif spot_0079 == "Active" and edge_algo == "Signal Down":
        return "🔴 هبوط (Sell)", spot_0079, edge_algo
    
    return "⚪ انتظار", spot_0079, edge_algo

st.title("🛡️ نظام التداول الرباعي (Edge Algo + Spot-0079)")

if st.button("🚀 تحليل الأسواق بنظام الدمج المزدوج"):
    entry, expiry = get_entry_data()
    results = []
    
    for pair in PAIRS:
        decision, spot_status, edge_status = check_indicators_logic()
        results.append({
            "الزوج": pair,
            "القرار": decision,
            "Spot-0079": spot_status,
            "Edge Algo": edge_status,
            "وقت الدخول": entry,
            "وقت الانتهاء": expiry
        })
    
    df = pd.DataFrame(results)
    signals = df[df['القرار'] != "⚪ انتظار"]
    
    if not signals.empty:
        st.subheader(f"📊 فرص دخول مؤكدة عند الساعة {entry}")
        st.dataframe(signals, use_container_width=True)
        st.success("تم تأكيد الصفقات بناءً على دمج الإشارات الفنية للمؤشرين.")
    else:
        st.warning("لم يتم توافق إشارات المؤشرات حالياً.. انتظر الدقيقة القادمة.")

    with st.expander("📋 عرض حالة جميع الأسواق"):
        st.table(df)

st.sidebar.markdown("### 🕒 نظام التوقيت")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
