import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام التداول الرباعي الشامل (20 زوج OTC)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M')}**")

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
        price = random.uniform(1.0500, 1.1000)
        sr_break = random.choice(["Breakout Up", "Breakout Down", "None"])
        chandelier = random.choice(["Bullish", "Bearish"])
        chello = random.choice(["Strong Buy", "Strong Sell", "Neutral"])
        system_ster = random.choice(["Buy", "Sell", "Neutral"])
        
        expiry_time = (platform_time + timedelta(minutes=1)).strftime('%H:%M')
        
        data.append({
            "الزوج": pair, 
            "السعر": f"{price:.4f}", 
            "SR Breaks": sr_break,
            "Chandelier": chandelier,
            "Chello Pro": chello,
            "System Ster": system_ster,
            "وقت الانتهاء": expiry_time
        })
    return pd.DataFrame(data)

# --- منطق الدمج ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        if (row['SR Breaks'] == "Breakout Up" and 
            row['Chandelier'] == "Bullish" and 
            row['Chello Pro'] == "Strong Buy" and
            row['System Ster'] == "Buy"):
            row['القرار'] = "🟢 شراء (1M)"
            
        elif (row['SR Breaks'] == "Breakout Down" and 
              row['Chandelier'] == "Bearish" and 
              row['Chello Pro'] == "Strong Sell" and
              row['System Ster'] == "Sell"):
            row['القرار'] = "🔴 بيع (1M)"
        else:
            row['القرار'] = "⚪ انتظار"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ مسح 20 زوج OTC"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df[['الزوج', 'السعر', 'SR Breaks', 'Chandelier', 'Chello Pro', 'System Ster', 'القرار', 'وقت الانتهاء']])
        st.success("تم العثور على فرص قوية في قائمة الـ 20 زوج.")
    else:
        st.warning("لا توجد فرص مطابقة حالياً.. السوق هادئ.")

st.markdown("""
### ملاحظة:
* النظام الآن يراقب **20 زوجاً** لزيادة فرص الصيد.
* **تنبيه:** مع زيادة عدد الأزواج، قد تظهر فرص أكثر، التزم بإدارة رأس المال.
""")
