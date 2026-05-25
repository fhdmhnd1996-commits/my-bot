import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Pro OTC Analyzer", layout="wide")
st.title("🎯 نظام التداول الرباعي (توقيت الدقيقة)")

# دالة التحليل والبحث عن صفقات
def find_opportunities():
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    # التوقيت الحالي بالدقيقة (UTC+3)
    entry_time = (datetime.utcnow() + timedelta(hours=3)).strftime("%H:%M")
    
    for pair in pairs:
        # محاكاة مؤشرات
        rsi = np.random.randint(20, 80)
        volume = np.random.uniform(0.5, 2.0)
        
        # منطق اتخاذ القرار
        if rsi < 35 and volume > 1.5:
            decision = "🟢 شراء (دخول فوري)"
        elif rsi > 65 and volume > 1.5:
            decision = "🔴 بيع (دخول فوري)"
        else:
            decision = "⚪ انتظار"
            
        data.append({
            "الزوج": pair,
            "وقت الدخول": entry_time,
            "RSI": rsi,
            "القرار": decision
        })
    return pd.DataFrame(data)

# الواجهة
if st.button("🚀 ابحث عن صفقة (توقيت الدقيقة)"):
    df = find_opportunities()
    
    # تنسيق الجدول
    def style_rows(row):
        color = ''
        if 'شراء' in row['القرار']: color = 'background-color: #d4edda'
        elif 'بيع' in row['القرار']: color = 'background-color: #f8d7da'
        return [color] * len(row)

    st.dataframe(
        df.style.apply(style_rows, axis=1), 
        use_container_width=True, 
        hide_index=True
    )
    
    # رسالة ذكية
    if not df[df['القرار'] != "⚪ انتظار"].empty:
        st.success(f"تم رصد فرص في تمام الساعة {datetime.utcnow().add(hours=3).strftime('%H:%M')} - نفذ الصفقة الآن!")
    else:
        st.warning("لا توجد فرص مطابقة للشروط حالياً.")

st.sidebar.markdown("---")
st.sidebar.write(f"🕒 توقيت المنصة المعتمد: **{(datetime.utcnow() + timedelta(hours=3)).strftime('%H:%M')}**")
