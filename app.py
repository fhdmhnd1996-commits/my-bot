import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="نظام التداول الرباعي المطور", layout="wide")

# --- قائمة الـ 20 سوق OTC ---
PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

# --- دالة توليد بيانات السوق ---
def fetch_market_data():
    current_time = datetime.now()
    entry_time = current_time.strftime("%H:%M")
    expiry_time = (current_time + timedelta(minutes=1)).strftime("%H:%M")
    
    data = {
        "الزوج": PAIRS,
        "سعر الدخول": [round(np.random.uniform(1.0500, 1.1000), 4) for _ in range(20)],
        "وقت الدخول": [entry_time] * 20,
        "وقت الانتهاء": [expiry_time] * 20,
        "SR_Breaks": [np.random.choice(["Breakout Up", "Breakout Down", "None"], p=[0.2, 0.2, 0.6]) for _ in range(20)],
        "Chandelier": [np.random.choice(["Bullish", "Bearish"]) for _ in range(20)],
        "Chello_Pro": [np.random.choice(["Strong Buy", "Strong Sell", "Neutral"]) for _ in range(20)]
    }
    return pd.DataFrame(data)

# --- دالة التحليل مع تحديد الاتجاه ---
def apply_strategy(df):
    def check_signal(row):
        if row['SR_Breaks'] == "Breakout Up" and row['Chandelier'] == "Bullish" and row['Chello_Pro'] == "Strong Buy":
            return "🟢 صعود (شراء)"
        elif row['SR_Breaks'] == "Breakout Down" and row['Chandelier'] == "Bearish" and row['Chello_Pro'] == "Strong Sell":
            return "🔴 هبوط (بيع)"
        return "⚪ انتظار"

    df['القرار'] = df.apply(check_signal, axis=1)
    return df

# --- الواجهة ---
st.title("🎯 نظام التحليل الرباعي (صعود / هبوط)")

if st.button("🚀 تحليل الأسواق الـ 20"):
    raw_data = fetch_market_data()
    final_data = apply_strategy(raw_data)
    
    # فلترة النتائج
    signals = final_data[final_data['القرار'] != "⚪ انتظار"]
    
    st.subheader("📊 الفرص المتاحة (التوجه الحالي)")
    if not signals.empty:
        # عرض النتائج مع توضيح صريح للاتجاه
        st.dataframe(signals[['الزوج', 'سعر الدخول', 'وقت الانتهاء', 'القرار']], use_container_width=True)
    else:
        st.warning("لا توجد فرص مطابقة للشروط حالياً. السوق في حالة تذبذب (انتظار).")

    with st.expander("📋 عرض حالة جميع الأسواق"):
        st.table(final_data)

st.sidebar.markdown("### 🛠 إعدادات النظام")
st.sidebar.write(f"تحديث: {datetime.now().strftime('%H:%M:%S')}")
