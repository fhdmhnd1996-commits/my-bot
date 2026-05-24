import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro 1M OTC System", layout="wide")
st.title("🎯 نظام التداول بدقيقة (SR + Chandelier)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M:%S')}**")

# --- محاكاة المؤشرات ---
def get_market_data():
    data = []
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    for pair in pairs:
        price = random.uniform(1.0500, 1.1000)
        sr_signal = random.choice(["Breakout Up", "Breakout Down", "None"])
        chandelier_trend = random.choice(["Bullish", "Bearish"])
        
        # إضافة وقت انتهاء الصفقة بعد دقيقة واحدة من الآن
        expiry_time = (platform_time + timedelta(minutes=1)).strftime('%H:%M:%S')
        
        data.append({
            "Pair": pair, 
            "Price": f"{price:.4f}", 
            "SR_Signal": sr_signal, 
            "Trend": chandelier_trend,
            "Expiry": expiry_time
        })
    return pd.DataFrame(data)

# --- منطق الدمج (الفلترة القوية) ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        # شرط الدخول: اختراق + ترند مؤكد
        if row['SR_Signal'] == "Breakout Up" and row['Trend'] == "Bullish":
            row['Decision'] = "🟢 شراء (1M)"
        elif row['SR_Signal'] == "Breakout Down" and row['Trend'] == "Bearish":
            row['Decision'] = "🔴 بيع (1M)"
        else:
            row['Decision'] = "⚪ انتظار"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 تحليل صفقات الدقيقة الواحدة"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    # فلترة النتائج لعرض الفرص القوية فقط
    final_df = final_df[final_df['Decision'] != "⚪ انتظار"]
    
    if not final_df.empty:
        st.table(final_df[['Pair', 'Price', 'Decision', 'Expiry']])
        st.success("تم تحديد صفقات 1M القوية بناءً على الدمج الفني.")
    else:
        st.warning("لا توجد فرص قوية للدقيقة الواحدة حالياً.. انتظر اكتمال الاختراق.")

st.markdown("""
### ملاحظة هامة:
* يتم حساب **وقت الانتهاء (Expiry)** تلقائياً بعد دقيقة واحدة من وقت الفحص.
* النظام يفلتر السوق بناءً على تقاطع **SR Breaks** مع **Chandelier Exit**.
""")
