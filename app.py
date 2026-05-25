import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام الدمج الذكي (20 زوج OTC)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة الحالي: **{platform_time.strftime('%H:%M:%S')}**")

# --- محاكاة المؤشرات ---
def get_market_data():
    otc_pairs = [
        "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
        "AUDCAD OTC", "EURJPY OTC", "GBPJPY OTC", "NZDUSD OTC", "AUDJPY OTC",
        "EURGBP OTC", "EURCAD OTC", "CHFJPY OTC", "GBPCAD OTC", "CADJPY OTC",
        "AUDNZD OTC", "NZDJPY OTC", "EURCHF OTC", "GBPCHF OTC", "AUDCHF OTC"
    ]
    data = []
    for pair in otc_pairs:
        sr_break = random.choice(["Breakout Up", "Breakout Down", "None"])
        chandelier = random.choice(["Bullish", "Bearish"])
        chello = random.choice(["Strong Buy", "Strong Sell", "Neutral"])
        system_ster = random.choice(["Buy", "Sell", "Neutral"])
        
        data.append({
            "الزوج": pair,
            "SR Breaks": sr_break,
            "Chandelier": chandelier,
            "Chello Pro": chello,
            "System Ster": system_ster
        })
    return pd.DataFrame(data)

# --- منطق الدمج (نظام النقاط + وقت الدخول) ---
def analyze_combined_system(df):
    results = []
    # التقاط وقت الدخول الفعلي الآن
    entry_time = datetime.utcnow() + timedelta(hours=3)
    
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
            row['القرار'] = "🟢 شراء قوي"
            row['وقت الدخول'] = entry_time.strftime('%H:%M:%S')
        elif sell_score >= 3:
            row['القرار'] = "🔴 بيع قوي"
            row['وقت الدخول'] = entry_time.strftime('%H:%M:%S')
        else:
            row['القرار'] = "⚪ انتظار"
            row['وقت الدخول'] = "-"
        
        row['قوة الإشارة'] = f"{max(score, sell_score)}/4"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ تحليل الدمج الذكي"):
    df = get_market_data()
    final_df = analyze_combined_system(df)
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        # عرض الجدول مع وقت الدخول
        st.table(display_df[['الزوج', 'قوة الإشارة', 'القرار', 'وقت الدخول']])
    else:
        st.warning("لا توجد فرص دمج قوية حالياً.. حاول مجدداً بعد ثوانٍ.")

st.markdown("""
### ملاحظة للمتداول:
* **وقت الدخول:** هو اللحظة الدقيقة التي ضغطت فيها على زر المسح.
* إذا ظهرت إشارة، يُفضل دخول الصفقة خلال أول 15-30 ثانية من وقت الدخول الموضح.
""")
