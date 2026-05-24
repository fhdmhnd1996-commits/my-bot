import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام الدمج الذكي (20 زوج OTC - توقيت نظامي)")

# إعداد الوقت (UTC+3)
now = datetime.utcnow() + timedelta(hours=3)
next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
st.sidebar.write(f"🕒 توقيت المنصة: **{now.strftime('%H:%M:%S')}**")
st.sidebar.write(f"⏱️ التوقيت القادم لدخول الصفقة: **{next_minute.strftime('%H:%M')}**")

# قائمة بـ 20 زوج OTC
otc_pairs = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "AUDCAD OTC", "EURJPY OTC", "GBPJPY OTC", "NZDUSD OTC", "AUDJPY OTC",
    "EURGBP OTC", "EURCAD OTC", "CHFJPY OTC", "GBPCAD OTC", "CADJPY OTC",
    "AUDNZD OTC", "NZDJPY OTC", "EURCHF OTC", "GBPCHF OTC", "AUDCHF OTC"
]

# --- محاكاة المؤشرات ---
def get_market_data():
    data = []
    for pair in otc_pairs:
        data.append({
            "الزوج": pair,
            "SR Breaks": random.choice(["Breakout Up", "Breakout Down", "None"]),
            "Chandelier": random.choice(["Bullish", "Bearish"]),
            "Chello Pro": random.choice(["Strong Buy", "Strong Sell", "Neutral"]),
            "System Ster": random.choice(["Buy", "Sell", "Neutral"])
        })
    return pd.DataFrame(data)

# --- منطق الدمج (نظام النقاط والتوقيت النظامي) ---
def analyze_combined_system(df):
    results = []
    # تحديد التوقيت بدقة الدقيقة القادمة
    entry_time = next_minute.strftime('%H:%M')
    expiry_time = (next_minute + timedelta(minutes=1)).strftime('%H:%M')
    
    for _, row in df.iterrows():
        score = 0
        if row['SR Breaks'] == "Breakout Up": score += 1
        if row['Chandelier'] == "Bullish": score += 1
        if row['Chello Pro'] == "Strong Buy": score += 1
        if row['System Ster'] == "Buy": score += 1
        
        sell_score = 0
        if row['SR Breaks'] == "Breakout Down": sell_score += 1
        if row['Chandelier'] == "Bearish": sell_score += 1
        if row['Chello Pro'] == "Strong Sell": sell_score += 1
        if row['System Ster'] == "Sell": sell_score += 1
        
        if score >= 3:
            row['القرار'] = "🟢 شراء (1M)"
            row['وقت الدخول'] = entry_time
            row['وقت الانتهاء'] = expiry_time
            row['قوة الإشارة'] = f"{score}/4"
        elif sell_score >= 3:
            row['القرار'] = "🔴 بيع (1M)"
            row['وقت الدخول'] = entry_time
            row['وقت الانتهاء'] = expiry_time
            row['قوة الإشارة'] = f"{sell_score}/4"
        else:
            row['القرار'] = "⚪ انتظار"
            row['وقت الدخول'] = "-"
            row['وقت الانتهاء'] = "-"
            row['قوة الإشارة'] = "-"
            
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ مسح السوق الآن"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df[['الزوج', 'قوة الإشارة', 'القرار', 'وقت الدخول', 'وقت الانتهاء']])
    else:
        st.warning("لا توجد فرص قوية حالياً. انتظر بداية الدقيقة الجديدة.")

st.markdown("""
### ملاحظات هامة:
* النظام يقوم بمسح **20 زوجاً** فورياً.
* **التوقيت:** وقت الدخول في الجدول هو **بداية الدقيقة القادمة** لضمان دقة صفقات الـ 1M.
* لا تفتح أكثر من صفقة في نفس الوقت لتجنب التشتت.
""")
