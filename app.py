import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Alnze Trading Bot", page_icon="📈")

st.title("📈 Alnze Trading Bot")
st.write("مرحباً بك في لوحة التحكم الخاصة بك.")

# رابط تسجيل الدخول الرسمي لمنصة بوكت اوبشن
pocket_option_url = "https://pocketoption.com/en/login/"

# واجهة تسجيل الدخول
st.subheader("🔐 الدخول إلى منصة التداول")
st.write("للبدء، يرجى تسجيل الدخول إلى حسابك في منصة Pocket Option:")

# زر يوجه المستخدم إلى المنصة في نافذة جديدة
if st.button("تسجيل الدخول إلى Pocket Option"):
    st.markdown(f'<a href="{pocket_option_url}" target="_blank" style="text-decoration:none; color:white; background-color:blue; padding:10px 20px; border-radius:5px;">اضغط هنا للتوجه لصفحة الدخول الرسمية</a>', unsafe_allow_html=True)

st.divider()

# زر تشغيل النظام (يظهر فقط لمن يريد البدء بعد تسجيل الدخول)
if st.button("تشغيل العملية"):
    st.info("نظام التداول (Edge Algo + Spot-0079 + S/R) قيد التشغيل...")
