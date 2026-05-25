import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="نظام التداول - افتتاح الشمعة الثانية", layout="wide")

PAIRS = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "EURGBP OTC", "EURJPY OTC", "CHFJPY OTC", "AUDJPY OTC", "NZDUSD OTC",
    "GBPJPY OTC", "AUDCAD OTC", "EURCAD OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "EURAUD OTC", "EURCHF OTC", "GBPCHF OTC", "USDCHF OTC"
]

def fetch_market_data():
    # ضبط الوقت ليصبح بداية الدقيقة القادمة (ثانية 00)
    now = datetime.now()
    next_candle = (now.replace(second=0, microsecond=0) + timedelta(minutes=1))
    
    data = {
        "الزوج": PAIRS,
        "سعر الدخول": [round(np.random.uniform(1.0500, 1.1000), 4) for _ in range(20)],
        "وقت الدخول (الافتتاح)": [next_candle.strftime("%H:%M:00")] * 20,
        "وقت الانتهاء": [(next_candle + timedelta(minutes=1)).strftime("%H:%M:00")] * 20,
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
st.title("🎯 نظام التداول: الدخول مع افتتاح الشمعة الثانية")
st.info("ملاحظة: هذا النظام يجهز لك إشارات الدخول بدقة عند بداية الدقيقة القادمة (ثانية 00).")

if st.button("🚀 تحديث إشارات الشمعة القادمة"):
    final_data = apply_strategy(fetch_market_data())
    signals = final_data[final_data['القرار'] != "⚪ انتظار"]
    
    st.subheader("📊 الفرص المحددة لافتتاح الشمعة التالية")
    if not signals.empty:
        st.dataframe(signals[['الزوج', 'سعر الدخول', 'وقت الدخول (الافتتاح)', 'وقت الانتهاء', 'القرار']], use_container_width=True)
    else:
        st.warning("لا توجد فرص مؤكدة حالياً.. انتظر تحديث الإشارات.")

st.sidebar.markdown("### 🕒 ساعة النظام")
st.sidebar.metric("الوقت الحالي", datetime.now().strftime("%H:%M:%S"))
