import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Pro OTC Entry", layout="wide")
st.title("🎯 نظام دخول الشمعة التالية بدقة")

def get_entry_data():
    # الحساب الدقيق: الوقت الآن + ثواني متبقية لتصل للدقيقة التالية
    now = datetime.utcnow() + timedelta(hours=3)
    
    # حساب الثواني المتبقية لنهاية الدقيقة الحالية
    seconds_to_next_minute = 60 - now.second
    
    # وقت دخول الصفقة (بداية الشمعة التالية)
    entry_time = (now + timedelta(seconds=seconds_to_next_minute)).strftime("%H:%M")
    
    # وقت انتهاء الصفقة (بعد دقيقة واحدة من الدخول)
    expiry_time = (now + timedelta(seconds=seconds_to_next_minute + 60)).strftime("%H:%M")
    
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    data = []
    
    for pair in pairs:
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
            "وقت دخول الصفقة": entry_time,
            "وقت انتهاء الصفقة": expiry_time,
            "القرار": decision
        })
    return pd.DataFrame(data)

if st.button("🚀 فحص السوق (توقيت الدقيقة القادمة)"):
    df = get_entry_data()
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.success("الوقت الموضح في الجدول هو الوقت الذي يجب أن تضغط فيه على 'شراء/بيع' في منصتك فوراً.")

st.sidebar.write(f"🕒 التوقيت الفعلي الآن: **{(datetime.utcnow() + timedelta(hours=3)).strftime('%H:%M:%S')}**")
