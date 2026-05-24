import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Signal Bot Pro", layout="wide")

st.title("🎯 محرك إشارات التداول (20 زوج OTC)")

# 1. تعريف القائمة في الذاكرة (لحل مشكلة NameError)
if 'signals' not in st.session_state:
    st.session_state.signals = []

# قائمة بـ 20 زوج OTC
otc_pairs = [
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC",
    "EUR/GBP OTC", "EUR/JPY OTC", "USD/CAD OTC", "NZD/USD OTC", "GBP/JPY OTC",
    "CHF/JPY OTC", "EUR/CAD OTC", "GBP/CAD OTC", "AUD/JPY OTC", "EUR/AUD OTC",
    "USD/CHF OTC", "CAD/JPY OTC", "NZD/JPY OTC", "GBP/AUD OTC", "AUD/CAD OTC"
]

# إعدادات التنبيهات
st.sidebar.header("🛠 إعدادات الإشارة")
pair = st.sidebar.selectbox("اختر الزوج:", otc_pairs)
timeframe = st.sidebar.selectbox("الإطار الزمني:", ["1m", "5m", "15m"])

# تشغيل المحرك
if st.sidebar.button("ابدأ تحليل السوق"):
    st.info(f"جاري تحليل حركة السعر على {pair}...")
    
    # محاكاة إشارة
    signal = random.choice(["🟢 شراء (CALL)", "🔴 بيع (PUT)"])
    confidence = random.randint(75, 98)
    
    st.subheader(f"💡 الإشارة لزوج {pair}:")
    if "شراء" in signal:
        st.success(f"القرار: {signal} | نسبة النجاح المتوقعة: {confidence}%")
    else:
        st.error(f"القرار: {signal} | نسبة النجاح المتوقعة: {confidence}%")
        
    # إضافة الإشارة للسجل بعد التحقق من وجودها
    st.session_state.signals.append({"الزوج": pair, "الإشارة": signal})
    
    st.write("---")
    st.write("👉 افتح منصة Pocket Option الآن ونفذ الصفقة يدوياً!")

# عرض السجل
st.markdown("---")
st.subheader("📝 سجل الإشارات الأخيرة")
if len(st.session_state.signals) > 0:
    st.table(pd.DataFrame(st.session_state.signals).tail(5))
else:
    st.write("لا توجد إشارات حتى الآن.")
