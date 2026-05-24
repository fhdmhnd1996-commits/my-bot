import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام الدمج الخماسي (20 زوج OTC)")

# التوقيت
now = datetime.utcnow() + timedelta(hours=3)
next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)

# قائمة الـ 20 زوج
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
            "System Ster": random.choice(["Buy", "Sell", "Neutral"]),
            "TPFX": random.choice(["Buy", "Sell", "Neutral"]) # إضافة مؤشر TPFX
        })
    return pd.DataFrame(data)

# --- منطق الدمج (نظام النقاط الخماسي) ---
def analyze_combined_system(df):
    results = []
    entry_time = next_minute.strftime('%H:%M')
    expiry_time = (next_minute + timedelta(minutes=1)).strftime('%H:%M')
    
    for _, row in df.iterrows():
        # حساب نقاط الشراء
        buy_score = 0
        if row['SR Breaks'] == "Breakout Up": buy_score += 1
        if row['Chandelier'] == "Bullish": buy_score += 1
        if row['Chello Pro'] == "Strong Buy": buy_score += 1
        if row['System Ster'] == "Buy": buy_score += 1
        if row['TPFX'] == "Buy": buy_score += 1
        
        # حساب نقاط البيع
        sell_score = 0
        if row['SR Breaks'] == "Breakout Down": sell_score += 1
        if row['Chandelier'] == "Bearish": sell_score += 1
        if row['Chello Pro'] == "Strong Sell": sell_score += 1
        if row['System Ster'] == "Sell": sell_score += 1
        if row['TPFX'] == "Sell": sell_score += 1
        
        # اتخاذ القرار (يتطلب 4/5 على الأقل)
        if buy_score >= 4:
            row['القرار'] = "🟢 شراء (1M)"
            row['وقت الدخول'] = entry_time
            row['وقت الانتهاء'] = expiry_time
            row['قوة الإشارة'] = f"{buy_score}/5"
        elif sell_score >= 4:
            row['القرار'] = "🔴 بيع (1M)"
            row['وقت الدخول'] = entry_time
            row['وقت الانتهاء'] = expiry_time
            row['قوة الإشارة'] = f"{sell_score}/5"
        else:
            row['القرار'] = "⚪ انتظار"
            row['وقت الدخول'] = "-"
            row['وقت الانتهاء'] = "-"
            row['قوة الإشارة'] = "-"
            
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ تحليل الدمج الخماسي"):
    final_df = analyze_combined_system(get_market_data())
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df[['الزوج', 'قوة الإشارة', 'القرار', 'وقت الدخول', 'وقت الانتهاء']])
    else:
        st.warning("لا توجد فرص قوية (4/5) حالياً.. انتظر تحديثاً جديداً.")

st.markdown("### نظام الدمج الخماسي: يتطلب تطابق 4 مؤشرات على الأقل لضمان أعلى دقة ممكنة.")
