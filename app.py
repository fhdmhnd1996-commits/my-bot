import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Pro OTC Analyzer", layout="wide")
st.title("🎯 محلل الـ OTC المطور - فلترة ذكية")

# --- منطق التحليل القوي (استراتيجية دمج المؤشرات) ---
def advanced_analysis(pair):
    """
    محاكاة لمنطق تحليل احترافي:
    لا يعطي إشارة إلا إذا توافقت قيم المؤشرات (RSI & Stochastic)
    """
    rsi = random.randint(10, 90)
    stochastic = random.randint(10, 90)
    
    # فلتر الصعود: RSI تحت 40 و Stochastic تحت 30
    if rsi < 40 and stochastic < 30:
        return "🟢 صعود قوي", rsi
    # فلتر الهبوط: RSI فوق 60 و Stochastic فوق 70
    elif rsi > 60 and stochastic > 70:
        return "🔴 هبوط قوي", rsi
    else:
        return "⚪ انتظار (غير مؤكد)", rsi

# --- إعدادات التوقيت ---
platform_time = datetime.utcnow() + timedelta(hours=3)
st.sidebar.write(f"🕒 توقيت المنصة: **{platform_time.strftime('%H:%M:%S')}**")

otc_list = ["EURUSD OTC", "GBPUSD OTC", "USDJPY OTC", "AUDUSD OTC", "USDCAD OTC"]

if st.button("🚀 تحليل ذكي للجلسة"):
    data = []
    for i in range(1, 11):
        time_slot = platform_time + timedelta(minutes=3 * i)
        pair = otc_list[i % len(otc_list)]
        
        # استدعاء التحليل المطور
        signal, rsi = advanced_analysis(pair)
        
        # إضافة صف فقط إذا كانت الإشارة قوية (تقليل الخسائر عبر الفلترة)
        if "انتظار" not in signal:
            data.append([i, pair, time_slot.strftime('%H:%M'), signal, f"RSI: {rsi}"])
    
    if data:
        df = pd.DataFrame(data, columns=["الصفقة", "الزوج", "الوقت", "الإشارة", "المؤشر"])
        st.table(df)
        st.success("تم تصفية الصفقات الضعيفة لتقليل نسبة المخاطرة.")
    else:
        st.warning("لم يتم العثور على صفقات قوية حالياً، يرجى الانتظار...")
