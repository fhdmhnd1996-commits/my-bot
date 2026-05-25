import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# إعداد الصفحة
st.set_page_config(page_title="Pro OTC Next-Candle", layout="wide")
st.title("🎯 نظام التداول (دخول الشمعة التالية)")

# دالة التحليل مع حساب وقت الشمعة التالية
def find_opportunities():
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    # التوقيت الحالي
    now = datetime.utcnow() + timedelta(hours=3)
    entry_time = now.strftime("%H:%M")
    # وقت الشمعة القادمة (إضافة دقيقة واحدة)
    next_candle = (now + timedelta(minutes=1)).strftime("%H:%M")
    
    for pair in pairs:
        # محاكاة مؤشرات
        rsi = np.random.randint(20, 80)
        volume = np.random.uniform(0.5, 2.0)
        
        # منطق اتخاذ القرار
        if rsi < 35 and volume > 1.5:
            decision = "🟢 شراء (دخول الشمعة التالية)"
        elif rsi > 65 and volume > 1.5:
            decision = "🔴 بيع (دخول الشمعة التالية)"
        else:
            decision = "⚪ انتظار"
            
        data.append({
            "الزوج": pair,
            "وقت الدخول": entry_time,
            "وقت انتهاء الصفقة": next_candle,
            "القرار": decision
        })
    return pd.DataFrame(data)

# الواجهة
if st.button("🚀 ابحث عن فرص الشمعة القادمة"):
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
    
    # ملاحظة توجيهية
    if not df[df['القرار'] != "⚪ انتظار"].empty:
        st.success("تنبيه: أدخل الصفقة مع بداية الشمعة التالية (في الوقت الموضح في الجدول).")

st.sidebar.write(f"🕒 الوقت الحالي: **{(datetime.utcnow() + timedelta(hours=3)).strftime('%H:%M:%S')}**")
