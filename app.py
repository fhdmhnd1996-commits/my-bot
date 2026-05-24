import streamlit as st
import pandas as pd

# 1. إعداد الصفحة
st.set_page_config(layout="wide", page_title="Pocket Option Bot")

# 2. العنوان
st.title("🤖 منصة التداول الآلي")

# 3. القائمة الجانبية (للبيانات الحساسة)
with st.sidebar:
    st.header("🔑 إعدادات الحساب")
    pocket_id = st.text_input("أدخل رقم حسابك (ID):", type="password")

# 4. إعدادات الصفقات
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ إعدادات الصفقات")
    pair = st.selectbox("اختر الزوج:", ["EUR/USD", "GBP/USD", "EUR/USD OTC"])
    amount = st.number_input("قيمة الصفقة ($):", min_value=1.0, value=10.0)
    
    # زر التشغيل
    if st.button("🚀 بدء التداول"):
        if pocket_id:
            st.success(f"تم ربط الحساب بنجاح!")
        else:
            st.error("يرجى إدخال رقم الـ ID أولاً")

with col2:
    st.subheader("📊 لوحة المراقبة")
    st.info("النظام في وضع الانتظار...")

# 5. سجل الصفقات
st.markdown("---")
st.subheader("📝 سجل الصفقات")
st.table(pd.DataFrame(columns=['الزوج', 'الحالة']))
