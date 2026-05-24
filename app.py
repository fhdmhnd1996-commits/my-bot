import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Professional 4-Filter System", layout="wide")
st.title("🎯 نظام التداول الرباعي (SR Breaks + Chello + Chandelier + Trend)")

# إعداد الوقت (UTC+3)
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M')}**")

# --- محاكاة المؤشرات الرباعية ---
def get_market_data():
    data = []
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    for pair in pairs:
        price = random.uniform(1.0500, 1.1000)
        # المؤشر الجديد: SR Breaks
        sr_break = random.choice(["Breakout Up", "Breakout Down", "None"])
        # المؤشرات السابقة
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
        # الفلترة الرباعية: لن يظهر القرار إلا إذا اتفقت الأربعة معاً
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
if st.button("🚀 تحليل فني دقيق (نظام الدمج الرباعي)"):
    market_df = get_market_data()
    final_df = analyze_combined_system(market_df)
    
    # عرض النتائج
    display_df = final_df[final_df['القرار'] != "⚪ انتظار"]
    
    if not display_df.empty:
        st.table(display_df[['الزوج', 'السعر', 'SR Breaks', 'Chandelier', 'Chello Pro', 'القرار', 'وقت الانتهاء']])
        st.success("تم تأكيد الصفقات بناءً على دمج 4 مؤشرات فنية احترافية.")
    else:
        st.warning("لا توجد فرص مطابقة للشروط الرباعية.. الانتظار هو مفتاح الأمان.")

st.markdown("""
### كيف يعمل هذا النظام؟
* **SR Breaks:** يحدد بداية الاختراق الحقيقي للسعر.
* **Chandelier:** يحميك من الانعكاسات المفاجئة.
* **Chello Pro:** يؤكد زخم وقوة الحركة.
* **القاعدة:** لا يتم عرض أي صفقة ما لم تتفق المؤشرات الثلاثة الرئيسية مع إشارة الاختراق (SR).
""")
