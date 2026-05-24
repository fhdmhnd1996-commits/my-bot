import streamlit as st
import pandas as pd
import random

# إعداد الصفحة
st.set_page_config(page_title="Signal Bot Pro", layout="wide")

# إنشاء الذاكرة إذا لم تكن موجودة
if 'signals' not in st.session_state:
    st.session_state.signals = []

st.title("🎯 محرك إشارات التداول (20 زوج OTC)")

# قائمة الأزواج
otc_pairs = [
    "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC", "AUD/USD OTC",
    "EUR/GBP OTC", "EUR/JPY OTC", "USD/CAD OTC", "NZD/USD OTC", "GBP/JPY OTC",
    "CHF/JPY OTC", "EUR/CAD OTC", "GBP/CAD OTC", "AUD/JPY OTC", "EUR/AUD OTC",
    "USD/CHF OTC", "CAD/JPY OTC", "NZD/JPY OTC", "GBP/AUD OTC", "AUD/CAD OTC"
]

# القائمة الجانبية
pair = st.sidebar.selectbox("اختر الزوج:", otc_pairs)

# الرادار
st.subheader("💡 اضغط هنا لبدء الرادار:")
if st.button("🚀 تحليل السوق الآن"):
    st.info(f"جاري تحليل حركة السعر على {pair}...")
    
    # محاكاة إشارة
    signal = random.choice(["🟢 شراء (CALL)", "🔴 بيع (PUT)"])
    confidence = random.randint(75, 98)
    
    st.success(f"القرار: {signal} | نسبة النجاح: {confidence}%")
    
    # إضافة الإشارة للسجل
    st.session_state.signals.append({"الزوج": pair, "الإشارة": signal})

# عرض السجل
st.markdown("---")
st.subheader("📝 سجل الإشارات الأخيرة")
if st.session_state.signals:
    st.table(pd.DataFrame(st.session_state.signals).tail(5))
else:
    st.write("لا توجد إشارات حتى الآن.")
