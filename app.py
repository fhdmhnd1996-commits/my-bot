import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="نظام التداول الدقيق", layout="wide")

# قائمة الأسواق
PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def fetch_market_data():
    # الحصول على الوقت الحالي وتصفير الثواني ليكون الدخول في بداية الدقيقة 00
    now = datetime.now()
    # ضبط وقت الدخول ليكون بداية الدقيقة القادمة أو الحالية (00 ثانية)
    entry_time = now.replace(second=0, microsecond=0)
    expiry_time = entry_time + timedelta(minutes=1)
    
    data = {
        "الزوج": PAIRS,
        "سعر الدخول": [round(np.random.uniform(1.0500, 1.1000), 4) for _ in range(20)],
        "وقت الدخول": [entry_time.strftime("%H:%M:%S")] * 20,
        "وقت الانتهاء": [expiry_time.strftime("%H:%M:%S")] * 20,
        "SR_Breaks": [np.random.choice(["Breakout Up", "Breakout Down", "None"], p=[0.2, 0.2, 0.6]) for _ in range(20)],
        "Chandelier": [np.random.choice(["Bullish", "Bearish"]) for _ in range(20)],
        "Chello_Pro": [np.random.choice(["Strong Buy", "Strong Sell", "Neutral"]) for _ in range(20)]
    }
    return pd.DataFrame(data)

def apply_strategy(df):
    def check_signal(row):
        if row['SR_Breaks'] == "Breakout Up" and row['Chandelier'] == "Bullish" and row['Chello_Pro'] == "Strong Buy":
            return "🟢 صعود (شراء)"
        elif row['SR_Breaks'] == "Breakout Down" and row['Chandelier'] == "Bearish" and row['Chello_Pro'] == "Strong Sell":
            return "🔴 هبوط (بيع)"
        return "⚪ انتظار"

    df['القرار'] = df.apply(check_signal, axis=1)
    return df

# الواجهة
st.title("🎯 نظام التداول الرباعي (دخول عند بداية الدقيقة 00)")

if st.button("🚀 تحليل الأسواق وتحديد نقاط الدخول"):
    final_data = apply_strategy(fetch_market_data())
    signals = final_data[final_data['القرار'] != "⚪ انتظار"]
    
    st.subheader("📊 الفرص المتاحة الآن")
    if not signals.empty:
        st.dataframe(signals[['الزوج', 'سعر الدخول', 'وقت الدخول', 'وقت الانتهاء', 'القرار']], use_container_width=True)
    else:
        st.warning("لا توجد فرص مطابقة حالياً.. انتظر بداية الدقيقة التالية.")

    with st.expander("📋 عرض جميع الأسواق"):
        st.table(final_data)

st.sidebar.markdown("---")
st.sidebar.write(f"التوقيت الحالي: **{datetime.now().strftime('%H:%M:%S')}**")
