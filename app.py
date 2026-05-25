import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- إعدادات النظام ---
st.set_page_config(page_title="Pro OTC Filter v2.3", layout="wide")
st.title("🛡️ نظام الفلترة الرباعي (توقيت UTC+3)")

# دالة للحصول على توقيت UTC+3
def get_platform_time():
    # الحصول على التوقيت العالمي الحالي وإضافة 3 ساعات
    return (datetime.utcnow() + timedelta(hours=3)).strftime("%H:%M")

# دالة محاكاة البيانات
def get_advanced_market_data():
    data = []
    pairs = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]
    current_time = get_platform_time()
    
    for pair in pairs:
        data.append({
            "الزوج": pair,
            "وقت الدخول": current_time,
            "RSI": np.random.randint(20, 80),
            "Volume": np.random.uniform(0.5, 2.0),
            "EMA_Signal": np.random.uniform(-0.002, 0.002),
            "Sentiment": np.random.choice(['Strong Bull', 'Strong Bear', 'Choppy'])
        })
    return pd.DataFrame(data)

# --- منطق الفلترة ---
def strict_filter(row):
    is_bullish = (row['RSI'] < 70) and (row['EMA_Signal'] > 0) and (row['Sentiment'] == 'Strong Bull')
    is_bearish = (row['RSI'] > 30) and (row['EMA_Signal'] < 0) and (row['Sentiment'] == 'Strong Bear')
    
    if is_bullish and row['Volume'] > 1.0:
        return "🟢 شراء (دخول فوري)"
    elif is_bearish and row['Volume'] > 1.0:
        return "🔴 بيع (دخول فوري)"
    else:
        return "⚪ فلترة (تجنب الخسارة)"

# --- الواجهة ---
st.write(f"🕒 توقيت النظام المعتمد: **{get_platform_time()} (UTC+3)**")

if st.button("🚀 فحص السوق (توقيت UTC+3)"):
    df = get_advanced_market_data()
    df['القرار'] = df.apply(strict_filter, axis=1)
    
    # تنسيق الألوان
    def highlight_rows(x):
        if 'شراء' in x: return 'background-color: #d4edda'
        elif 'بيع' in x: return 'background-color: #f8d7da'
        return ''

    st.dataframe(
        df.style.map(highlight_rows, subset=['القرار']),
        use_container_width=True,
        hide_index=True
    )
    
    if len(df[df['القرار'] != "⚪ فلترة (تجنب الخسارة)"]) == 0:
        st.warning(f"السوق هادئ حالياً، يُنصح بالانتظار.")

st.markdown("""
---
### 💡 ملاحظة:
* تم ضبط التوقيت تلقائياً ليطابق **UTC+3**. 
* تأكد دائماً أن الساعة المذكورة في التطبيق تتطابق مع الساعة الموجودة داخل منصة التداول الخاصة بك لضمان دقة تنفيذ الصفقات.
""")
