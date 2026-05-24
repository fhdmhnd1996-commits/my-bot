import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro 1M OTC System", layout="wide")
st.title("🎯 نظام التداول بدقيقة (SR + Chandelier)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M')}**")

# --- محاكاة المؤشرات ---
def get_market_data():
    data = []
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    for pair in pairs:
        price = random.uniform(1.0500, 1.1000)
        sr_signal = random.choice(["Breakout Up", "Breakout Down", "None"])
        chandelier_trend = random.choice(["Bullish", "Bearish"])
        
        # وقت الانتهاء: بعد دقيقة واحدة (بالساعة والدقيقة فقط)
        expiry_time = (platform_time + timedelta(minutes=1)).strftime('%H:%M')
        
        data.append({
            "الزوج": pair, 
            "السعر": f"{price:.4f}", 
            "إشارة SR": sr_signal, 
            "الاتجاه": chandelier_trend,
            "وقت الانتهاء": expiry_time
        })
    return pd.DataFrame(data)

# --- منطق الدمج ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        if row['إشارة SR'] == "Breakout Up" and row['الاتجاه'] == "Bullish":
            row['القرار'] = "🟢 شراء (1M)"
        elif row['إشارة SR'] == "Breakout Down" and row['الاتجاه'] == "Bearish":
            row['القرار'] = "🔴 بيع (1M)"
        else:
            row['القرار'] = "⚪ انتظار"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 تحليل صفقات الدقيقة الواحدة"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    # عرض الفرص القوية فقط
    final_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not final_df.empty:
        st.table(final_df[['الزوج', 'السعر', 'القرار', 'وقت الانتهاء']])
        st.success("تم تحديد صفقات 1M القوية بنجاح.")
    else:
        st.warning("لا توجد فرص قوية للدقيقة الواحدة حالياً.. انتظر اكتمال الاختراق.")
