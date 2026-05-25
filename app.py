import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام الدمج الذكي (20 زوج OTC)")

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
        # محاكاة حالة المؤشرات
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

# --- منطق الدمج (نظام النقاط) ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        score = 0
        
        # منح نقاط لاتجاه الشراء
        if row['SR Breaks'] == "Breakout Up": score += 1
        if row['Chandelier'] == "Bullish": score += 1
        if row['Chello Pro'] == "Strong Buy": score += 1
        if row['System Ster'] == "Buy": score += 1
        
        # منح نقاط لاتجاه البيع
        sell_score = 0
        if row['SR Breaks'] == "Breakout Down": sell_score += 1
        if row['Chandelier'] == "Bearish": sell_score += 1
        if row['Chello Pro'] == "Strong Sell": sell_score += 1
        if row['System Ster'] == "Sell": sell_score += 1
        
        # اتخاذ القرار بناءً على الدمج
        if score >= 3:
            row['القرار'] = "🟢 شراء قوي"
        elif sell_score >= 3:
            row['القرار'] = "🔴 بيع قوي"
        else:
            row['القرار'] = "⚪ انتظار"
        
        row['قوة الإشارة'] = f"{max(score, sell_score)}/4"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ تحليل الدمج الذكي"):
    df = get_market_data()
    final_df = analyze_combined_system(df)
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df)
    else:
        st.warning("لا توجد فرص دمج قوية حالياً (تحتاج 3/4 مؤشرات على الأقل).")

st.markdown("""
### كيف يعمل الدمج؟
* النظام الآن يمنح **نقطة واحدة لكل مؤشر**.
* لا تظهر الإشارة إلا إذا حصل الزوج على **3 أو 4 نقاط** (مصداقية أعلى).
* هذا يحميك من الإشارات الكاذبة التي قد تأتي من مؤشر واحد فقط.
""")
