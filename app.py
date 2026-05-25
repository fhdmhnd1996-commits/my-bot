import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Professional Trading System", layout="wide")

# --- دالة محاكاة بيانات السوق مع توقيت الدخول ---
def fetch_market_data():
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    
    # الحصول على الوقت الحالي (ساعة ودقيقة فقط)
    current_time = datetime.now()
    entry_time_str = current_time.strftime("%H:%M")
    # وقت الانتهاء بعد دقيقة
    expiry_time_str = (current_time + timedelta(minutes=1)).strftime("%H:%M")
    
    data = {
        "الزوج": pairs,
        "سعر الدخول": [np.random.uniform(1.0500, 1.1000) for _ in range(5)],
        "وقت الدخول": [entry_time_str] * 5,
        "وقت الانتهاء": [expiry_time_str] * 5,
        "SR_Breaks": [np.random.choice(["Breakout Up", "Breakout Down", "None"]) for _ in range(5)],
        "Chandelier": [np.random.choice(["Bullish", "Bearish"]) for _ in range(5)],
        "Chello_Pro": [np.random.choice(["Strong Buy", "Strong Sell", "Neutral"]) for _ in range(5)]
    }
    return pd.DataFrame(data)

# --- دالة التحليل المنطقي ---
def apply_strategy(df):
    def check_signal(row):
        if row['SR_Breaks'] == "Breakout Up" and row['Chandelier'] == "Bullish" and row['Chello_Pro'] == "Strong Buy":
            return "🟢 شراء (Buy)"
        elif row['SR_Breaks'] == "Breakout Down" and row['Chandelier'] == "Bearish" and row['Chello_Pro'] == "Strong Sell":
            return "🔴 بيع (Sell)"
        return "⚪ انتظار"

    df['القرار'] = df.apply(check_signal, axis=1)
    return df

# --- الواجهة الرئيسية ---
st.title("🎯 نظام التحليل الرباعي (دخول دقيق)")

if st.button("🚀 تحديث وتحليل السوق"):
    raw_data = fetch_market_data()
    final_data = apply_strategy(raw_data)
    
    st.subheader("📊 الصفقات المؤكدة")
    signals = final_data[final_data['القرار'] != "⚪ انتظار"]
    
    if not signals.empty:
        # عرض البيانات الأساسية فقط بما فيها الأوقات بالدقائق
        st.dataframe(signals[['الزوج', 'سعر الدخول', 'وقت الدخول', 'وقت الانتهاء', 'القرار']], use_container_width=True)
    else:
        st.info("لا توجد فرص مطابقة للشروط حالياً.")

    with st.expander("
