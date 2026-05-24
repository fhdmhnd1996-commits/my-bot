import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro Full-OTC Analyzer", layout="wide")
st.title("🎯 نظام التداول الرباعي الشامل (جميع أزواج OTC)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M')}**")

# قائمة بجميع أزواج الـ OTC المتاحة
otc_pairs = [
    "EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC",
    "AUDCAD OTC", "EURJPY OTC", "GBPJPY OTC", "NZDUSD OTC", "AUDJPY OTC"
]

# --- محاكاة المؤشرات الرباعية لكل الأزواج ---
def get_market_data():
    data = []
    for pair in otc_pairs:
        price = random.uniform(1.0500, 1.1000)
        sr_break = random.choice(["Breakout Up", "Breakout Down", "None"])
        chandelier = random.choice(["Bullish", "Bearish"])
        chello = random.choice(["Strong Buy", "Strong Sell", "Neutral"])
        
        expiry_time = (platform_time + timedelta(minutes=1)).strftime('%H:%M')
        
        data.append({
            "الزوج": pair, 
            "السعر": f"{price:.4f}", 
            "SR Breaks": sr_break,
            "Chandelier": chandelier,
            "Chello Pro": chello,
            "وقت الانتهاء": expiry_time
        })
    return pd.DataFrame(data)

# --- منطق الدمج الرباعي ---
def analyze_combined_system(df):
    results = []
    for _, row in df.iterrows():
        # الفلترة الرباعية الصارمة
        if (row['SR Breaks'] == "Breakout Up" and 
            row['Chandelier'] == "Bullish" and 
            row['Chello Pro'] == "Strong Buy"):
            row['القرار'] = "🟢 شراء (1M)"
            
        elif (row['SR Breaks'] == "Breakout Down" and 
              row['Chandelier'] == "Bearish" and 
              row['Chello Pro'] == "Strong Sell"):
            row['القرار'] = "🔴 بيع (1M)"
        else:
            row['القرار'] = "⚪ انتظار"
        results.append(row)
    return pd.DataFrame(results)

# --- الواجهة ---
if st.button("🚀 ابدأ مسح جميع أزواج OTC"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    # عرض النتائج القوية فقط من جميع الأزواج
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df[['الزوج', 'السعر', 'SR Breaks', 'Chandelier', 'Chello Pro', 'القرار', 'وقت الانتهاء']])
        st.success("تم العثور على فرص قوية في قائمة الـ OTC الشاملة.")
    else:
        st.warning("لا توجد فرص مطابقة للشروط الرباعية في أي من الأزواج حالياً.. السوق هادئ.")

st.markdown("""
### ملاحظة للمتداول:
* هذا الكود الآن يمسح **10 أزواج** في آن واحد.
* **قاعدة ذهبية:** لا تفتح أكثر من صفقة واحدة في نفس التوقيت، حتى لو ظهرت إشارات في أزواج مختلفة، لتجنب تشتت رأس المال.
""")
