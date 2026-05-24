import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(layout="wide", page_title="Pocket Option Auto-Bot")

st.title("🤖 نظام التداول الآلي الاحترافي")

# 1. إعدادات الحساب (ID)
with st.sidebar:
    st.header("👤 إعدادات الحساب")
    pocket_id = st.text_input("رقم حسابك في Pocket Option:", type="password")
    st.info("سيتم استخدام هذا الـ ID للربط الآمن.")

# 2. تقسيم الواجهة
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ إعدادات الصفقات")
    
    # 2. أزواج OTC
    pair = st.selectbox("اختر الزوج:", [
        "EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", 
        "BTC/USD OTC", "AUD/USD OTC"
    ])
    
    # 3. قيمة الصفقة
    amount = st.number_input("قيمة الصفقة ($):", min_value=1.0, value=10.0)
    
    # 4 & 5. إدارة المخاطر
    stop_loss = st.number_input("إيقاف الخسارة عند ($):", value=50.0)
    take_profit = st.number_input("إيقاف الربح عند ($):", value=100.0)
    
    st.markdown("---")
    
    # 7. تشغيل وإيقاف البوت
    start_bot = st.button("✅ تشغيل البوت الآلي")
    stop_bot = st.button("🛑 إيقاف البوت الآلي")

with col2:
    # 6. الرادار (Live Radar)
    st.subheader("📊 رادار السوق (Live Radar)")
    if start_bot:
        if pocket_id:
            st.success(f"🚀 البوت يعمل الآن على حساب: {pocket_id[:3]}***")
            st.write(f"المراقبة جارية على: **{pair}**")
            st.warning("جاري تحليل الشموع وتوقع الصفقات...")
        else:
            st.error("⚠️ يرجى إدخال رقم الـ ID أولاً!")
    elif stop_bot:
        st.error("🛑 تم إيقاف البوت الآلي بنجاح.")
    else:
        st.info("نظام الرادار في وضع الاستعداد. اضغط تشغيل للبدء.")

# سجل الصفقات
st.markdown("---")
st.subheader("📝 سجل الصفقات")
st.table(pd.DataFrame(columns=['الوقت', 'الزوج', 'الصفقة', 'النتيجة']))
