import streamlit as st
import pandas as pd

# إعداد واجهة احترافية
st.set_page_config(layout="wide", page_title="Pocket Option Auto-Trader")

st.title("🤖 منصة التداول الآلي - Pocket Option")

# شريط جانبي لإدخال البيانات الحساسة (لا تحفظ البيانات داخل الكود)
with st.sidebar:
    st.header("👤 إعدادات الحساب")
    pocket_id = st.text_input("أدخل رقم حسابك (Pocket Option ID):", type="password")
    st.warning("تأكد من رقم الحساب قبل التشغيل.")

# قسم إعدادات التداول
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ إعدادات الصفقات")
    pair = st.selectbox("اختر الزوج:", [
        "EUR/USD", "GBP/USD", "EUR/USD OTC", "GBP/USD OTC"
    ])
    amount = st.number_input("قيمة الصفقة ($):", min_value=1.0, value=10.0)
    
    # زر التشغيل
    if st.button("🚀 بدء التداول على الحساب"):
        if pocket_id:
            st.success(f"تم ربط الحساب: {pocket_id[:4]}****")
            st.info(f"جاري مراقبة {pair}...")
        else:
            st.error("يرجى إدخال رقم الـ ID الخاص بحسابك أولاً.")

with col2:
    st.subheader("📊 لوحة المراقبة")
    st.info("النظام جاهز للربط عبر الـ API.")

# سجل الصفقات
st.markdown("---")
st.subheader("📝 سجل الصفقات")
st.table(pd.DataFrame(columns=['رقم الحساب', 'الزوج', 'الحالة']))
