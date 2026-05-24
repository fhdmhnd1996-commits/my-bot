import streamlit as st
import pandas as pd

# إعداد واجهة احترافية
st.set_page_config(layout="wide", page_title="Pocket Option OTC Bot")

# 1. Header المنصة
st.title("🚀 Pocket Option - Trading Terminal")
st.markdown("---")

# 2. تقسيم الواجهة
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ إعدادات الصفقات")
    # تم إضافة خيارات الـ OTC هنا
    pair = st.selectbox("1. اسم الزوج:", [
        "EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD", 
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "BTC/USD OTC"
    ])
    value = st.number_input("2. قيمة الصفقة ($):", min_value=1.0, value=10.0)
    sl = st.number_input("3. إيقاف الخسارة ($):", min_value=0.1, value=5.0)
    tp = st.number_input("4. إيقاف الربح ($):", min_value=0.1, value=10.0)
    
    st.markdown("---")
    
    start_btn = st.button("✅ تشغيل التداول")
    stop_btn = st.button("🛑 إيقاف التداول")

with col2:
    st.subheader("📊 الرادار (Live Radar)")
    if start_btn:
        st.success(f"البوت نشط الآن على زوج: {pair}")
        st.write("ملاحظة: سوق الـ OTC يدار داخلياً بواسطة المنصة.")
    elif stop_btn:
        st.error("تم إيقاف النظام.")
    else:
        st.info("النظام في وضع الاستعداد.")

# 3. سجل الصفقات
st.markdown("---")
st.subheader("📝 سجل التداول")
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['الزوج', 'النتيجة', 'الربح'])
st.table(st.session_state.history)
