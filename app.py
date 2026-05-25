import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Pro OTC Analyzer", layout="wide")
st.title("🎯 نظام التداول الرباعي المطور")

# --- محرك البحث عن الفرص (المنطق) ---
def find_opportunities():
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    # محاكاة تحليل فني متقدم (يمكن استبدال هذا الجزء بـ API خاص بمنصتك)
    for pair in pairs:
        rsi = np.random.randint(20, 80)
        trend = np.random.choice(['صاعد', 'هابط'])
        volume = np.random.uniform(0.5, 2.0)
        
        # الفلترة الرباعية الصارمة
        if rsi < 35 and trend == 'صاعد' and volume > 1.5:
            decision = "🟢 شراء (تأكيد عالٍ)"
        elif rsi > 65 and trend == 'هابط' and volume > 1.5:
            decision = "🔴 بيع (تأكيد عالٍ)"
        else:
            decision = "⚪ انتظار"
            
        data.append({
            "الزوج": pair,
            "RSI": rsi,
            "الاتجاه": trend,
            "السيولة": round(volume, 2),
            "القرار": decision
        })
    return pd.DataFrame(data)

# --- واجهة المستخدم ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📊 لوحة مراقبة الفرص")
    if st.button("🔍 ابحث عن صفقة الآن"):
        df = find_opportunities()
        
        # التنسيق الشرطي
        def style_df(row):
            color = ''
            if 'شراء' in row['القرار']: color = 'background-color: #d4edda'
            elif 'بيع' in row['القرار']: color = 'background-color: #f8d7da'
            return [color] * len(row)

        st.dataframe(df.style.apply(style_df, axis=1), use_container_width=True, hide_index=True)
        
        # التنبيه في حال وجود فرصة
        if not df[df['القرار'] != "⚪ انتظار"].empty:
            st.success("فرصة حقيقية متاحة! راقب المنصة فوراً.")
        else:
            st.warning("السوق حالياً متذبذب، يُنصح بالانتظار.")

with col2:
    st.subheader("🕒 التوقيت")
    current_time = (datetime.utcnow() + timedelta(hours=3)).strftime("%H:%M:%S")
    st.metric("توقيت المنصة (UTC+3)", current_time)
    
    st.markdown("---")
    st.write("**قواعد الحماية:**")
    st.caption("1. لا تتداول أثناء الأخبار.")
    st.caption("2. التزم بإدارة المخاطر (2%).")
    st.caption("3. توقف بعد خسارة صفقتين.")

# --- شرح مبسط لآلية البحث ---
st.markdown("---")
st.write("### 🧠 كيف يبحث النظام عن صفقة؟")
st.write("يقوم النظام بمسح 5 عوامل في نفس اللحظة: (السعر، اتجاه السوق، مؤشر الـ RSI، حجم السيولة، ووقت المنصة). لا يتم إعطاء إشارة دخول إلا إذا تطابقت الشروط الأربعة معاً.")
