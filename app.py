import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro 1M OTC System", layout="wide")
st.title("🎯 نظام التداول الاحترافي (Chello Pro + SR + Chandelier)")

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
        # محاكاة مؤشر Chello Pro (يعطي إشارة زخم)
        chello_pro = random.choice(["Strong Buy", "Strong Sell", "Neutral"])
        
        expiry_time = (platform_time + timedelta(minutes=1)).strftime('%H:%M')
        
        data.append({
            "الزوج": pair, 
            "السعر": f"{price:.4f}", 
            "إشارة SR": sr_signal, 
            "الاتجاه": chandelier_trend,
            "Chello Pro": chello_pro,
            "وقت الانتهاء": expiry_time
        })
    return pd.DataFrame(data)

# --- منطق الدمج الثلاثي ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        # الفلترة الثلاثية: لا يدخل إلا إذا اتفقت المؤشرات الثلاثة
        if (row['إشارة SR'] == "Breakout Up" and 
            row['الاتجاه'] == "Bullish" and 
            row['Chello Pro'] == "Strong Buy"):
            row['القرار'] = "🟢 شراء (1M)"
            
        elif (row['إشارة SR'] == "Breakout Down" and 
              row['الاتجاه'] == "Bearish" and 
              row['Chello Pro'] == "Strong Sell"):
            row['القرار'] = "🔴 بيع (1M)"
        else:
            row['القرار'] = "⚪ انتظار"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 تحليل صفقات 1M (نظام الدمج الثلاثي)"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    # عرض الفرص التي اتفقت فيها المؤشرات الثلاثة فقط
    final_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not final_df.empty:
        st.table(final_df[['الزوج', 'السعر', 'Chello Pro', 'القرار', 'وقت الانتهاء']])
        st.success("تم تأكيد الصفقات بناءً على تقاطع المؤشرات الثلاثة.")
    else:
        st.warning("لا توجد إشارات دخول مؤكدة حالياً.. الفلترة الثلاثية صارمة جداً لتجنب الخسارة.")
