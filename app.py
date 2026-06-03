import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Alnze System", page_icon="🛡️")

# دالة للتحقق من البيانات (يمكنك ربطها بقاعدة بيانات لاحقاً)
def check_password(email, password):
    # مثال بسيط: استبدل هذه القيم ببياناتك أو اربطها بقاعدة بيانات
    return email == "admin@alnze.com" and password == "123456"

# إدارة حالة تسجيل الدخول
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# صفحة تسجيل الدخول
if not st.session_state['logged_in']:
    st.title("🛡️ بوابة دخول نظام التداول")
    email = st.text_input("البريد الإلكتروني")
    password = st.text_input("كلمة السر", type="password")
    
    if st.button("تسجيل الدخول"):
        if check_password(email, password):
            st.session_state['logged_in'] = True
            st.rerun() # تحديث الصفحة للدخول للوحة التحكم
        else:
            st.error("البريد أو كلمة السر غير صحيحة")
else:
    # محتوى لوحة التحكم (يظهر فقط بعد تسجيل الدخول)
    st.sidebar.title("إدارة النظام")
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.title("📈 Alnze Trading Dashboard")
    st.write("تم تسجيل الدخول بنجاح إلى نظام Edge Algo الرباعي.")
    
    # هنا ستضع واجهة التحكم في البوت لاحقاً
    st.success("المنصة جاهزة للتشغيل")
