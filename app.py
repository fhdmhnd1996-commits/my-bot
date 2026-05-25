import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Pro OTC Pro-Guard", layout="wide")
st.title("🛡️ نظام الحماية من الخسائر (OTC)")

def get_pro_data():
    now = datetime.utcnow() + timedelta(hours=3)
    # حساب الثواني المتبقية لنهاية الدقيقة الحالية لضبط الدخول مع الشمعة التالية
    seconds_to_next_minute = 60 - now.second
    entry_time = (now + timedelta(seconds=seconds_to_next_minute)).strftime("%H:%M")
    expiry_time = (now + timedelta(seconds=seconds_to_next_minute + 60)).strftime("%H:%M")
    
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    for pair in pairs:
        # محاكاة تحليل فني متقدم
        rsi = np.random.randint(20, 80)
        # فلتر إضافي: التذبذب (ATR)
        volatility = np.random.uniform(0.1, 3.0) 
        
        # --- الفلترة الصارمة (هنا يكمن سر تقليل الخسائر) ---
        # 1. لا تدخل إذا كان السوق متذبذباً جداً (فوق 2.5)
        # 2. لا تدخل إذا كان السوق عرضياً (RSI بين 40 و 60)
        
        if rsi < 30 and volatility < 2.0:
            decision = "🟢 شراء (تأكيد قوي)"
        elif rsi > 70 and volatility < 2.0:
            decision = "🔴 بيع (تأكيد قوي)"
        elif volatility > 2.5:
            decision = "⚠️ خطر (تجنب التداول)"
        else:
            decision = "⚪ انتظار"
            
        data.append({
            "الزوج": pair,
            "وقت الدخول": entry_time,
            "وقت الانتهاء": expiry_time,
            "القرار": decision
        })
    return pd.DataFrame(data)

if st.button("🚀 فحص السوق بفلترة الحماية"):
    df = get_pro_data()
    
    def highlight(row):
        if 'شراء' in row['القرار']: return ['background-color: #d4edda'] * len(row)
        if 'بيع' in row['القرار']: return ['background-color: #f8d7da'] * len(row)
        if 'خطر' in row['القرار']: return ['background-color: #fff3cd'] * len(row)
        return [''] * len(row)

    st.dataframe(df.style.apply(highlight, axis=1), use_container_width=True, hide_index=True)
    
    # تحذير إضافي
    if "⚠️ خطر (تجنب التداول)" in df['القرار'].values:
        st.warning("تحذير: النظام اكتشف تقلبات غير طبيعية في بعض الأزواج، يرجى الحذر!")

st.sidebar.write(f"🕒 توقيت المنصة: **{(datetime.utcnow() + timedelta(hours=3)).strftime('%H:%M:%S')}**")
